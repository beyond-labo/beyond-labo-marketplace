# Beyond Labo Marketplace

Beyond Labo の Codex プラグインと SKILL を配布するマーケットプレイスです。

## 導入

Codex アプリの画面から追加する手順は、[インストールガイド](install.md) を参照してください。

コマンドで追加する場合は、次の手順を使います。

このリポジトリをローカルに取得したあと、リポジトリのルートをマーケットプレイスとして登録します。

```bash
codex plugin marketplace add .
```

次に、目的のプラグインを追加します。

```bash
codex plugin add <plugin-name>@personal
```

追加後は新しいタスクで SKILL を利用してください。

## プラグイン一覧

- [System Architecture Design](plugins/system-architecture-design.md)：アプリケーションとシステムのアーキテクチャを設計・レビューします。
- [Git & GitHub Workflow](plugins/git-gh-authentication.md)：ブランチ操作、GitHub CLI 認証、PR 作成を安全に進めます。
- [対話・コミュニケーション](plugins/communication-writing.md)：日本語の技術文書と説明文を推敲します。

## SKILL 一覧

- [App Architecture Design](skills/app-architecture-design.md)
- [Backend Architecture Design](skills/backend-architecture-design.md)
- [UNIX Design Principles](skills/unix-design-principles.md)
- [Git & GitHub CLI Authentication](skills/git-gh-authentication.md)
- [Git Branch Workflow](skills/git-branch-workflow.md)
- [GitHub Pull Request Workflow](skills/gh-pull-request-workflow.md)
- [japanese-tech-writing](skills/japanese-tech-writing.md)
- [cognitive-rhythm-writing](skills/cognitive-rhythm-writing.md)
