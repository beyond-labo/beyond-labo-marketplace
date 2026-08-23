# 対話・コミュニケーション

`communication-writing` は、日本語の技術文書と読み物としての説明文を推敲するプラグインです。

| 項目 | 内容 |
| --- | --- |
| バージョン | `0.1.0` |
| カテゴリ | Productivity |
| 認証 | 不要 |

## 導入

リポジトリのルートで次を実行します。

```bash
codex plugin marketplace add .
codex plugin add communication-writing@personal
```

## 含まれる SKILL

- [japanese-tech-writing](../skills/japanese-tech-writing.md)：技術文書の構成、論証、用語、冗長さを点検します。
- [cognitive-rhythm-writing](../skills/cognitive-rhythm-writing.md)：説明文の観察、逡巡、断定、再観察の切り替えを設計します。

技術的な正確さや構造を整える作業には前者を使います。

正しいが単調な説明文に推進力を与える作業には後者を使います。

両方が必要な文章では、`japanese-tech-writing` で論証と表記を整えてから、`cognitive-rhythm-writing` で文章の緩急を点検します。
