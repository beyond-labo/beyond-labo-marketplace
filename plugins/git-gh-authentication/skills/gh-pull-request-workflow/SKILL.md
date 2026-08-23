---
name: gh-pull-request-workflow
description: Commit selected Git changes, push a branch, and create or inspect a GitHub pull request with GitHub CLI. Use when a user explicitly asks to commit, push, open, update, view, or prepare a pull request, including draft PRs and PR descriptions.
---

# GitHub Pull Request Workflow

Publish a deliberate, reviewable change set. Use local Git for staging and commits, and `gh` for GitHub authentication checks and PR operations.

## Confirm scope

Before staging, inspect the worktree and the intended files:

```bash
git status --short --untracked-files=all
git diff --stat
git diff -- <path>
```

If unrelated changes exist, stage only explicit paths. Do not use `git add -A` or `git add .` unless the user confirmed that the whole worktree belongs in the PR. Do not amend, reset, rebase, force-push, or overwrite a remote branch without explicit authorization.

## Commit selected changes

Run relevant validation before commit when it has not already run. Then verify the staged set:

```bash
git add <path...>
git diff --cached --check
git diff --cached --name-status
git commit -m "<concise conventional summary>"
```

After the commit, confirm the remaining worktree state. Report any uncommitted files rather than silently including them in a later commit.

## Authenticate and push

Check the CLI before GitHub operations:

```bash
gh --version
gh auth status
```

If authentication fails, use `git-gh-authentication` and confirm `gh auth status` succeeds before creating or reading a PR. Push only when the user asked to publish the branch:

```bash
git push -u origin <branch>
```

## Create a pull request

Create a PR only with explicit user authorization. Determine the base from an explicit user request or the remote default branch; do not assume it. Default to a draft PR unless the user asks for review-ready status.

### PR language

Write the PR title and body in the language the user requests.

When the user does not specify a language, infer it from the request and the repository's user-facing documentation.

Do not default to English merely because Git, GitHub CLI, branch names, code identifiers, or commands use English.

Keep commands, file paths, code identifiers, and GitHub API fields unchanged.

Apply the same rule when updating an existing PR.

### Japanese PR body template

When creating a Japanese PR, start from [PULL_REQUEST_TEMPLATE_JA.md](assets/PULL_REQUEST_TEMPLATE_JA.md).

Use a Japanese title that states both the changed target and the change itself.

Avoid generic titles such as `update` or `fix` when they do not identify the review scope.

Replace every placeholder with the actual change details, remove sections that do not apply, and list only validation that was actually run.

In `概要`, state what changed, why it changed, and whether external contracts change.

In `主な対応内容`, describe each substantial change as a concrete noun phrase rather than a completion report.

In `既存契約への影響`, name affected APIs, user flows, configuration, CI, or compatibility, and state explicitly when there is no impact.

Use `レビュー時に見てほしい点` for design decisions and compatibility risks that require reviewer attention.

Write a Markdown body to a temporary file. Include the change summary, impact on existing contracts, validation actually run, and review focus. Do not embed Markdown directly in the shell command.

```bash
gh pr create \
  --draft \
  --base <default-branch> \
  --head <branch> \
  --title "<clear title>" \
  --body-file <temporary-body-file>
```

After creation or update, verify the result:

```bash
gh pr view <number-or-url> --json title,body,url,isDraft,baseRefName,headRefName
```

Report the URL, branch, commit, base branch, validation, and any remaining user action.
