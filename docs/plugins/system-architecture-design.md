# System Architecture Design

バージョン：0.2.0。カテゴリ：DeveloperTools。

アプリと Backend の責務、依存方向、命名、API 契約、YAGNI を設計する Codex プラグインです。
3 つの SKILL と、共通の配置と契約を扱う参照資料を含みます。
フレームワーク固有の実装は専用スキルが担当し、SwiftUI + TCA には [iOS Development](ios-development.md) を使用します。

## 導入と利用条件

[導入ガイド](../install.html)に従ってこのマーケットプレイスを追加し、`system-architecture-design` を選んでインストールしてください。
追加認証や MCP 接続は不要です。
対象コードとローカルの設計規約を読み取れる環境で利用します。
利用許諾は [README の利用条件](https://github.com/beyond-labo/beyond-labo-marketplace#利用条件)を確認してください。

## 含まれる SKILL

- [App Architecture Design](../skills/app-architecture-design.md)：クライアントの UI 状態と汎用の機能境界。
- [Backend Architecture Design](../skills/backend-architecture-design.md)：HTTP と保存の境界、層名の判断、公開契約。
- [UNIX Design Principles](../skills/unix-design-principles.md)：システム分割、合成、運用のトレードオフ。

## 0.1.0 からの変更

新規設計の既定を、ソースルート直下の `<Feature>/<Layer>`、PascalCase / UpperCamelCase と単数形の `UseCase` 等へ揃えました。
これはこの配布物の既定です。対象プロジェクトの明示ルールとツールの制約を優先します。
Backend の Presentation / Infrastructure と Adapter による配置を比較でき、特定の層名を Clean Architecture の必須要件として扱いません。
App の状態管理は採用方式に合わせ、ViewModel を必須にしません。

プラグイン名と既存 SKILL 名は変更していません。
更新後も既存アプリを一括改名する必要はありません。
古い規約を改訂する場合は、既存配置と新しい既定の差を確認し、移行する範囲を別途定めてください。
[変更履歴](../changelog.md)と[利用例による確認](../architecture-examples.md)も参照できます。
