#!/usr/bin/env python3
"""Plan/apply bundled settings; preserve pre-existing and locally edited files."""
import argparse
import hashlib
import json
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
STATE = '.kiro/settings/okf-sdd-install.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_target(root, relative):
    if relative.startswith('/') or '..' in Path(relative).parts:
        raise ValueError('path must stay inside project')
    path = root / relative
    for item in [path, *path.parents]:
        if item == root:
            break
        if item.is_symlink():
            raise ValueError('symlink target is not supported: ' + relative)
        if item != path and item.exists() and not item.is_dir():
            raise ValueError('parent is not a directory: ' + relative)
    if path.exists() and not path.is_file():
        raise ValueError('target is not a file: ' + relative)
    return path


def setup(root, apply=False, assets=ASSETS):
    root = Path(root)
    if not root.is_dir() or root.is_symlink():
        raise ValueError('root must be an existing non-symlink directory')
    root = root.resolve()
    state_path = safe_target(root, STATE)
    old = json.loads(state_path.read_text()) if state_path.exists() else {'schema': 1, 'files': {}}
    if (not isinstance(old, dict) or old.get('schema') != 1 or not isinstance(old.get('files'), dict)
            or any(not isinstance(k, str) or not isinstance(v, str) or len(v) != 64 for k, v in old['files'].items())):
        raise ValueError('invalid install state; review it manually')
    owned = dict(old['files'])
    plan, writes = [], []
    for source in sorted((assets / 'settings').rglob('*')):
        if source.is_symlink():
            raise ValueError('bundled asset must not be a symlink')
        if not source.is_file():
            continue
        relative = '.kiro/settings/' + source.relative_to(assets / 'settings').as_posix()
        target = safe_target(root, relative)
        data = source.read_bytes()
        current = target.read_bytes() if target.exists() else None
        if current == data:
            action = 'unchanged'
        elif current is None:
            action = 'create'
        elif owned.get(relative) == digest(current):
            action = 'update'
        else:
            action = 'preserve-local'
        plan.append({'path': relative, 'action': action})
        if action in ('create', 'update'):
            writes.append((target, data))
            owned[relative] = digest(data)
    # Preflight all paths before writing anything. No AGENTS, agent registration,
    # specs, approval state, or generated knowledge is installed.
    if apply:
        for target, data in writes:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        if writes:
            state_path.parent.mkdir(parents=True, exist_ok=True)
            state_path.write_text(json.dumps({'schema': 1, 'files': owned}, indent=2) + '\n')
    return {'applied': apply, 'files': plan,
            'preserved_local': sum(p['action'] == 'preserve-local' for p in plan)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--apply', action='store_true', help='write only new or unchanged-since-install assets')
    args = parser.parse_args(argv)
    try:
        print(json.dumps(setup(args.root, args.apply), ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
