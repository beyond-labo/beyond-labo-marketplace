# Backend Architecture Design

API、サービス、Backend 機能の設計やレビューに使います。
機能所有、公開契約、データ、UseCase、Port と Adapter の境界を整理します。

## 前提条件

[System Architecture Design](../plugins/system-architecture-design.md) を導入し、対象の既存コード、設計の決定記録、HTTP 契約と外部依存を確認できること。

## 層名と契約の判断

Presentation / Infrastructure を既存規約として維持する方法と、Adapter の Inbound / Outbound に分ける方法を比較します。
どちらかを唯一の Clean Architecture の層名として強制しません。
Port は内側の契約、Gateway は外部接続の役割、HTTP は通信方式として区別します。
未承認の配置案を採用済みとして扱いません。

新規設計の既定は `<Feature>/<Layer>`、`Application/UseCase` 等の単数形です。
Backend 所有の HTTP スキーマから OpenAPI を生成し、利用側が固定した契約を使う流れを基本に、既存方式と独立リリースの条件を確認します。

## プロンプト例

```text
$backend-architecture-design で、この HTTP 機能をレビューしてください。
Presentation / Infrastructure と Adapter の入力側と出力側の配置候補を、責務と依存方向で比較してください。
既存の決定と未承認の提案を区別し、Port の所有者と旧クライアントへの互換性も確認してください。
```
