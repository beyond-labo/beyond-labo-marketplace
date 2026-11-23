# Unslop SKILL

既存画面を監査し、製品の機能と個性を保ちながら、余白、色、文言、文字、レイアウトを改善します。

## いつ使うか

「AI が作ったような見た目を直したい」「この画面を仕上げたい」と依頼するときに使います。
局所的な問題は局所的に直し、問題がなければ無理にリデザインしません。
新機能の設計や、表示を変えない状態管理の整理は別の設計作業として扱います。

## 前提条件

[Unslop プラグイン](../plugins/unslop.md)を追加し、新しいチャットで `$unslop` を指定します。
対象画面のコード、表示を確認する環境、既存の仕様やデザイントークンを参照できる状態にします。
画像しかない場合の監査では、問題点と改善案を返します。
再構築や実装まで依頼された場合は、Web の画像から静的 HTML、iOS の画像から指定のネイティブ技術で画面を再現します。
Web の URL だけなら保存した HTML を改善できます。
保存した HTML の変更で元サイトが更新されることはありません。

## Web のプロンプト例

```text
$unslop を使い、設定画面を監査して見た目を改善してください。
既存のコンポーネント、ブランド、機能、文言の意味を保ち、表示と操作を確認するところまで進めてください。
```

```text
$unslop でこのダッシュボードを監査してください。
今回は問題点と改善方針の提示までとし、コードは変更しないでください。
```

Web 用の保存や動画機能を使うときだけ、対象プロジェクトへ必要な依存を準備します。
同梱スクリプトの使い方は [Web 実行ガイド](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/unslop/skills/unslop/references/web-runtime.md) にあります。
通常の改善には Node.js の追加依存を要求しません。

## iOS のプロンプト例

```text
$unslop を使い、SwiftUI のプロフィール画面を監査して改善してください。
既存の機能と状態管理を保ち、Dynamic Type、SF Symbols、標準コントロールを優先してください。
利用できる XcodeBuildMCP で表示と操作を確認し、実施できなかった条件も報告してください。
```

```text
$unslop を使い、この iOS 画面の余白と文字の階層を整えてください。
既存の Liquid Glass と最低対応 OS を保ち、Light、Dark、大きい文字で確認するところまで任せます。
```

## iOS の適用手順

1. 対象画面の仕様、最低対応 OS、View とデータ、既存のデザイントークンを確認します。
2. 可能なら変更前の Simulator 画面を取得し、問題箇所を監査します。
3. 製品の方針を短く示し、許可された範囲でネイティブ UI を改善します。
4. 同じ画面条件で前後を比較し、関係する操作、build とテストを確認します。
5. 変更内容と検証結果、未実施の確認を報告します。

iOS 用の手順は、Web の px 値、Web フォント、Lucide、装飾禁止規則より優先します。
Dynamic Type、semantic color、SF Symbols、safe area、標準コントロールとシステムの material を使い、最低対応 OS を無断で上げません。
実装判断の詳細は [iOS 適用手順](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/unslop/skills/unslop/references/ios.md) が正本です。

## 確認する条件

| 条件 | 確認内容 |
| --- | --- |
| 標準と大きい文字 | 重要な情報と操作が欠けないか |
| Light、Dark、小さい対応端末 | 表示の崩れとコントラスト |
| VoiceOver | ラベル、読み上げ順、操作と状態。画像だけでは確認できません。 |
| 動きと透明度の設定 | Reduce Motion、必要なら Reduce Transparency と Increase Contrast |
| 操作と状態 | 入力、遷移、関係する loading、empty、error、disabled |
| build とテスト | プロジェクトが指定する検証と影響範囲の回帰確認 |

このプラグインの導入だけで XcodeBuildMCP や SwiftUI 関連スキルは追加されません。
実行できない環境ではコードの監査を進め、未実施の表示確認を明記します。

## 帰属とライセンス

Based on [unslop](https://github.com/heydamir/unslop) by **Damir Sokolovsky** ([@heydamir](https://x.com/heydamir))。
Beyond Labo が Codex 向けの導線と iOS 適用手順を追加しました。
このガイドとプラグイン全体は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で配布します。
帰属、改変表示、ライセンス全文と免責への参照は [NOTICE.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/unslop/NOTICE.md) にあります。
上流のスキルと画像をコピーするときも、これらの表示を保持してください。
