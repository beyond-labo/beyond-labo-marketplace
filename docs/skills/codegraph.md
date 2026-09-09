# CodeGraph SKILL

ソースコードのシンボル、呼び出し関係、変更影響とテスト候補を調べます。

## いつ使うか

関数の呼び出し元、依存先、変更の波及範囲、確認すべきテスト候補を調べたいときに使います。

## 前提条件と初回準備

[CodeGraph プラグイン](../plugins/codegraph.md)を追加した後、対象ワークスペースで次を実行します。

対象は `colbymchenry/codegraph` です。
同名の別パッケージとの混同を避けるため、`@colbymchenry/codegraph@1.6.0` を指定します。
ソース側の Node.js 要件は 20 以上 25 未満で、公開 npm パッケージはプラットフォーム別の実行環境を含みます。
認証と API キーは不要です。

```bash
npm install --prefix .tools/codegraph @colbymchenry/codegraph@1.6.0
export PATH="$PWD/.tools/codegraph/node_modules/.bin:$PATH"
export CODEGRAPH_TELEMETRY=0
export DO_NOT_TRACK=1
codegraph --version
```

既存の実行環境がある場合は、バージョンと導入元を確認して再利用します。
`.tools/` は実行環境の置き場の例で、プラグインのキャッシュ内へ依存を追加する必要はありません。

## プロンプト例

```text
$codegraph を使い、このリポジトリの認証処理の呼び出し元と変更影響、確認すべきテストを調べてください。
```


## 入出力と責務

初回インストールは npm レジストリへ接続します。
解析はコードを読み、`.codegraph/` にインデックスを書きます。
上流の既定の匿名テレメトリーは、上記の環境変数で無効にします。
CLI のみの構成では常駐監視を行わないため、変更後は `codegraph sync <project>` で更新します。

文書を含む知識グラフは Graphify、説明用の図は Archify が担います。
静的解析は動的呼び出しなどを取りこぼすことがあるため、主要な結論は現行ソースで確かめます。
テスト候補の一覧だけで変更の安全性は保証できません。
リポジトリのテスト命名規則によっては、`affected` の既定フィルターから漏れます。
Python の `test_*.py` なら `codegraph affected <changed-file> --path <project> --filter 'test_*.py' --json` のように指定し、実際のテストファイルと突き合わせます。

上流のエージェント登録コマンドや hooks は自動追加しません。
実行方法の正本は [SKILL.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/codegraph/skills/codegraph/SKILL.md)、依存の固定値と詳細は[セットアップ参照](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/codegraph/skills/codegraph/references/setup.md)です。
