"""Behavioral checks for relocatable distribution and project settings updates."""
import contextlib
import importlib.util
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SKILL = Path(__file__).resolve().parents[1]
PLUGIN = SKILL.parents[1]
spec = importlib.util.spec_from_file_location('setup_project', SKILL / 'scripts/setup_project.py')
setup_project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup_project)


def files(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.project = self.root / 'consumer'
        self.project.mkdir()

    def test_plan_is_readonly_and_install_does_not_create_spec_or_agents(self):
        result = setup_project.setup(self.project)
        self.assertGreater(len(result['files']), 16)
        self.assertEqual(files(self.project), {})
        setup_project.setup(self.project, apply=True)
        self.assertFalse((self.project / '.kiro/specs').exists())
        self.assertFalse((self.project / 'AGENTS.md').exists())
        self.assertFalse((self.project / '.codex').exists())
        before = files(self.project)
        setup_project.setup(self.project, apply=True)
        self.assertEqual(files(self.project), before)

    def test_update_managed_only_and_preserve_existing_customizations(self):
        assets = self.root / 'assets'
        shutil.copytree(SKILL / 'assets', assets)
        custom = self.project / '.kiro/settings/templates/specs/design.md'
        custom.parent.mkdir(parents=True)
        custom.write_text('custom template')
        setup_project.setup(self.project, apply=True, assets=assets)
        profile = self.project / '.kiro/settings/okf-profile.md'
        template = assets / 'settings/templates/specs/design.md'
        template.write_text('new upstream template')
        (assets / 'settings/okf-profile.md').write_text('new upstream profile')
        result = setup_project.setup(self.project, apply=True, assets=assets)
        self.assertEqual(custom.read_text(), 'custom template')
        self.assertEqual(profile.read_text(), 'new upstream profile')
        self.assertEqual(result['preserved_local'], 1)
        profile.write_text('local profile edits')
        (assets / 'settings/okf-profile.md').write_text('next upstream profile')
        setup_project.setup(self.project, apply=True, assets=assets)
        self.assertEqual(profile.read_text(), 'local profile edits')

    def test_symlink_preflight_prevents_any_write(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (self.project / '.kiro').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            setup_project.setup(self.project, apply=True)
        self.assertEqual(files(outside), {})

    def test_malformed_install_state_prevents_write(self):
        state = self.project / setup_project.STATE
        state.parent.mkdir(parents=True)
        state.write_text('[]')
        before = files(self.project)
        with self.assertRaises(ValueError):
            setup_project.setup(self.project, apply=True)
        self.assertEqual(files(self.project), before)

    def test_relocated_plugin_templates_links_and_cli(self):
        relocated = self.root / 'cache with spaces' / 'okf-sdd'
        shutil.copytree(PLUGIN, relocated, ignore=shutil.ignore_patterns('__pycache__'))
        skill = relocated / 'skills/kiro-spec-sync'
        for doc in relocated.rglob('*.md'):
            text = re.sub(r'```.*?```', '', doc.read_text(), flags=re.S)
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                if ':' in target or target.startswith('#'):
                    continue
                path = (doc.parent / target.split('#')[0]).resolve()
                self.assertTrue(path.is_relative_to(relocated), (doc, target))
                self.assertTrue(path.exists(), (doc, target))
        subprocess.run([sys.executable, str(skill / 'scripts/setup_project.py'), '--root', str(self.project), '--apply'], check=True, stdout=subprocess.DEVNULL)
        feature = self.project / '.kiro/specs/sample'
        feature.mkdir(parents=True)
        templates = self.project / '.kiro/settings/templates'
        for template in templates.rglob('*.md'):
            rendered = re.sub(r'\{\{[^}]+\}\}', 'Example', template.read_text())
            metadata = yaml.safe_load(rendered.split('---', 2)[1])
            self.assertIsInstance(metadata['type'], str)
            self.assertEqual(metadata['sources'], [])
        initial = (templates / 'specs/init.json').read_text().replace('{{FEATURE_NAME}}', 'sample').replace('{{TIMESTAMP}}', '2026-09-10T00:00:00Z')
        (feature / 'spec.json').write_text(initial)
        rendered = re.sub(r'\{\{[^}]+\}\}', 'Example', (templates / 'specs/requirements-init.md').read_text())
        (feature / 'requirements.md').write_text(rendered)
        before = files(self.project)
        result = subprocess.run([sys.executable, str(skill / 'scripts/okf.py'), 'check', '--root', str(self.project), '--feature', 'sample'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(files(self.project), before)
        self.assertEqual(json.loads(result.stdout)['scanned_specs'], 1)


if __name__ == '__main__':
    unittest.main()
