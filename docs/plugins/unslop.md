# Unslop

Web と iOS の UI を監査し、製品らしい見た目へ整えます。
Damir Sokolovsky の [unslop](https://github.com/heydamir/unslop) を取り込み、Beyond Labo が Codex 向けの導線と iOS の適用手順を追加した配布版です。

## 導入

[導入ガイド](../install.html)に従ってマーケットプレイスを追加し、`unslop` をインストールします。

```bash
codex plugin add unslop@personal
```

新しいチャットで `$unslop` を呼び出してください。
この配布版は明示呼び出し専用です。
画面実装後の監査と仕上げを任せるときに指定します。

## 構成と前提条件

| 項目 | 内容 |
| --- | --- |
| プラグイン | `unslop` |
| バージョン | `0.1.0` |
| カテゴリ | `DeveloperTools` |
| SKILL | [Unslop](../skills/unslop.md) |
| 上流の固定コミット | [`620163e`](https://github.com/heydamir/unslop/tree/620163eedb3529d9cd23a3994ed8d287d06f760d) |
| 同梱物 | スキル、参照資料と画像、Web 用スクリプト、examples、上流テスト、ライセンスと帰属情報 |
| MCP と認証 | MCP は同梱しません。スキル利用に専用認証は不要です。 |

通常の改善には、対象画面のコードとそのプロジェクトの実行環境を使います。
Web の保存機能には Node.js、Playwright と Chromium、紹介動画には追加で ffmpeg が必要です。
iOS の実行確認には Xcode と対応する Simulator を使い、利用可能なら XcodeBuildMCP を優先します。
これらのツールと専門スキルはプラグインに同梱しません。

## 開発フローへの組み込み

1. 製品仕様と既存のデザインシステムに沿って画面を実装します。
2. `$unslop` で対象画面を監査し、改善方針を確認します。
3. 許可した範囲の改善を進め、同じ画面条件で表示と操作を比較します。

監査だけの依頼ではコードを変更しません。
改善まで依頼している場合は、通常の実装判断ごとに確認を繰り返さず進めます。
新機能やブランド変更など、範囲を変える判断が必要なら確認します。

iOS では Web の固定寸法や装飾禁止を適用せず、標準 UI、Dynamic Type、SF Symbols、アクセシビリティを優先します。
システムの Liquid Glass は保持し、独自の装飾を増やすことも避けます。
適用例と確認条件は [SKILL ガイド](../skills/unslop.md)を参照してください。

## 責務の境界

unslop は既存画面の監査と表示の改善を扱います。
機能仕様、API、状態管理の責務、遷移の意味を変える判断は、製品側の設計と承認に従います。
SwiftUI の構成や material の具体的な実装には、利用環境にある関連スキルを必要に応じて併用します。
公開や画像生成サービスの契約は、画面改善の許可に含めません。

## 更新とライセンス

上流の特定コミットを取り込み、差分をレビューして更新します。
更新の正本は [UPSTREAM.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/unslop/UPSTREAM.md) です。
配布ブランチへの取り込み後、マーケットプレイスとインストール済み版を更新し、新しいチャットで利用します。

unslop の作者は **Damir Sokolovsky** ([@heydamir](https://x.com/heydamir)) です。
このプラグイン全体とこのガイドは、Beyond Labo の追加と改変を含め [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で配布します。
上流の公式配布版や作者の推奨を表すものではありません。
コピーや改変を配布するときは、作者、上流リンク、ライセンス、変更表示を保持してください。
全文と免責は [LICENSE](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/unslop/LICENSE)、帰属と変更の範囲は [NOTICE.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/unslop/NOTICE.md) にあります。
