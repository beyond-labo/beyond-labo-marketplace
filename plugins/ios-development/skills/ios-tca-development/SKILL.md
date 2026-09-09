---
name: ios-tca-development
description: Implement or review iOS features using SwiftUI, TCA, and Clean Architecture, including dependency composition, generated API boundaries, DTO mapping, cancellation, and TestStore or Simulator verification. Use after this stack is selected; use app-architecture-design for framework-neutral client boundaries, not as an extra ViewModel workflow.
---

# iOS TCA Development

SwiftUI + TCA + Clean Architecture を選定済みの iOS 機能を実装またはレビューする。
この組み合わせとフォルダー配置は本スキルの設計方針であり、TCA 公式の必須構成ではない。
既存アプリの別方式からの移行は、依頼の範囲に含まれる場合だけ行う。

汎用の配置、Port / Adapter の責務、モデル所有と YAGNI の詳細は System Architecture Design が所有する。
利用可能なら `app-architecture-design` の[共通資料の正本](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/system-architecture-design/references/architecture-boundaries.md)を参照する。
別プラグインが隣のパスへインストールされるとは仮定しない。
単独導入時も以下の iOS 境界を適用できる。共通資料が取得できなくても自動インストールを行わず、プロジェクト規約を優先して参照の未確認を明記する。

## 実装前の選定と範囲

1. 対象の規約、実装済みの画面と処理、契約成果物、Xcode プロジェクトまたは Swift package を確認する。
2. 最低 iOS、Xcode と Swift、TCA、swift-dependencies、API 生成ツールと runtime / transport の選定版および `Package.resolved` を照合する。[版と一次資料の確認](references/versions-and-verification.md)を読む。
3. 未選定なら、互換性を確認した候補と根拠を提示する。版が決まる前に最新 API が使用可能と断言したり、依存更新を既成事実にしたりしない。
4. 今回の一つの操作について、画面状態、業務処理、契約変換、依存注入、必要な検証を決める。設計のみの依頼なら文書で止め、実装を依頼されていれば動作する最小の処理を作る。

## 機能配置と状態の所有

この配布物の新規設計向け既定は、ソースルート直下の `<Feature>/<Layer>` と PascalCase / UpperCamelCase、単数形の役割名である。
ローカル規約と言語やツールの制約を優先し、`apps/ios` 等の配置用ディレクトリや規定ファイル名は改名しない。
`Features` / `features` の中間階層を挟まない。
次は実装時の配置候補であり、一括生成するスキャフォールドではない。

```text
<SourceRoot>/Hosting/Presentation/View/HostingView.swift
<SourceRoot>/Hosting/Presentation/Reducer/HostingReducer.swift
<SourceRoot>/Hosting/Presentation/Dependency/HostingUseCasesDependency.swift
<SourceRoot>/Hosting/Application/UseCase/CreateHosting.swift
<SourceRoot>/Hosting/Application/Port/HostingRepository.swift
<SourceRoot>/Hosting/Domain/Model/Hosting.swift
<SourceRoot>/Hosting/Infrastructure/Adapter/HostingAPIAdapter.swift
<SourceRoot>/Hosting/Infrastructure/Mapper/HostingAPIMapper.swift
<SourceRoot>/App/Composition/BuildApp.swift
```

SwiftUI View が Action を Store へ送り、Reducer が State の更新と Effect を定義する。
Effect から UseCase を呼び、結果を内側の型で Action に返す。
State と Action は必要がなければ Reducer ファイルへ同居させる。
MVVM の描画と表示ロジックの分離は保つが、TCA の上に別の ViewModel / ObservableObject を重ねない。

画面状態、ナビゲーション、画面寿命に伴う Effect のキャンセルは Presentation が所有する。
親は子 Reducer を合成し、子の結果は delegate Action 等の明示的な契約で受け取る。
全機能の業務データをアプリ全体 State に重複保持しない。
業務処理の調整は Application、不変条件は Domain に置く。
表示用の日時や文言の整形は Presentation が担当し、必要なら Domain モデルを直接 State に保持する。
層ごとに同形の表示 DTO を増やさない。

## TCA dependency bridge と Composition

静的依存は `Presentation → Application → Domain`、`Infrastructure → Application / Domain` とする。
Domain と Application は `ComposableArchitecture`、`Dependencies`、SwiftUI、生成 API 型に依存しない。
通常の Swift 型、async 関数、protocol またはクロージャで UseCase と Port を表し、依存は初期化引数で渡す。

