# iOS の画面を改善する手順

この手順は Beyond Labo による unslop の適用拡張である。
iOS では、この文書を Web 向けの pass、固定 px 値、フォント、Lucide、装飾禁止規則、チェックリストより優先する。
共通の目的は、機能と製品の個性を保ち、表示の階層と一貫性を改善することにある。

## 対象画面と契約の確認

対象リポジトリの `AGENTS.md`、関連する画面仕様、既存のデザイントークンを読む。
対応 OS、SwiftUI または UIKit、対象画面、表示データ、遷移、入力、エラー時の復帰を確認する。
見た目の改善のために公開 API、業務ルール、状態の所有者、TCA Reducer の振る舞いを変更しない。
意味を持つラベルや状態表示を装飾と誤認して削除しない。

実際の View と関連コンポーネントを特定し、可能なら変更前の画面を取得する。
XcodeBuildMCP が利用できる環境では、プロジェクトと scheme、利用可能な Simulator を調べ、対象を選んで build、起動、画面操作、スクリーンショット取得を行う。
scheme や端末名を推測して固定しない。
XcodeBuildMCP の機能が足りない場合だけ、制約を説明してプロジェクト指定の CLI 手順で補う。
実行環境が使えない場合もコード上の監査は進められるが、表示確認を未実施と明記する。

iOS のスクリーンショットだけが入力なら、指摘と改善案を返す。
コードの再構築まで依頼された場合は SwiftUI など指定のネイティブ技術で作り、元アプリへの実装済みと混同しない。
HTML の再現や Web 用 snapshot/story スクリプトを iOS の検証として扱わない。

## 監査から実装まで

1. 余白と整列、情報の優先順位、色の意味、文字、アイコン、操作と状態を監査し、画面上の位置と問題を対応付ける。
2. 既存のブランドと標準 UI を基準に、局所的な修正で足りるか判断する。問題がなければ、そのまま報告する。
3. 製品、性格、製品に結び付く世界観、強調する内容、固有の細部の五点で方針を短く示す。フォームや設定画面に装飾的な見せ場を強制しない。
4. 監査のみの依頼なら、ここで結果を返す。改善まで許可されていれば範囲内で進め、機能やブランドを変える未決事項だけ確認する。
5. 余白、色、アイコン、文言、文字、レイアウト、細部、画像、動きの順を目安に修正する。既存のコンポーネントとトークンで揃え、不要な変更は加えない。

## ネイティブ UI の判断基準

| 対象 | iOS で優先するもの |
| --- | --- |
| 余白と寸法 | 既存の pt トークン、標準の配置、safe area。Web の 4px グリッドや 32px の行高を強制しない。文字拡大時にも操作領域を保つ。 |
| 文字 | `.body`、`.headline` などの意味を持つ text style と Dynamic Type。既存のカスタムフォントも拡大に追従させ、固定サイズや行数制限で重要な文字を切らない。Web の weight 上限や italic 禁止を移植しない。 |
| 色 | `.primary`、`.secondary`、既存の semantic color と Asset の外観別定義。選択、エラー、警告を色だけに依存させない。 |
| アイコン | 既存の SF Symbols と隣接文字に合うサイズ、weight。意味を持つ絵文字は一律削除せず、操作アイコンとの役割を確認する。 |
| コントロール | 標準の Button、List、Form、Toggle、sheet、toolbar を活用し、押下、無効、選択、フォーカスを区別できる状態にする。見た目を揃えるために標準操作を自作し直さない。 |
| レイアウト | 内容に応じた高さ、文字の折り返し、小さい端末、キーボード、横向きや iPad 対応の既存方針。iPhone 画面へ Web の hero や sidebar 幅を持ち込まない。 |
| 文言 | 既存のローカライズ経路、日本語の意味、確認理由と状態の明確さ。意味を変える短縮や固定の英語化をしない。 |
| 動き | 状態や操作の意味を伝える標準の遷移と Reduce Motion。標準アニメーションを一律削除せず、不要な繰り返しを減らす。 |

Liquid Glass が使われている画面では、システムのナビゲーションと操作用 material を保持する。
上流の「glass に置き換えない」という Web 向けの規則を、標準 material の削除理由にしない。
独自の glass を内容カード全体へ増やすことも避ける。
新しい API を追加する必要がある場合は、対象 OS の availability と既存のフォールバックを確認し、最低対応 OS を無断で上げない。

利用環境に SwiftUI UI Patterns、Liquid Glass、View Refactor の専門スキルがある場合は、対象の判断に必要なものだけ併用する。
unslop は画面の監査と改善方針を担当し、状態管理やアーキテクチャの整理だけを目的に起動しない。
専門スキルや MCP がインストールされていると仮定せず、未導入でも使える基準をこの文書に保持する。

## 受け入れ条件と確認記録

表示に影響する変更では、同じ画面、同じデータ、同じ端末条件で変更前後を比較する。
対象に応じて次を確認し、未確認の条件を報告する。

- 標準の文字サイズとアクセシビリティ用の大きい文字で、主要な情報と操作が欠けない。
- Light と Dark、小さい対応端末で表示とコントラストを確認する。
- VoiceOver のラベル、読み上げ順、操作名と状態を確認する。画像だけで確認済みとしない。
- Reduce Motion、必要なら Reduce Transparency と Increase Contrast を確認する。
- 変更した操作、入力、遷移、loading、empty、error、disabled のうち関係する状態を確認する。
- 既存の build と影響範囲のテストを実施する。標準の UI 確認と自動テストの結果を区別する。

完了報告には、監査結果、方針、変更したファイル、比較した画面条件、build/test 結果、未実施の確認を含める。
スクリーンショット、コードレビュー、Simulator 上の手動操作だけでアクセシビリティ全体や実機動作を保証しない。
生成画像や紹介動画は別途依頼された場合の成果物とし、画面改善の必須条件にしない。

## 参照する一次資料

- [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)：支援技術と動きへの配慮。
- [Apple HIG: Typography](https://developer.apple.com/design/human-interface-guidelines/typography)：text style、Dynamic Type、文字の階層。
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)：標準コンポーネントと外観設定の確認。

2026-11-23 に確認した一次資料をもとに Beyond Labo が作成した。
unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)) の適用拡張。
この文書は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) で配布する。
帰属と改変表示は [NOTICE.md](../../../NOTICE.md) を参照。
