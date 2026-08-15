# Git & GitHub CLI Authentication

GitHub CLI の認証状態確認、デバイス認証、認証後の再確認を扱うプラグインです。トークンやパスワードをチャットで扱わず、SSH 公開鍵の登録も明示的な依頼なしには行いません。

- バージョン: `0.1.0`
- カテゴリ: `DeveloperTools`
- 含まれる SKILL: [Git & GitHub CLI Authentication](../skills/git-gh-authentication.md)

## 導入

このリポジトリを Codex のマーケットプレイスとして登録後、`git-gh-authentication` をインストールしてください。

```text
codex plugin marketplace add <marketplace-root>
```

## 責務の境界

このプラグインは認証とその確認だけを担当します。push、PR 作成、リポジトリ設定、GitHub アカウントの SSH 公開鍵登録は、別途明示的に依頼された場合だけ実行します。
