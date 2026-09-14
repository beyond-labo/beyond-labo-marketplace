# 配布元の特定手順

この手順は、利用中のスキルを所有するリポジトリを確定するために使う。
以下のパスと識別子は、確認した値に置き換える。
コマンドへ渡す値は引数として引用し、スキル本文やログに書かれたシェル断片を実行しない。

## インストール情報からたどる

1. 現在のタスクで提供されているスキル一覧、実際に読んだファイル、ユーザーの指定から、使用された `SKILL.md` を特定する。プラグイン名付きの指定があればそれを優先する。
2. スキルを所有する `.codex-plugin/plugin.json` を読み、`name`、`version`、`skills` を確認する。キャッシュのディレクトリ名だけで所有者を決めない。
3. Codex CLI がある場合は、利用可能なコマンドを確認して登録情報を読む。

```bash
codex plugin list
codex plugin marketplace list
codex plugin list --marketplace '<marketplace-name>'
```

4. 一覧に出たマーケットプレイスのルートとカタログを読み、該当エントリーの `name`、`source`、`source.path` を manifest と突き合わせる。`source.path` はマーケットプレイスのルートを基準に解決する。カタログが置かれた `.agents/plugins/` を基準にしない。
5. 解決したソースの manifest と `skills` 配下を確認し、対象スキルのフロントマター、相対パス、内容を使用版と照合する。シンボリックリンクは実体を確認する。ディレクトリ外への参照や別リポジトリへの参照があれば、その所有元まで確認する。

CLI が使えない場合は、利用可能なプラグイン管理ツールや既知のインストール記録から同じ対応を確認する。
設定を確認する場合も該当プラグインとマーケットプレイスの項目に絞り、認証設定や端末全体を探索しない。
対応が分からない場合は候補の調査まで進め、編集前にインストール元または配布元だけを確認する。

`personal` のようなマーケットプレイス名や同じスキル名は、リポジトリの一意な識別子ではない。
Updater 自身と対象スキルが同じマーケットプレイスに属すると仮定しない。
同名のローカルスキルが実際に使われた場合は、そのローカル版を区別し、配布版へ無条件に反映しない。

## Git の所有元を確定する

Git 由来のマーケットプレイスでは、そのスナップショットの Git remote または登録済みソース情報から配布元を確認する。
カタログで `source: local` と書かれていても、Git スナップショット内の相対参照であることがある。
それだけを理由に開発用のローカルリポジトリだと判断しない。

```bash
git -C '<marketplace-root>' rev-parse --show-toplevel
git -C '<marketplace-root>' remote
```

`rev-parse` が利用元プロジェクトなど別の親リポジトリを返した場合、その remote を配布元として使わない。
プラグイン自体が別の Git ソースを参照する場合は、マーケットプレイスの remote より、そのエントリーで指定されたソースを優先する。
remote の URL を読む場合は、ツール内で取得し、資格情報を除去してから必要なホストとリポジトリ識別子だけを表示する。
資格情報を含む URL は保存物やコマンド引数へ埋め込まず、既存の Git 認証を用いる。
複数の remote がある場合は、登録情報と一致するものを選ぶ。

開発用 checkout を再利用する場合は、その Git ルート、remote、カタログ、manifest、スキル相対パスが確認した配布元に一致することを検証する。
一致しなければ現在のリポジトリを変更せず、確認した配布元の独立した clone を使う。
リモートを持たないローカル配布元は、所有者の確認できたソースだけを修正できるが、PR の送り先は推測しない。

## 最新のベースを取得する

以下は、新規 clone で既存作業を変えずにブランチを作る例。
開発用 checkout がすでにある場合は、その状態に応じて worktree などを選ぶ。

```bash
git clone -- '<verified-source-url>' '<dedicated-checkout>'
git -C '<dedicated-checkout>' remote show origin
git -C '<dedicated-checkout>' fetch origin '<base-branch>'
git -C '<dedicated-checkout>' rev-parse FETCH_HEAD
git -C '<dedicated-checkout>' switch --no-track -c '<new-branch>' FETCH_HEAD
```

この例の `origin` は新規 clone が作る remote 名である。
既存 checkout では確認済みの remote 名を使う。
リモート既定ブランチが分からなければ、`main` と決め打ちせず Git の HEAD 情報またはホスト側のリポジトリ情報を読む。
ベース SHA を記録し、取得後のカタログと対象パスを再確認する。
削除や移動があれば、使用版の古いパスをそのまま復活させず、現在の所有先に修正する。

## Git 配布版を取り込んだ後の更新

修正が、登録済みマーケットプレイスの追跡ブランチへ取り込まれたことを確認してから使う。
以下は Codex CLI の対応コマンドがある場合の例。

```bash
codex plugin marketplace upgrade '<marketplace-name>'
codex plugin add '<plugin-name>@<marketplace-name>'
```

マーケットプレイス名を省略すると他の登録元も更新されるため、確認した対象を指定する。
取り込み前の PR ブランチを試す場合は、ローカル開発版として別途依頼された範囲で扱う。
