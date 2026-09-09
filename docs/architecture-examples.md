# 設計スキルの利用例と確認範囲

更新したスキルを小さな入力へ適用し、配置と責務を机上で確認した記録です。
以下の出力は設計例であり、実際の iOS アプリ、Swift コンパイル、TestStore、Simulator の実行結果ではありません。
このリポジトリには今回の例に対応するアプリ実装を追加していません。

## Hosting の取得画面

入力：

```text
$ios-tca-development で Hosting の取得画面を設計してください。
SwiftUI + TCA + Clean Architecture を採用します。
機能名はソースルート直下、役割名は UseCase 等とします。
取得結果には日時と状態 enum があり、画面終了時には通信をキャンセルします。
アプリ本体とバージョン選定は今回の対象外です。
```

適用結果：

| 責務 | 配置候補 | 入力と出力 |
| --- | --- | --- |
| 画面 | `Hosting/Presentation/View/HostingView.swift` | State を描画し、Action を送る |
| 状態遷移 | `Hosting/Presentation/Reducer/HostingReducer.swift` | State と Action を同居。取得 Effect とキャンセルを制御 |
| UseCase の呼び出し口 | `Hosting/Presentation/Dependency/HostingUseCasesDependency.swift` | Application の取得操作と結果だけを公開 |
| 取得操作 | `Hosting/Application/UseCase/LoadHosting.swift` | Port を使い、内部の Hosting を返す |
| 必要な取得契約 | `Hosting/Application/Port/HostingRepository.swift` | 生成型を含まない取得操作 |
| 業務モデル | `Hosting/Domain/Model/Hosting.swift` | 内部の日付と状態。不変条件を所有 |
| API 接続 | `Hosting/Infrastructure/Adapter/HostingAPIAdapter.swift` | 生成 Client を呼び、Port を実装 |
| 独立した変換 | `Hosting/Infrastructure/Mapper/HostingAPIMapper.swift` | 日時と未知 enum を検証し、内部モデルか失敗へ変換 |
| 組み立て | `App/Composition/BuildApp.swift` | Client、Adapter、UseCase を作り Store へ注入 |

生成クライアントを共通で使う責務が生じれば `Platform/Networking/Generated` に置きます。
Platform から Hosting のモデルを参照しません。
日時と enum の変換には独立した境界条件があるため、この例では Mapper を分離する判断にしました。

静的依存は Presentation から Application、Application から Domain、Infrastructure から Application / Domain へ向きます。
生成 DTO を知る箇所は通信基盤と API Adapter / Mapper の範囲に収まります。
ViewModel、別の ObservableObject、横断 DTO 変換層は必要ありません。
`Features` 階層を作らず、`UseCase` の表記で機能の下に配置できます。

将来必要になる検証は、取得成功と失敗の TestStore、画面終了時の Effect と通信のキャンセル、遅延した結果の扱い、UseCase、日時と enum の変換です。
実装前の依頼なので、今回作る成果物は設計文書のみです。
Xcode プロジェクト、予約ソース、CI、OpenAPI の仮ファイルは作りません。

## 単純な変換の所有

入力：

```text
API の一つの ID を内部の ID へ変換するだけで、利用箇所は Adapter 一か所です。
Mapper と変換プロトコルを先に分けるべきか判断してください。
```

適用結果：Adapter の private 関数に置きます。
独立した責務のない Mapper ファイルとプロトコルは追加しません。
生成 DTO を受け取る Domain initializer も作らないため、内側への外部型依存を避けられます。

## Backend の命名が未決の場合

入力：

```text
$backend-architecture-design で HTTP 境界を整理してください。
規約には Presentation / Infrastructure があり、会話には Adapter 案がありますが未承認です。
```

