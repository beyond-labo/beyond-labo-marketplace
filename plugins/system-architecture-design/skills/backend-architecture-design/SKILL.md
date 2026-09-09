---
name: backend-architecture-design
description: Design or review server feature ownership, HTTP and persistence boundaries, use cases, ports, dependency direction, and public API contracts. Use for backend architecture and layer naming decisions; use app-architecture-design for client UI boundaries and unix-design-principles for system decomposition tradeoffs.
---

# Backend Architecture Design

Backend の機能、公開契約、データと外部作用の所有者を決める。
実装前に既存コードとローカルの決定記録を読み、[共通の配置、責務、契約](../../references/architecture-boundaries.md)を適用する。

## 依存方向と責務

Domain は業務モデルと不変条件、Application は UseCase と業務処理の調整を所有する。
Port は呼び出し側の内側に定義し、通常は `Application/Port`、業務概念自体が必要とする場合は `Domain/Port` とする。
HTTP フレームワーク、DB ドライバー、SDK、公開 DTO を内側へ import しない。

受信境界は認証情報の取り出し、入力形式の検証、UseCase 呼び出し、結果とエラーの HTTP 応答への変換を所有する。
業務上の認可判断や不変条件は UseCase / Domain に残す。
送信境界は Port を実装して DB や外部 API に接続し、外部形式と内側のモデルを変換する。
Composition が接続の設定と具体的実装を組み立てる。

```text
静的依存:
受信境界 → Application → Domain
送信境界 → Application / Domain の Port
Composition → 必要な各実装

実行:
HTTP Handler → UseCase → Port の実装 → DB / 外部 API
```

## Backend の外側に付ける名前

Clean Architecture 原典の Interface Adapters は Controller / Presenter と外部データ変換を含む領域である。
Presentation は原典の層名ではない。
次の候補を対象プロジェクトの語彙と既存責務に合わせて比較し、一つを唯一の正解として強制しない。

| 候補 | 受信境界 | 送信境界 | 判断点 |
| --- | --- | --- | --- |
| Presentation / Infrastructure | `Hosting/Presentation/Handler` | `Hosting/Infrastructure/Repository` | 既存規約で Presentation が HTTP 入出力を意味するなら維持できる。UI 専用語と誤解されない説明が必要 |
| Adapter に集約 | `Hosting/Adapter/Inbound/Handler` | `Hosting/Adapter/Outbound/Repository` | 入力と出力を明示する。Inbound / Outbound は方向を表す区分で、別の業務層ではない |

後者で Infrastructure も使うなら、接続プールや低水準の Driver 等、Adapter とは異なる責務がある場合だけ設ける。
Adapter は契約への適合と変換、Infrastructure は実接続の技術機構を所有するよう定義する。
同じ HTTP 呼び出しを両方で包むだけなら一つにまとめる。
入力 Adapter が出力 Adapter を直接呼ぶ構成にせず、Application を経由して役割を分離する。
HTTP は通信方式、Gateway は外部接続の役割、Port は内側の契約なので、この表の層名の代用として並べない。

文書に Presentation / Infrastructure、会話に Adapter 案が残る場合は、前者の決定日と後者の承認状態、実装を照合する。
未承認の案を採用済みに書き換えず、変更対象でなければ既存配置を維持したうえで未決論点として報告する。

## 機能設計と検証

1. 機能をソースルート直下に置く。たとえば `src/Hosting/Application/UseCase/CreateHosting` と `src/Hosting/Domain/Model/Hosting`。役割は `UseCase`、`Port`、`Handler`、`Mapper` 等の単数形にする。
2. 機能ごとのデータ所有、UseCase の入力と結果、トランザクション、外部失敗とリトライの責務を定める。必要な場合に冪等性やイベント契約を設計する。
3. 機能間では明示的な契約を用い、他機能の境界実装を import しない。共有は所有者が明確で複数機能が実際に使う安定した概念に限る。
4. 共通資料の生成方向に沿って、Backend の HTTP スキーマから OpenAPI を生成し、固定した成果物で利用側を更新する。旧クライアントを含む互換性を検証する。
5. 業務不変条件、差し替えた Port に対する UseCase、HTTP の正常応答と不正入力、永続化や外部接続の変換と失敗を実装済みの範囲で確認する。

成果物には責務表、静的依存、公開契約、採用した命名と理由、未決の設計判断、実際に実行した検証を含める。
空の層や予約 CI を作って実装済みと表現しない。
