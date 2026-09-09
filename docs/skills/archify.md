# Archify SKILL

システム構成や処理の流れを、検証可能な JSON と単体 HTML の図にします。

## いつ使うか

構成図、シーケンス図、処理フローなどを、共有できる HTML にしたいときに使います。

## 前提条件と初回準備

[Archify プラグイン](../plugins/archify.md)を追加した後、対象ワークスペースで次を実行します。

Git と Node.js 18 以上が必要です。
上流の確認済み開発スナップショットを取得し、`doctor` が成功することを確認します。
通常の描画に npm install、認証、API キーは不要です。

```bash
git clone https://github.com/tt-a1i/archify.git .tools/archify
git -C .tools/archify checkout --detach 10722002bb8777ecb639d93c49586fae4adf3ae4
export ARCHIFY_UPDATE_CHECK_DISABLED=1
node .tools/archify/archify/bin/archify.mjs doctor
```

既存の実行環境がある場合は、バージョンと導入元を確認して再利用します。
`.tools/` は実行環境の置き場の例で、プラグインのキャッシュ内へ依存を追加する必要はありません。

## プロンプト例

```text
$archify を使い、このリポジトリの主要コンポーネントとリクエスト経路を日本語の図にしてください。
```


## 入出力と責務

初回取得は GitHub に接続します。
描画時はローカルの JSON を読み、指定先へ HTML を書きます。
上記の環境変数で任意の更新確認を無効にします。
日本語ラベルは記述できますが、固定のビューアー操作 UI は英語になります。

設計方針の検討には System Architecture Design を使います。
Archify は図の入力仕様とレイアウトを検証しますが、実際のシステム構成の正しさを保証するものではありません。

上流のエージェント登録コマンドや hooks は自動追加しません。
実行方法の正本は [SKILL.md](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/archify/skills/archify/SKILL.md)、依存の固定値と詳細は[セットアップ参照](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/archify/skills/archify/references/setup.md)です。