適用結果：既存配置を維持し、二つの候補を責務表で比較します。
Adapter 案なら受信を `Hosting/Adapter/Inbound/Handler`、送信を `Hosting/Adapter/Outbound/Repository` とし、Application を介して接続します。
Infrastructure を残すのは、低水準 Driver 等の別の責務がある場合だけです。
同じ通信の中継だけなら Adapter と Infrastructure の二重実装は提案しません。
この比較を承認済みの移行や実装済み構成とは報告しません。

## 対象プロジェクトの命名制約

入力：

```text
機能と役割は UseCase のような camelケースで設計してください。
配置は apps/backend/src と apps/ios です。package.json と既存の npm 識別子は維持します。
別の対象プロジェクトには小文字パッケージを使う明示規約があります。
```

適用結果：最初の対象では UpperCamelCase と解釈したことを示し、たとえば `apps/backend/src/Hosting/Application/UseCase` を候補にします。
配置用ディレクトリと規定ファイル、識別子は改名しません。
別の対象では小文字の明示規約を優先し、配布物の既定を理由に一括改名しません。

## 独立した契約更新

入力：

```text
Backend の公開状態 enum に値を追加します。旧 iOS が残っています。
Backend 内部型を packages/contracts に共有して通常ビルドを最新に揃える案を評価してください。
```

適用結果：Backend の HTTP スキーマから OpenAPI を生成し、互換性を確認します。
iOS の通常ビルドは固定済み契約を維持し、契約更新の変更で生成版と成果物を更新します。
旧デコーダーが未知 enum を拒否する可能性を検証し、単なる追加変更だから互換と判断しません。
Backend 内部型と DTO のソース共有は行わず、それぞれのアプリが内部モデルを所有します。

## スキルの選択

| 入力の目的 | 主に使用するスキル |
| --- | --- |
| フレームワーク未選定の画面境界 | app-architecture-design |
| Backend の受信と送信の責務、層名 | backend-architecture-design |
| サービス分割の運用コストと合成 | unix-design-principles |
| SwiftUI + TCA の実装、DTO 変換、TestStore | ios-tca-development |

iOS の設計でも汎用原則は参照しますが、同じ ViewModel の実装手順を重ねて適用しません。
これらの机上確認は指示の矛盾と配置の問題を検討するためのものです。
独立したエージェントの実行評価やアプリの動作保証を行ったものではありません。

## 配布物の検証結果

2026-09-06 に、変更した 2 プラグインを `validate_plugin.py`、4 スキルを `quick_validate.py` で検証し、すべて成功しました。
検証用の一時 Python 環境には PyYAML 6.0.3 を使用しました。

カタログの既存エントリーと表示順を保持し、4 プラグインと 9 スキルの名前、パス、ポリシー、カテゴリ、UI メタデータ、公開ページの登録を照合しました。
変更したプラグインのバージョンと紹介ページも一致しています。
Pages の公開ルートを考慮した 72 件のローカルリンク、プラグイン内の参照先、リポジトリ正本への URL のローカル対応先を確認しました。
公開前の新しい正本 URL がリモートから取得可能になったことまでは確認していません。
`git diff --check` は成功し、端末固有のホームパスの検索では該当を検出しませんでした。

既存の個人用 architecture SKILL とインストールキャッシュは、変更前の配布ソースと同一内容でした。
配布ソースを唯一の更新対象とし、コピー先は変更していません。
アプリファイルの変更、利用者環境へのインストール、push、PR 作成、公開は実施していません。

## 2026-09-10 の main 統合時の再検証

最新 main の表形式カタログと追加済みの図やグラフ用プラグインを維持して、この変更を統合しました。
既存カタログの表示順を保ち、iOS Development を末尾に追加しています。
2 プラグインと 4 スキルの公式 validator、7 プラグインと 12 スキルの登録整合、105 件のローカルリンクを再確認しました。
既存の導入ページが参照する `index.html#plugins` を維持するため、カタログに対応するアンカーを追加しました。
アプリのビルドや Simulator 検証は今回も対象外です。
