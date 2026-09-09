# Graphify SKILL

コードと文書を横断する知識グラフを構築し、出典と関係を探索します。

## いつ使うか

設計文書、コード、論文などの関係を横断して調べたいときや、既存の Graphify グラフへ質問したいときに使います。

## 前提条件と初回準備

[Graphify プラグイン](../plugins/graphify.md)を追加した後、対象ワークスペースで次を実行します。

Python 3.10 以上が必要です（検証環境は 3.12）。
配布パッケージ名は `graphifyy`、実行コマンド名は `graphify` です。
コード解析は認証不要です。
文書解析には、このタスクのアシスタント、または利用者が選んだ LLM バックエンドを使います。

```bash
python3 -m venv .tools/graphify
.tools/graphify/bin/python -m pip install graphifyy==0.9.56
.tools/graphify/bin/graphify --help
```

既存の実行環境がある場合は、バージョンと導入元を確認して再利用します。
`.tools/` は実行環境の置き場の例で、プラグインのキャッシュ内へ依存を追加する必要はありません。
Windows では仮想環境の `Scripts` 配下の実行ファイルを使います。

## プロンプト例

```text
$graphify を使い、src と docs の関係を知識グラフにしてください。外部 API は使わず、このタスク内で文書を分析してください。
```

コードだけを解析する例：

```bash
.tools/graphify/bin/graphify extract <project> --code-only --no-cluster --max-workers 1
.tools/graphify/bin/graphify query "認証処理" --graph <project>/graphify-out/graph.json
```

この例では文書を解析せず、HTML やレポートもまだ生成しません。
HTML とレポートが必要なら `cluster-only <project> --no-label` を実行します。
文書解析のバックエンド設定と、このタスク内で解析する方法は[セットアップ詳細](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/graphify/skills/graphify/references/setup.md)にあります。

## 入出力と責務

初回インストールは PyPI とパッケージ配信先へ接続します。
解析対象と出力先を指定し、`graphify-out/` にグラフを書きます。
クラウド LLM を選ぶ場合は対象文書が送信されるため、既存のキーだけを根拠に自動実行しません。
Gemini を使う場合の資格情報名は `GEMINI_API_KEY` または `GOOGLE_API_KEY` です。
PDF は `pdf`、Office 文書は `office` の追加依存が必要です。

呼び出し元や変更影響のシンボル単位の調査には CodeGraph を使います。
説明用に構成を整理した図は Archify の役割です。
グラフ上の最短経路と、実行時の呼び出し経路は区別します。

上流のエージェント登録コマンドや hooks は自動追加しません。
実行方法の正本は [SKILL.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/graphify/skills/graphify/SKILL.md)、依存の固定値と詳細は[セットアップ参照](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/graphify/skills/graphify/references/setup.md)です。
