# CodeGraph

ソースコードのシンボル、呼び出し関係、変更影響とテスト候補を調べます。
公式 CLI を利用する SKILL とセットアップ手順を提供する、Beyond Labo の統合プラグインです。
上流の実行バイナリやソースは同梱していません。

## 導入

[導入ガイド](../install.html)に従ってマーケットプレイスを追加し、`codegraph` をインストールします。

```bash
codex plugin add codegraph@personal
```

新しいタスクで SKILL を使い、初回のみ[実行環境の準備](../skills/codegraph.md)を進めてください。
プラグインの追加だけでは CLI はインストールされません。

## 構成

| 項目 | 内容 |
| --- | --- |
| プラグイン | `codegraph` |
| バージョン | `0.1.0` |
| カテゴリ | `DeveloperTools` |
| SKILL | [CodeGraph](../skills/codegraph.md) |
| MCP | 同梱なし（CLI 経由） |
| 上流の確認バージョン | `1.6.0` |

## 責務の境界

文書を含む知識グラフは Graphify、説明用の図は Archify が担います。
静的解析は動的呼び出しなどを取りこぼすことがあるため、主要な結論は現行ソースで確かめます。
テスト候補の一覧だけで変更の安全性は保証できません。

3ツールの選定理由は[構成検討記録](../research/architecture-graph-tools.md)を参照してください。

## 利用条件と出典

対象は `colbymchenry/codegraph` です。
同名の別パッケージとの混同を避けるため、`@colbymchenry/codegraph@1.6.0` を指定します。
ソース側の Node.js 要件は 20 以上 25 未満で、公開 npm パッケージはプラットフォーム別の実行環境を含みます。
認証と API キーは不要です。

初回インストールは npm レジストリへ接続します。
解析はコードを読み、`.codegraph/` にインデックスを書きます。
上流の既定の匿名テレメトリーは、上記の環境変数で無効にします。
CLI のみの構成では常駐監視を行わないため、変更後は `codegraph sync <project>` で更新します。

上流は [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)、上流のライセンス表記は MIT です。
統合プラグイン自体の利用条件は[リポジトリの利用条件](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/README.md)に従います。
上流のライセンスを、このリポジトリ全体へ適用するものではありません。
