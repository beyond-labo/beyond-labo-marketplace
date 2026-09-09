# App Architecture Design

クライアントの画面、機能、フローについて、フレームワークに依存しない境界設計やレビューに使います。
UI 状態の所有者、UseCase、ナビゲーション、外部作用と静的依存を明確にします。
MVVM では ViewModel、Reducer 方式では State / Action / Reducer / Store に表示の責務を割り当てます。

## 前提条件

[System Architecture Design](../plugins/system-architecture-design.md) を導入し、対象の規約と既存の UI 方式を確認できること。
SwiftUI + TCA の実装、DTO 変換、TestStore の手順には [iOS TCA Development](ios-tca-development.md) を使います。

## 配置と責務

新規設計の既定はソースルート直下の `<Feature>/<Layer>` と、`UseCase`、`Port` 等の単数形です。
対象プロジェクトの規約とツール制約を優先します。
生成 DTO は外部境界に閉じ込め、空の層や将来用の予約ファイルは作りません。

## プロンプト例

```text
$app-architecture-design で、この画面追加の境界を設計してください。
既存の状態管理方式を維持し、UI 状態、ナビゲーション、UseCase、外部 API 変換の所有者を示してください。
実装に必要な配置と、将来の文書上の候補を分けてください。
```
