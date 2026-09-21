# Codex Model Routing

`codex-model-routing` は、タスクの難易度と役割に応じて Codex の親モデル、オーケストレーター、SubAgent のモデル構成を選ぶプラグインです。
通常は GPT-5.6 Terra または GPT-5.6 Sol、目的と受け入れ条件が明瞭なタスクは GPT-5.6 Luna、さらに高度で長い推論を要する場合は GPT-6 Astra を使います。

## 導入

[導入ガイド](../install.html)に従ってマーケットプレイスを追加し、`codex-model-routing` をインストールします。
以下の `personal` は、このカタログをその名前で登録した場合の例です。

```bash
codex plugin marketplace upgrade personal
codex plugin add codex-model-routing@personal
```

追加後は新しいタスクから利用します。

## 構成と利用条件

| 項目 | 内容 |
| --- | --- |
| プラグイン | `codex-model-routing` |
| バージョン | `0.1.0` |
| カテゴリ | `Productivity` |
| SKILL | [Codex Model Routing](../skills/codex-model-routing.md) |
| MCP、常駐処理 | 同梱なし |
| 認証 | 不要 |
| 対象 | Codex のタスク、オーケストレーター、SubAgent |

このプラグインは、モデルを提供したりアカウントへ追加したりしません。
利用できるモデルは、Codex の実行環境とアカウントの提供状況に依存します。

## モデル方針

| モデル | 役割 |
| --- | --- |
| GPT-5.6 Luna | 目的、範囲、受け入れ条件が明瞭で、狭く閉じられる実行タスクと、すべての SubAgent |
| GPT-5.6 Terra | 一定の判断を含む通常の実装、レビュー、調査 |
| GPT-5.6 Sol | 曖昧で複雑な複数段階タスクと、そのオーケストレーション |
| GPT-6 Astra | 新規性、矛盾した制約、高い失敗コスト、長い推論が複数重なる最難関タスク |

モデルの一般的な位置付けは、[OpenAI のモデル一覧](https://developers.openai.com/api/docs/models)と[SubAgent の公式ガイド](https://learn.chatgpt.com/docs/agent-configuration/subagents)を基準にしています。
その上で、SubAgent を Luna に統一し、Luna へ渡せない難所を親の Sol または Astra が保持することを、このプラグイン固有の運用方針としています。

## プロンプト例

```text
$codex-model-routing を使い、このタスクに適した親モデルと SubAgent の構成を決めてください。
```

```text
$codex-model-routing で、この複雑な移行作業を Luna の SubAgent に委譲できる単位へ分解し、親を Sol と Astra のどちらにするか判断してください。
```

## 責務の境界

このプラグインは、モデル選択、タスク分割、委譲時のモデル方針を扱います。
実装手順、設計規範、Git 操作、仕様管理などは、それぞれの業務 SKILL が担います。

モデル選択は、SubAgent の作成、新しいタスクの作成、外部サービスへの書き込みを自動的に許可するものではありません。
現在のタスクでモデルを変更できない場合は、次のタスクまたは SubAgent に適用する構成を示します。
SubAgent を Luna に固定できない実行環境では、SubAgent を起動せず親が作業を保持します。
利用できないモデルを黙って別モデルへ置き換えません。
