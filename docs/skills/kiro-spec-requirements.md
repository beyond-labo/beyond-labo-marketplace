# kiro-spec-requirements

.kiro の機能仕様の要件と受け入れ条件を生成・更新する。一般的な文章推敲には使わない。

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
$kiro-spec-requirements notifications 通知を無効にした場合の受け入れ条件を具体化してください。
```

例の `notifications` は対象の feature 名へ置き換えます。
レビュー合格と工程承認、仕様の同期と実装完了は別々に扱います。
読取専用の依頼では本文・承認・索引を書き換えません。

## 正本

[SKILL.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-spec-requirements/SKILL.md)
