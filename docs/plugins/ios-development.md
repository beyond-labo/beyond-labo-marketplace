# iOS Development

バージョン：0.1.0。カテゴリ：DeveloperTools。

SwiftUI + TCA + Clean Architecture を採用した iOS 機能を設計、実装、レビューする Codex プラグインです。
[iOS TCA Development](../skills/ios-tca-development.md) 一つに、状態管理、API 境界、依存注入、検証をまとめています。
TCA の上に別の ViewModel を重ねず、Domain と Application を TCA と生成 API 型から分離します。

## 導入と利用条件

[導入ガイド](../install.html)に従ってこのマーケットプレイスを追加し、`ios-development` を選んでインストールしてください。
追加認証や MCP 接続は不要です。
設計には対象規約と契約の情報、実装と Simulator 検証には対応する macOS / Xcode、依存ライブラリと対象プロジェクトが必要です。
外部 API の実通信を行う場合の資格情報と権限は対象アプリの環境で用意します。
利用許諾は [README の利用条件](https://github.com/beyond-labo/beyond-labo-marketplace#利用条件)を確認してください。

## 他のプラグインとの境界

汎用の命名、Port / Adapter の責務、API 契約と YAGNI の詳細は [System Architecture Design](system-architecture-design.md) が所有します。
iOS Development は iOS 固有の実装と検証を所有し、単独導入も可能です。
他プラグインのインストール位置を仮定せず、利用可能なスキルまたは公開された正本を参照します。

この構成は設計上の選択であり、TCA 公式が Clean Architecture や同じフォルダー名を必須にしているわけではありません。
TCA の採用方針と具体的な版の選定を分け、実装時に最低 iOS、Xcode / Swift、解決した依存を確認します。

## 利用例

```text
$ios-tca-development で Hosting の取得画面を実装してください。
既存の採用バージョンと固定した OpenAPI を確認し、TCA の Effect から UseCase を呼び出してください。
DTO の不正値と未知 enum、キャンセル、依存注入を検証し、TestStore と Simulator の結果を区別して報告してください。
```

[小さな設計例](../architecture-examples.md)と[変更履歴](../changelog.md)も参照できます。
