# Git & GitHub Workflow

Git ブランチ操作、GitHub CLI の認証状態確認とデバイス認証、コミット・push・PR 作成を扱うプラグインです。3つの SKILL により、それぞれの外部変更の境界を明確にします。

- バージョン: `0.1.0+codex.20260815055613`
- カテゴリ: `DeveloperTools`
- 含まれる SKILL:
  - [Git & GitHub CLI Authentication](../skills/git-gh-authentication.md)
  - [Git Branch Workflow](../skills/git-branch-workflow.md)
  - [GitHub Pull Request Workflow](../skills/gh-pull-request-workflow.md)

## 導入

このリポジトリを Codex のマーケットプレイスとして登録後、`git-gh-authentication` をインストールしてください。

```text
codex plugin marketplace add <marketplace-root>
```

## 責務の境界

認証、ブランチ操作、PR 作成を別々の SKILL が担当します。いずれも、ユーザーの明示的な依頼がない限り、push、PR 作成、リポジトリ設定、GitHub アカウントの SSH 公開鍵登録を実行しません。
