# iOS TCA Development

SwiftUI + TCA + Clean Architecture を選定した iOS 機能の実装やレビューに使います。
TCA の画面状態と Effect、UseCase の注入、API DTO の変換、キャンセル、TestStore と Simulator の検証を扱います。

## 前提条件

[iOS Development](../plugins/ios-development.md) を導入し、対象アプリの規約、採用版、HTTP 契約を確認できること。
具体的な版が未選定なら互換性確認から始めます。
ビルドと Simulator 実行には、対応する Xcode と実在するプロジェクトが必要です。

## 境界と検証

機能はソースルート直下へ配置し、`Hosting/Application/UseCase`、`Hosting/Presentation/Reducer` 等を使います。
State と Action は必要がなければ Reducer ファイルへ同居させ、別の ViewModel / ObservableObject は重ねません。
Domain と Application は TCA、Dependencies、UI、生成 API 型に依存しません。

Presentation の依存 bridge から UseCase を呼び、App/Composition が Adapter と UseCase を組み立てて注入します。
Presentation の liveValue では具体的 Infrastructure を生成しません。
API 変換は機能の Infrastructure が所有し、小さな変換は Adapter 内から始めます。

TestStore の状態遷移と Effect、UseCase の業務処理、Mapper の不正値と未知 enum、キャンセル伝播を確認します。
構成検証、単体テスト、アプリビルド、Simulator 上の起動と操作を区別して報告します。
未実装の予約ファイルや必ず失敗する CI を作りません。

## プロンプト例

```text
$ios-tca-development でこの取得画面をレビューしてください。
TCA dependency bridge と Composition の配線、生成 DTO の参照範囲、キャンセル時の表示を確認してください。
採用版を根拠に修正し、実行したテスト、ビルド、Simulator 検証と未実施の項目を報告してください。
```

設計のみの場合は次のように依頼できます。

```text
$ios-tca-development で Hosting の画面構成を文書化してください。
アプリと TCA の具体的な版は未選定です。最小の責務と必要になる検証を示し、予約ソースやプロジェクト設定は作成しないでください。
```
