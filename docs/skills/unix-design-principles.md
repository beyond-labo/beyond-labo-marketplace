# UNIX Design Principles

アーキテクチャ、API、モジュール、サービス、データフロー、運用設計の評価に使います。責務、境界、合成、可観測性、失敗の隔離、分割粒度を検討します。

## 前提条件

[System Architecture Design](../plugins/system-architecture-design.md) を導入し、対象の目的、主要ユースケース、品質要件、既存の制約を共有できること。

個々の App / Backend の層配置は対応する architecture SKILL、iOS TCA の実装は [iOS TCA Development](ios-tca-development.md) が担当します。
空の層や同形 DTO の複製を単純化とみなさず、実在する処理だけを検証します。

## プロンプト例

```text
このサービス分割案を UNIX 設計原則で評価してください。分ける理由、安定させる契約、隔離する失敗、移行と検証を示してください。
```
