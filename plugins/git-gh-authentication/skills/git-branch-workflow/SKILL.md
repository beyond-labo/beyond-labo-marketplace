---
name: git-branch-workflow
description: Create, inspect, switch, and update Git work branches safely. Use when a user asks to start work from the latest remote default branch, create or rename a feature branch, check branch status, or prepare a clean branch before implementation, commit, push, or pull-request work.
---

# Git Branch Workflow

Manage local branches without losing uncommitted work or assuming the repository's default branch.

## Inspect before changing state

Run these checks before switching, pulling, or creating a branch:

```bash
git status --short --branch
git branch --show-current
git remote -v
```

Treat uncommitted changes as user-owned unless their scope is clear. Do not reset, checkout paths, stash, clean, or switch away from a dirty branch without explicit user approval.

## Start from the latest default branch

When the user asks to start from the remote default branch:

1. Discover the default branch from `origin`; do not assume `main` or `master`.
2. Fetch `origin`, switch to that branch only when the worktree is safe to change, then update it with a fast-forward-only pull.
3. Create the requested branch from the updated commit and confirm its tracking state.

Use this sequence after resolving the intended branch name:

```bash
git remote show origin
git fetch origin
git switch <default-branch>
git pull --ff-only origin <default-branch>
git switch -c <new-branch>
git status --short --branch
```

If the remote cannot be reached, report that the base cannot be verified. Do not claim the branch is current from cached remote refs alone.

## Branch naming and existing branches

Follow repository-local naming rules before choosing a name. If none exist, use a concise purpose-oriented name such as `feature/<topic>` or `fix/<topic>`. Do not overwrite, force-move, or delete an existing branch. If the requested name already exists, report its current target and ask whether to use it or select another name.

## Switching and updating an existing branch

Before switching, ensure that uncommitted changes will not be affected. Before integrating the default branch into an existing feature branch, ask whether the user wants merge or rebase when the repository has no local rule. Never use force-push as part of normal branch maintenance.

## Handoff

Branch creation does not authorize a commit, push, or PR. Use a dedicated commit/pull-request workflow only when the user explicitly requests publication.
