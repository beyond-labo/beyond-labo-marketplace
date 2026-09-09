# Archify

システム構成や処理の流れを、検証可能な JSON と単体 HTML の図にします。
公式 CLI を利用する SKILL とセットアップ手順を提供する、Beyond Labo の統合プラグインです。
上流の実行バイナリやソースは同梱していません。

## 導入

[導入ガイド](../install.html)に従ってマーケットプレイスを追加し、`archify` をインストールします。

```bash
codex plugin add archify@personal
```

新しいタスクで SKILL を使い、初回のみ[実行環境の準備](../skills/archify.md)を進めてください。
プラグインの追加だけでは CLI はインストールされません。

## 構成

| 項目 | 内容 |
| --- | --- |
| プラグイン | `archify` |
| バージョン | `0.1.0` |
| カテゴリ | `DeveloperTools` |
| SKILL | [Archify](../skills/archify.md) |
| MCP | 同梱なし（CLI 経由） |
| 上流の確認バージョン | `2.17.0-dev.1` |

## 責務の境界

設計方針の検討には System Architecture Design を使います。
Archify は図の入力仕様とレイアウトを検証しますが、実際のシステム構成の正しさを保証するものではありません。

3ツールの選定理由は[構成検討記録](../research/architecture-graph-tools.md)を参照してください。

## 利用条件と出典

Git と Node.js 18 以上が必要です。
上流の確認済み開発スナップショットを取得し、`doctor` が成功することを確認します。
通常の描画に npm install、認証、API キーは不要です。

初回取得は GitHub に接続します。
描画時はローカルの JSON を読み、指定先へ HTML を書きます。
上記の環境変数で任意の更新確認を無効にします。
日本語ラベルは記述できますが、固定のビューアー操作 UI は英語になります。

上流は [tt-a1i/archify](https://github.com/tt-a1i/archify)、上流のライセンス表記は MIT です。
統合プラグイン自体の利用条件は[リポジトリの利用条件](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/README.md)に従います。
上流のライセンスを、このリポジトリ全体へ適用するものではありません。
