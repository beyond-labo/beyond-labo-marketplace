# kiro-steering

.kiro の仕様駆動開発で、コードと決定の根拠をもとに、プロジェクト方針を作成または更新する。古い方針の置換と関連仕様への影響確認を含む。

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
$kiro-steering 現行コードと決定に基づき、古い技術方針を更新してください。
```

例の `notifications` は対象の feature 名へ置き換えます。
レビュー合格と工程承認、仕様の同期と実装完了は別々に扱います。
読取専用の依頼では本文・承認・索引を書き換えません。

## 正本

[SKILL.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-steering/SKILL.md)
