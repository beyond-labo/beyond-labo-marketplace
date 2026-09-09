---
name: app-architecture-design
description: Design or review framework-neutral client application boundaries, UI state ownership, navigation, use cases, and dependency direction. Use for cross-platform architecture decisions; use ios-tca-development for SwiftUI + TCA implementation, API mapping, and TestStore workflows, and backend-architecture-design for server boundaries.
---

# App Architecture Design

クライアントの機能所有、UI 状態、依存方向を設計する。
具体的なフレームワークの実装手順を扱う専用スキルがある場合、その API とテスト手順は専用スキルに委ねる。

## 設計の進め方

1. ローカル規約と既存 UI の状態管理方式を読み、[共通の配置、責務、契約](../../references/architecture-boundaries.md)を適用する。
2. 独立して変更と検証ができる最小の機能について、画面契約、ユーザー操作、状態の所有者、UseCase、外部作用を特定する。
3. 機能をソースルート直下に置き、実在する責務だけを `<Feature>/<Layer>/<Role>` に割り当てる。
4. 静的依存と実行時の流れ、機能間の契約、ナビゲーション、Composition の配線を示す。
5. 既存配置からの移行を伴う変更と機能追加を区別し、実施した検証と未決の判断を報告する。

## 状態と依存の所有

| 領域 | 責務 | 静的な依存先 |
| --- | --- | --- |
| Domain | 業務概念と不変条件 | 通常の言語型。UI や外部 SDK を知らない |
| Application | UseCase、業務操作の調整、呼び出し側の Port | Domain |
| Infrastructure | 通信や保存の Adapter と境界変換 | Application / Domain の契約 |
| Presentation | View、表示状態と表示ロジック、ナビゲーション、UI の操作 | Application と UI フレームワーク |
| Composition | Adapter と UseCase と画面の組み立て | 必要な各実装 |

上の名前はクライアント向けの配置例であり、唯一の Clean Architecture の層名ではない。
Presentation の状態所有者は採用方式に合わせる。
MVVM なら ViewModel、Reducer 方式なら State / Action / Reducer / Store が担い、両方式を機械的に重ねない。
フレームワークが必要とする場合だけ Controller を用意する。

実行は `View → 表示ロジック → UseCase → Port の実装 → 外部システム` として説明する。
Reducer 方式の非同期処理なら Effect 等を介す。
静的依存は `Presentation → Application → Domain`、`Infrastructure → Application / Domain` とし、Composition が具体的実装を注入する。
View、表示ロジック、UseCase から具体的な HTTP Client や Repository を構築しない。

Domain と Application に UI、画面状態、ナビゲーション、生成 API 型、具体的 SDK を import しない。
表示用の整形や画面寿命に伴うキャンセルは Presentation、業務上の判断は Application / Domain が所有する。
機能間の通信は明示的な結果や操作の契約を介し、他機能の Presentation / Infrastructure 実装を直接参照しない。

## 配置の例とレビュー

以下は実際に責務がある場合の配置候補であり、生成すべきファイル一覧ではない。

```text
src/Hosting/Presentation/View/HostingView
src/Hosting/Application/UseCase/CreateHosting
src/Hosting/Application/Port/HostingRepository
src/Hosting/Domain/Model/Hosting
src/Hosting/Infrastructure/Adapter/HostingAPIAdapter
src/App/Composition/BuildApp
```

レビューでは、状態の二重所有、View への業務処理の混入、生成型の漏出、内部型のアプリ間共有、形式だけの Mapper / Repository ラッパーを確認する。
UI 状態と操作、UseCase の成功と失敗、外部契約の変換、Composition の配線を、それぞれ実装済みの範囲で検証する。
iOS の SwiftUI + TCA では `ios-tca-development` を利用できる場合に読み、ViewModel を追加せず、その版に対応した TestStore と Simulator の手順で検証する。
