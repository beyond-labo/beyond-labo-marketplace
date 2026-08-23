# Codex アプリから追加する

このガイドでは、GitHub 上の Beyond Labo Marketplace を Codex アプリへ追加し、プラグインを利用できる状態にします。

## 追加前に確認すること

Codex アプリへサインインし、インターネットへ接続できる状態にします。

## プラグイン画面を開く

Codex アプリの左側メニューから「プラグイン」を選択します。

![Codex の左側メニューにある「プラグイン」](/beyond-labo-marketplace/assets/install/open-plugins.png)

## マーケットプレイスを追加する

画面右上の「追加」を開き、「マーケットプレイスを追加」を選択します。

![「追加」メニューから「マーケットプレイスを追加」を選択する](/beyond-labo-marketplace/assets/install/add-marketplace.png)

## リポジトリを指定する

マーケットプレイスの追加画面には、次の値を入力します。

- **ソース**：`https://github.com/beyond-labo/beyond-labo-marketplace.git`
- **Git ref**：`main`
- **スパースパス**：空欄

SSH の設定を済ませている場合は、ソースに SSH URL を指定してもかまいません。

入力後に「マーケットプレイスを追加」を選択します。

画像は SSH URL を指定した例です。

SSH 認証を設定していない場合は、上記の HTTPS URL を入力します。

![ソースと Git ref を入力する画面](/beyond-labo-marketplace/assets/install/configure-marketplace.png)

## プラグインを追加する

プラグイン画面の「個人用」タブを選択します。

![「個人用」タブを選択する](/beyond-labo-marketplace/assets/install/select-personal-marketplace.png)

追加したマーケットプレイスから、使いたいプラグインを選び、「追加」または「インストール」を実行します。

現在は、次のプラグインを公開しています。

- `system-architecture-design`
- `git-gh-authentication`
- `communication-writing`

追加した SKILL を利用する前に、新しいタスクを開始します。

## うまく表示されないとき

「Git ref」が `main` になっていることを確認します。

プラグインが一覧に出ない場合は、マーケットプレイスを更新してから、もう一度一覧を開きます。

GitHub へ接続できない場合は、ネットワーク接続と指定した URL を確認します。

SSH URL で失敗する場合は、HTTPS URL を指定するか、GitHub の SSH 認証を設定します。
