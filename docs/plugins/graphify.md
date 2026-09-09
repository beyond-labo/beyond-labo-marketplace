# Graphify

コードと文書を横断する知識グラフを構築し、出典と関係を探索します。
公式 CLI を利用する SKILL とセットアップ手順を提供する、Beyond Labo の統合プラグインです。
上流の実行バイナリやソースは同梱していません。

## 導入

[導入ガイド](../install.html)に従ってマーケットプレイスを追加し、`graphify` をインストールします。

```bash
codex plugin add graphify@personal
```

新しいタスクで SKILL を使い、初回のみ[実行環境の準備](../skills/graphify.md)を進めてください。
プラグインの追加だけでは CLI はインストールされません。

## 構成

| 項目 | 内容 |
| --- | --- |
| プラグイン | `graphify` |
| バージョン | `0.1.0` |
| カテゴリ | `DeveloperTools` |
| SKILL | [Graphify](../skills/graphify.md) |
| MCP | 同梱なし（CLI 経由） |
| 上流の確認バージョン | `0.9.56` |

## 責務の境界

呼び出し元や変更影響のシンボル単位の調査には CodeGraph を使います。
説明用に構成を整理した図は Archify の役割です。
グラフ上の最短経路と、実行時の呼び出し経路は区別します。

3ツールの選定理由は[構成検討記録](../research/architecture-graph-tools.md)を参照してください。

## 利用条件と出典

Python 3.10 以上が必要です（検証環境は 3.12）。
配布パッケージ名は `graphifyy`、実行コマンド名は `graphify` です。
コード解析は認証不要です。
文書解析には、このタスクのアシスタント、または利用者が選んだ LLM バックエンドを使います。

初回インストールは PyPI とパッケージ配信先へ接続します。
解析対象と出力先を指定し、`graphify-out/` にグラフを書きます。
クラウド LLM を選ぶ場合は対象文書が送信されるため、既存のキーだけを根拠に自動実行しません。
Gemini を使う場合の資格情報名は `GEMINI_API_KEY` または `GOOGLE_API_KEY` です。
PDF は `pdf`、Office 文書は `office` の追加依存が必要です。

上流は [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)、上流のライセンス表記は Apache-2.0（同梱 LICENSE-MIT・NOTICE も参照） です。
統合プラグイン自体の利用条件は[リポジトリの利用条件](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/README.md)に従います。
上流のライセンスを、このリポジトリ全体へ適用するものではありません。
