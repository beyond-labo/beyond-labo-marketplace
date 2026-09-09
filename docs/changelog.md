# 変更履歴

## 2026-09-06

### System Architecture Design 0.2.0

- 共通の命名、責務、API 契約、YAGNI を一つの参照資料へ集約。
- 新規設計の既定を、機能直下の層、PascalCase / UpperCamelCase と単数形の役割へ統一。既存規約と言語やツールの制約を優先。
- Backend の HTTP 境界の命名候補と、Adapter / Infrastructure の重複を避ける判断を追加。
- App の ViewModel 前提を外し、状態管理方式に応じた所有者を明示。
- アプリごとのモデル所有、固定契約からの生成、旧クライアントとの互換性、境界での DTO 変換を整理。
- 空のスキャフォールドを避け、構成検証とアプリ検証を区別。

既存 SKILL 名の変更や削除はありません。
新しい既定に合わせた既存アプリの一括移行は不要です。
明示的に構成を移行する場合は、対象コードと規約の変更範囲を決めてから進めてください。

### iOS Development 0.1.0

- `ios-tca-development` を追加。SwiftUI + TCA + Clean Architecture の実装とレビューを一つのスキルで扱う。
- dependency bridge、Composition、DTO 変換、キャンセルと Sendable、TestStore、Simulator 検証を追加。
- 採用版の照合手順と、一次資料の確認範囲を記録。

ローカルに重複する architecture SKILL がある場合、このリポジトリの `plugins/system-architecture-design` が配布の正本です。
今回、個人用スキルやインストールキャッシュは変更していません。
古いコピーと新しい配布版を併用する場合は、明示的に配布版を選択するか、利用者の管理下で重複を整理してください。
