# Web の任意スクリプト

通常の UI 改善は、利用プロジェクトのコードと既存の実行環境で行う。
同梱スクリプトは、URL だけの入力から HTML を保存するときや、依頼された紹介動画を作るときに使う。
iOS アプリの実行や表示確認には使わない。

## 実行環境

スクリプトには Node.js が必要である。
Playwright と Chromium は対象プロジェクトの既存環境を優先し、不足している場合だけ、そのプロジェクトのパッケージ管理方法で準備する。
インストール済みプラグインのキャッシュへ依存を書き込まない。

```bash
npm install -D playwright
npx playwright install chromium
```

動画の出力には `ffmpeg` が PATH 上に必要である。
macOS の Homebrew を使う環境では次が導入例となる。

```bash
brew install ffmpeg
```

これらの依存、ブラウザー、画像生成サービス、MCP 接続はプラグインに同梱せず、自動導入もしない。
ブラウザーや ffmpeg がない場合は必要な準備を示し、コードの監査など実行できる範囲を進める。

## コマンド

以下の `<skill-folder>` を、現在読み込んでいる `SKILL.md` のディレクトリに置き換える。
スクリプトは作業ディレクトリの `package.json` を基準に Playwright を解決できるため、依存を用意したプロジェクトから実行する。
出力には用途ごとの新しいディレクトリを選び、元ファイルを上書きしない。

```bash
node <skill-folder>/scripts/snapshot.mjs https://example.com unslop/original.html --light
node <skill-folder>/scripts/snapshot.mjs ./page.html unslop/original.html --width 800 --height 600
node <skill-folder>/scripts/story.mjs unslop-story/story.html unslop-story.mp4
```

`snapshot.mjs` は指定ページをスクロールして、HTML、インライン化できる画像と CSS、`original.live.png` を保存する。
ページと関連リソースの取得はネットワークへ接続する。
ログイン済みブラウザーの認証を引き継ぐツールではなく、利用権限のあるページだけを対象にする。
元ページの JavaScript 動作や canvas の完全保存は保証されないため、保存した表示をライブの画像と比較する。
作成した HTML だけで元サイトが更新されたとは報告しない。

`story.mjs` の入力には `SKILL.md` の Story video 節にある meta tag と CSS の段階表現が必要である。
ブラウザーとローカル HTTP サーバーで描画し、ffmpeg で動画を書き出す。
動画の作者クレジットを保持し、動画を製品コードの代わりにしない。
Web ページの保存物、画像、フォントにはそれぞれの利用条件があるため、取得できたことを再配布の許可と混同しない。

## 配布版の確認

マーケットプレイスのリポジトリルートから、同梱した上流テストを実行できる。

```bash
node --test plugins/unslop/test/story-path.test.mjs
node --test plugins/unslop/test/snapshot.test.mjs
node --test plugins/unslop/test/story.test.mjs
```

snapshot のブラウザーテストは依存がない環境では skip する。
story のテストは ffmpeg を前提とする。事前に `ffmpeg -version` を確認する。
story の meta 解析テスト成功だけで MP4 の生成成功とは扱わず、動画機能を確認するときは実際に短い動画を書き出し、フレームとクレジットを確認する。

Beyond Labo が unslop の Codex 向け実行案内として追加した文書。
unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir))、[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
帰属と変更表示は [NOTICE.md](../../../NOTICE.md) を参照。
