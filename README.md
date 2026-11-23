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

- [OKF + SDD](docs/plugins/okf-sdd.md)：18スキルで現行の知識、仕様、承認、検証の整合を保ちます。
- [Marketplace Updater](docs/plugins/marketplace-updater.md)：別の作業環境で見つかった問題を、配布元のスキル改善へ反映します。
- [Codex Model Routing](docs/plugins/codex-model-routing.md)：タスクの難易度と役割に応じて、親モデルと SubAgent のモデル構成を選びます。
- [Unslop](docs/plugins/unslop.md)：Web と iOS の既存画面を監査し、製品らしい見た目へ整えます。

3ツールの分類と責務、CLI を採用した理由は[構成検討記録](docs/research/architecture-graph-tools.md)を参照してください。
各ツールの実行環境はプラグインと別に準備します。

## インストール

Codex アプリの画面からマーケットプレイスを追加する手順は、[インストールガイド](docs/install.html) を参照してください。

初めて追加する場合は、リポジトリをローカルへ複製する必要はありません。

Codex の「プラグイン」画面で、このリポジトリの GitHub URL と `main` ブランチを指定します。

## 利用条件

`plugins/unslop/` 全体と `docs/plugins/unslop.md`、`docs/skills/unslop.md` は、[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で配布します。
unslop の作者は Damir Sokolovsky ([@heydamir](https://x.com/heydamir))、上流は [heydamir/unslop](https://github.com/heydamir/unslop) です。
Beyond Labo が Codex 向けの導線と iOS 適用手順を追加しました。
作者、出典、ライセンス、改変表示を保持してください。
全文と免責は [LICENSE](plugins/unslop/LICENSE)、帰属と変更の範囲は [NOTICE.md](plugins/unslop/NOTICE.md) にあります。

上記以外の部分には、現時点で利用許諾を定めるリポジトリ全体の `LICENSE` ファイルがありません。
その部分の利用、複製、改変、再配布の可否を確認したい場合は、事前にリポジトリの管理者へ連絡してください。

プラグインの利用時は、各プラグインが必要とする認証、権限、外部サービスの利用条件にも従ってください。

設定値、API キー、アクセストークンなどの秘密情報を、Issue、Pull Request、プラグイン設定へ投稿しないでください。

機能の改善や追加を提案する場合は、[GitHub Issues](https://github.com/beyond-labo/beyond-labo-marketplace/issues) または Pull Request を利用してください。

## 開発者向け

プラグイン、カタログ、公開ドキュメントを変更するときは、リポジトリの [運用規約](AGENTS.md) に従ってください。

別のプロジェクトで使ったスキルを改善したい場合は、[Marketplace Updater](docs/skills/marketplace-updater.md) を利用できます。
「今回の問題を防ぐため、対象スキル自体を改善して」と依頼すると、インストール情報から配布元を特定して修正と検証を進めます。
PR 作成まで依頼すれば、公開に必要な操作も続けます。
