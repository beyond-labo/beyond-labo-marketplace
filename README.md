# Beyond Labo Marketplace

Beyond Labo が提供する Codex プラグインと SKILL のマーケットプレイスです。

各プラグインの目的とプロンプト例は、[プラグインガイド](https://beyond-labo.github.io/beyond-labo-marketplace/) で公開しています。

## プラグイン一覧

- [System Architecture Design](docs/plugins/system-architecture-design.md)：アプリケーションとシステムのアーキテクチャを設計・レビューします。
- [Git & GitHub Workflow](docs/plugins/git-gh-authentication.md)：ブランチ操作、GitHub CLI 認証、PR 作成を安全に進めます。
- [対話・コミュニケーション](docs/plugins/communication-writing.md)：日本語の技術文書と説明文を推敲します。

- [Archify](docs/plugins/archify.md)：システム構成や処理の流れを、検証可能な JSON と単体 HTML の図にします。
- [Graphify](docs/plugins/graphify.md)：コードと文書を横断する知識グラフを構築し、出典と関係を探索します。
- [CodeGraph](docs/plugins/codegraph.md)：ソースコードのシンボル、呼び出し関係、変更影響とテスト候補を調べます。

3ツールの分類と責務、CLI を採用した理由は[構成検討記録](docs/research/architecture-graph-tools.md)を参照してください。
各ツールの実行環境はプラグインと別に準備します。

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
