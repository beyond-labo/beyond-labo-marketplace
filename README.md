# Beyond Labo Marketplace

Beyond Labo が提供する Codex プラグインと SKILL のマーケットプレイスです。

各プラグインの目的とプロンプト例は、[プラグインガイド](https://beyond-labo.github.io/beyond-labo-marketplace/) で公開しています。

## プラグイン一覧

- [System Architecture Design](docs/plugins/system-architecture-design.md)：アプリケーションとシステムのアーキテクチャを設計・レビューします。
- [Git & GitHub Workflow](docs/plugins/git-gh-authentication.md)：ブランチ操作、GitHub CLI 認証、PR 作成を安全に進めます。
- [対話・コミュニケーション](docs/plugins/communication-writing.md)：日本語の技術文書と説明文を推敲します。

## インストール

Codex アプリの画面からマーケットプレイスを追加する手順は、[インストールガイド](docs/install.html) を参照してください。

初めて追加する場合は、リポジトリをローカルへ複製する必要はありません。

Codex の「プラグイン」画面で、このリポジトリの GitHub URL と `main` ブランチを指定します。

## 利用条件

このリポジトリには、現時点で利用許諾を定める `LICENSE` ファイルがありません。

利用、複製、改変、再配布の可否を確認したい場合は、事前にリポジトリの管理者へ連絡してください。

プラグインの利用時は、各プラグインが必要とする認証、権限、外部サービスの利用条件にも従ってください。

設定値、API キー、アクセストークンなどの秘密情報を、Issue、Pull Request、プラグイン設定へ投稿しないでください。

機能の改善や追加を提案する場合は、[GitHub Issues](https://github.com/beyond-labo/beyond-labo-marketplace/issues) または Pull Request を利用してください。

## 開発者向け

プラグイン、カタログ、公開ドキュメントを変更するときは、リポジトリの [運用規約](AGENTS.md) に従ってください。
