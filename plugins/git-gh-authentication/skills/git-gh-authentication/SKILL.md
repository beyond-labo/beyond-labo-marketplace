---
name: git-gh-authentication
description: Diagnose and complete GitHub CLI authentication for Git and GitHub workflows. Use when `gh auth status` fails, a token is invalid or expired, a user asks to sign in to GitHub CLI, or Git/GitHub operations require verified authentication before push or pull-request work.
---

# Git & GitHub CLI Authentication

Authenticate GitHub CLI safely before a Git or GitHub operation. Keep this skill limited to authentication and verification; push, PR creation, repository changes, and SSH-key registration require their own explicit user authorization.

## Workflow

1. Confirm the repository and intended operation, then run `gh --version` and `gh auth status`.
2. If `gh auth status` succeeds, use the existing session. Do not start a new authentication flow.
3. If it fails because the account is missing, the token is invalid, or the token expired, explain the failure and start device authentication only with user authorization.
4. Use the SSH protocol without changing the user's GitHub SSH-key settings:

   ```bash
   gh auth login --hostname github.com --git-protocol ssh --skip-ssh-key --web --clipboard
   ```

5. Keep the same terminal or execution session alive until device authentication finishes. If prompted to press Enter to open the URL, send Enter to that same process; do not terminate it, close its input, or begin a second flow.
6. Share the displayed `https://github.com/login/device` URL and one-time code only with the user who authorized authentication. Ask them to approve the device in their browser.
7. Wait for the same `gh auth login` process to report success, then run `gh auth status` again. Continue with Git or GitHub work only after this check passes.

## Device-flow safety

- Treat the device code as short-lived authentication material. Do not commit it, add it to files, logs, PR text, or share it with anyone other than the authorizing user.
- Never ask the user to paste a personal access token, password, recovery code, or MFA code into chat.
- Do not upload, generate, replace, or delete an SSH key unless the user separately requests that account change. Keep `--skip-ssh-key`.
- Do not interpret browser approval alone as success. The local `gh` process must complete and `gh auth status` must pass.

## Failed or interrupted flows

If the browser approval completed but `gh auth status` still fails, the local process probably exited before receiving the approval. Start one new device flow, preserve that process until completion, and use only its newly issued code. Do not reuse an older code.

If `gh` is unavailable, ask the user to install it. If the account lacks repository access after successful authentication, report the authorization failure; do not switch accounts, alter repository permissions, or create a token without explicit authorization.

## Handoff to Git and GitHub work

After successful authentication, verify the repository remote and branch before any network-changing action. Run a push or create a PR only when the user explicitly requested it. For a PR, create a draft by default and write the body to a temporary file rather than embedding Markdown in a shell command.
