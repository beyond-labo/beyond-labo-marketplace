# 版と一次資料の確認

## 実装に使う版の決め方

アプリの最低 iOS、`xcodebuild -version`、`swift --version`、プロジェクト設定、`Package.resolved` を最初に照合する。
TCA だけでなく、解決した swift-dependencies、macro 依存、API generator と runtime / transport も確認する。
採用タグの `Package.swift`、版別 manifest があればそのファイル、移行ガイドと API の宣言を読む。
main ブランチの例を、そのまま古い採用版のコードに持ち込まない。
確認できない項目は未確認と記録し、ライブラリの最低 OS から Xcode の対応版を推測しない。

## 一次資料と確認範囲

2026-09-06 の参照確認で得た情報は次のとおり。
これは採用版の指定や、アプリのビルド済み対応表ではない。

| 資料 | 確認した内容 | 実装時に再確認するもの |
| --- | --- | --- |
| [TCA releases](https://github.com/pointfreeco/swift-composable-architecture/releases/latest) | 確認時の latest は 1.26.2 | 採用タグ、リリース日、移行上の変更 |
| [1.26.2 Package.swift](https://raw.githubusercontent.com/pointfreeco/swift-composable-architecture/1.26.2/Package.swift) | tools version 6.4、iOS 16、Swift language mode 6 の宣言 | 使用 toolchain が選ぶ manifest、推移的依存、実際のビルド |
| [TCA README](https://github.com/pointfreeco/swift-composable-architecture) | main の例に `@Reducer`、`@ObservableState`、Effect、Store、TestStore がある | 同じ API が採用タグで利用できるか、Observation と最低 OS の条件 |
| [Dependencies の DependencyKey ソース](https://github.com/pointfreeco/swift-dependencies/blob/main/Sources/Dependencies/DependencyKey.swift) | interface と live implementation のキー適合を分ける方法を説明 | 採用版の `TestDependencyKey` / `DependencyKey`、注入 API、Sendable 要件 |
| [Swift OpenAPI Generator](https://github.com/apple/swift-openapi-generator) | OpenAPI からの Swift コード生成を提供する候補 | 採用版のスキーマ対応、runtime と transport の互換性、再生成方法 |
| [Swift concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) | Swift の並行処理仕様の参照先 | 採用言語モードの隔離、Sendable、キャンセルの仕様 |

1.26.2 の README、Cancellation.swift、Store.swift のタグ指定 URL は、この調査では取得できなかった。
したがって main のサンプルを 1.26.2 固有の API として検証済みにはしていない。
必要な API の採用タグが閲覧できなければ、取得済みのパッケージソースか公式のタグ別資料で確認してから実装する。
Swift concurrency の Web ページ本文も今回の取得では展開されず、仕様の実地確認は実装時に行う。

## アプリ実装で残す証拠

- 対象操作、採用版の一覧、参照したタグと API、構成の意図。
- TestStore の入力 Action、期待 State、受信する結果 Action、残存 Effect とキャンセルの扱い。
- UseCase と Mapper / Adapter テストの境界条件と実行結果。
- 実在する scheme と利用可能な Simulator destination を確認して実行したビルドとテストのコマンド、その結果。
- 本番 Composition による起動と主要操作の確認結果。実通信を試したか、代替 transport だったかも区別する。

`xcodebuild -list` と `xcodebuild -showdestinations -scheme <scheme>` は対象プロジェクトを明示して使用する。
テストは確認した project / workspace、scheme、destination を用いる。
アプリも選定ツールも存在しない設計段階ではこれらを実行したと扱わず、必要になる条件を文書へ記録する。
