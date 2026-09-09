# kiro-review

.kiro の仕様駆動開発で、実装差分を現行の承認済み仕様・責務境界・検証証拠に照らしてレビューする。実装後、修正後、タスク受け入れ時に使う。

## いつ使うか

このスキルは OKF + SDD の `.kiro` ワークフローで使います。
既存仕様に関係しない小修正は直接実施でき、すべての工程を通す必要はありません。

## 前提条件

`okf-sdd` v0.1.0 をマーケットプレイスから導入してください。
対象プロジェクトの関連文書、変更根拠、既存の承認範囲を確認します。
仕様がない段階では存在しない承認や完了状態を推測しません。
検査 CLI を使う場合は Python 3.10 以上と PyYAML 6.0.3 が必要です。
設定の準備と更新は [プラグインの導入手順](../plugins/okf-sdd.md) を参照してください。

## プロンプト例

```text
$kiro-review notifications 今回の実装差分を、現行仕様と検証証拠に照らして読み取り専用でレビューしてください。
```

例の `notifications` は対象の feature 名へ置き換えます。
レビュー合格と工程承認、仕様の同期と実装完了は別々に扱います。
読取専用の依頼では本文・承認・索引を書き換えません。

## 正本

[SKILL.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-review/SKILL.md)