Presentation の `Dependency` に置く薄い bridge は、Application が公開する入出力だけを露出する。
Application の公開 API が Domain の値を返す場合はその値を使え、境界ごとに包み直す必要はない。
Reducer は `@Dependency` 等、その版で対応する方法により bridge を受け取り、Effect 内で UseCase を実行する。
bridge は通信 Client ではなく UseCase の呼び出し口である。

`App/Composition` が生成 Client、Adapter、UseCase を組み立て、Store 生成時に依存を注入する。
Presentation の `liveValue` で具体的 Infrastructure を生成しない。
選定版が対応していれば、インターフェースの `TestDependencyKey` と実装側の `DependencyKey` の分離や Store の dependency override を使う。
キーの適合と既定値が必要な場合は、未注入が検出できる形にする。
未注入を空配列や成功応答で隠さず、本番配線が実際に override されることを検証する。
テストと Preview には明示的な代替値を渡す。

## API と DTO の境界

Backend 所有の HTTP スキーマから生成した、固定版またはハッシュ付きの OpenAPI を受け取る。
iOS 側で選定版のツールによりクライアントを生成し、自身の内部モデルへ変換する。
Backend の TypeScript 内部型や API DTO のソースを `packages/contracts` 等から直接共有しない。
通常の iOS ビルドが最新 Backend の変更や稼働中スキーマの取得に依存しないようにする。
旧 iOS のデコードと操作が維持されるかを、契約更新時に確認する。

共通の通信基盤が必要なら `Platform/Networking/Generated` に生成クライアントを置く。
Platform は機能のモデル、SwiftUI、TCA を知らない。
生成型を参照できるのは通信基盤と機能固有の API Adapter / Mapper だけとし、Domain、Application、State、Action へ漏らさない。

API Adapter が通信と変換を組み合わせ、Application の Port を実装する。
単純で一か所だけの変換は Adapter の private 関数から始める。
独立した検証が必要になった場合に `Hosting/Infrastructure/Mapper/HostingAPIMapper` 等へ分ける。
Domain の initializer に生成 DTO を渡さず、横断 DTO 変換層を作らない。

未知の enum、不正な日時、欠落や範囲外の必須値は、生成デコーダーと Mapper の両方で扱いを確認する。
デコード時点で失敗すれば Mapper には届かないため、生成コードの未知値対応も検証する。
業務として意味がある場合だけ未知値を内部で表現し、それ以外は Application が扱える失敗へ翻訳する。
不正値を無条件に既定値へ置き換えない。
HTTP ステータスや SDK エラーの詳細を UI Action に載せず、通信失敗、認証切れ、契約不整合等の意味へ変換する。

## 非同期処理と検証

- 画面の終了、再検索、同じ操作の連打でキャンセルする対象と ID を定める。Reducer の Effect から UseCase、Port、transport までキャンセルが伝わることを確かめる。
- `CancellationError` だけでなく採用 transport のキャンセル表現を確認する。キャンセルを通常の通信失敗表示や自動リトライへ変換しない。遅れて届く古い結果が新しい状態を上書きしないことも検証する。
- 選定 Swift の並行処理チェックに従い、境界値とクロージャの `Sendable` / `@Sendable`、actor isolation を確認する。警告を消すだけの `@unchecked Sendable`、`Task.detached`、無根拠な actor 追加で回避しない。
- TestStore で Action、State、Effect の結果、失敗、キャンセル、親子のナビゲーションを対象操作に応じて検証する。時刻や待機は制御可能な Clock と代替依存を使い、残った Effect と予期しない Action を確認する。
- UseCase は代替 Port で成功、業務失敗、キャンセルを検証する。Mapper / Adapter は DTO の正常値、不正値、未知値、エラー翻訳を検証する。Domain の不変条件は通常の Swift テストで確かめる。
- プロジェクトが存在すれば Simulator 向けビルドとテストを行い、本番 Composition を通した起動と主要操作も確認する。Preview やモックだけの確認を本番配線の成功と表現しない。

空の層や型、コメントだけのソース、開けない Xcode プロジェクト、無効な OpenAPI、未選定ツールの設定、必ず失敗する予約 CI は作らない。
将来の配置は文書へ残す。
実装済みの処理のみを検証し、構成検証、単体テスト、ビルド、Simulator 実行の結果と未実施理由を分けて報告する。
