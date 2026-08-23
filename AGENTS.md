# Beyond Labo Marketplace 運用規約

このリポジトリは Beyond Labo の Codex プラグインと SKILL を配布し、GitHub Pages で利用方法を公開する。
変更は、インストール可能なプラグイン、カタログ、公開ドキュメントの整合を保つこと。

## ディレクトリと正本

```text
.
├── .agents/plugins/marketplace.json  # Codex に読み込ませるプラグイン・カタログの正本
├── plugins/<plugin-name>/            # プラグイン本体
│   ├── .codex-plugin/plugin.json     # プラグインのメタデータの正本
│   ├── .mcp.json                      # MCP を提供する場合だけ作成する接続設定
│   └── skills/<skill-name>/SKILL.md  # SKILL 本体
└── docs/                             # GitHub Pages として公開する静的サイト
    ├── index.html                    # 公開トップページの正本
    └── assets/site.css               # 公開ページ共通のスタイル
```

- プラグイン名とフォルダ名、`.codex-plugin/plugin.json` の `name` は、64 文字以内の kebab-case で一致させる。
- SKILL 名とフォルダ名は kebab-case で一致させる。SKILL は必ず `SKILL.md` を持ち、フロントマターは `name` と `description` のみとする。
- 新規プラグインは `plugins/<plugin-name>` に作成し、`.agents/plugins/marketplace.json` には `./plugins/<plugin-name>` を登録する。`marketplace.json` は手編集せず、`plugin-creator` の scaffold コマンドで更新する。
- `marketplace.json` の `plugins` 配列は表示順である。既存順を変更しない。新規エントリーは末尾へ追加する。
- 各カタログエントリーには `policy.installation`、`policy.authentication`、`category` を必ず記載する。明示的な指定がなければ `AVAILABLE`、`ON_INSTALL` を使う。

## パスと秘密情報の保護

- リポジトリ、プラグイン manifest、SKILL、公開サイト、コミットメッセージに、利用者または開発者の実名、ユーザー名、メールアドレス、端末名、ホームディレクトリなど、端末固有の情報を含めない。
- ユーザー固有の絶対パスを記載しない。リポジトリ内のファイルはリポジトリルートからの相対パス、Codex の共通領域は `$CODEX_HOME`、ホームディレクトリは `~` で表す。
- ドキュメント中のコマンドは、どの開発者の環境でも読めるプレースホルダー（`<plugin-name>` など）と相対パスを使う。
- API キー、アクセストークン、Cookie、SSH 秘密鍵、接続文字列、実在する組織・個人用 URL をコミットしない。例示には値を入れず、環境変数名だけを示す。

## 新規 Plugin / SKILL の作成と責務整理

新規作成、機能追加、または SKILL の変更のたびに、実装前に `plugins/` 配下を確認し、次を判定する。

1. 既存プラグインまたは SKILL で同じ仕事を担えるか。
2. 既存 SKILL の説明、トリガー、入力・出力と重複または矛盾しないか。
3. 共通の手順・参照資料をどこが所有すべきか。

判定に応じて、次を実施する。

- 既存 SKILL の責務に収まる場合は、新規 SKILL を作らず既存 SKILL を拡張する。
- 一部だけ重なる場合は、各 SKILL の `description` を相互排他的なトリガーになるよう修正し、共通の詳細は一つの参照ファイルへ移す。
- 互いに独立して導入・更新できる機能だけを別プラグインにする。単なる説明量の増加を別プラグインの理由にしない。
- 互換性を壊す移動・統合・削除は、影響を README と Pages に反映し、既存利用者への移行手順を示す。

SKILL を新規作成するときは `skill-creator` の `init_skill.py` を使用し、必要な `agents/openai.yaml` を生成する。各 `SKILL.md` の変更後は、次を実行する。

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" \
  plugins/<plugin-name>/skills/<skill-name>
```

プラグインを新規作成するときは `plugin-creator` の `create_basic_plugin.py` で、リポジトリ内の `plugins/` と `.agents/plugins/marketplace.json` を指定する。作成・変更後は次を実行する。

```bash
python3 "$CODEX_HOME/skills/.system/plugin-creator/scripts/validate_plugin.py" \
  plugins/<plugin-name>
```

既存プラグインのローカル開発版を更新するときは、`marketplace.json` を直接変更しない。`update_plugin_cachebuster.py` を実行し、確認済みのローカル・マーケットプレイスから再インストールする。

## MCP を含むプラグイン

MCP は外部サービスまたはローカルプロセスとの接続がプラグインの明確な責務である場合だけ追加する。SKILL の説明や簡単なファイル操作のためだけに MCP を増やさない。

- 接続設定を置く場合は `plugins/<plugin-name>/.mcp.json` を作り、同じ変更で manifest の `mcpServers` を `./.mcp.json` に設定する。MCP を含めないプラグインでは、このフィールドを manifest に書かない。
- MCP 設定には秘密値を直接書かず、必要な資格情報は環境変数で参照する。環境変数名、認証の準備手順、最小権限の要件を SKILL と Pages に説明する。
- MCP のサーバー名、提供ツール、必要な権限、ネットワーク先を明記する。ユーザーの許可なく書き込み、削除、送信を行うツールは追加しない。
- `.mcp.json` の接続スキーマは MCP の提供元が定める公式仕様に従う。この規約には特定サービス固有の設定例や資格情報の詳細を重複して持ち込まない。
- manifest、`.mcp.json`、SKILL、Pages の記載を同一変更で更新し、実際に認証なしの状態と必要な認証後の状態を確認する。

## カタログの更新方法

カタログの正本は `.agents/plugins/marketplace.json`、各プラグインの説明の正本はその `.codex-plugin/plugin.json`、各 SKILL の説明の正本は `SKILL.md` とする。

- 新規・削除・改名・カテゴリ変更は、プラグイン本体、`marketplace.json`、紹介サイトを同じ変更で更新する。
- `marketplace.json` の `source.path`、プラグインの `name`、フォルダ名の不一致を残さない。
- カタログに未登録のプラグインを Pages で配布対象として紹介しない。逆に、登録済みのプラグインを紹介サイトから無言で省かない。
- カタログの項目を再利用してサイトを生成する仕組みを追加する場合は、プラグイン manifest と SKILL フロントマターを入力にする。サイト専用の重複メタデータを正本にしない。

## GitHub Pages の更新と同期

`docs/` を GitHub Pages の公開ルートとして扱う。サイトには、各プラグインと SKILL の目的、利用条件、導入方法、責務の境界、実行可能なプロンプト例を日本語で掲載する。

プラグインまたは SKILL に変更を加えたら、同じ変更で次を行う。

1. `docs/index.html` の一覧、カテゴリ、リンクを更新する。
2. `docs/plugins/<plugin-name>.md` と `docs/skills/<skill-name>.md` を追加または更新する。
3. 各 SKILL ページに、いつ使うか、前提条件、コピー可能なプロンプト例を最低一つ記載する。
4. プラグインと SKILL の正本（manifest / `SKILL.md`）と、ページ内の名前、説明、バージョン、導入コマンド、リンクを突き合わせる。
5. 削除・改名時は、古いページと索引リンクを同一変更で削除またはリダイレクトする。

紹介ページは製品仕様の代替ではない。正本との食い違いを見つけた場合は、どちらが正しいかを推測せず、プラグインの実装と manifest を確認してから両方を修正する。

GitHub Pages のビルド設定や公開 URL を変更する場合は、変更後にローカルのリンク切れを確認し、GitHub Actions を使う構成では対象ワークフローの成功も確認する。

## 変更前の最終確認

コミット前に、少なくとも次を確認する。

```bash
git diff --check
git status --short
rg -n --glob '!AGENTS.md' '(^|[^[:alnum:]_])/(Users|home)/' .
```

プラグインまたは SKILL を変更した場合は、対応する validator を実行し、カタログと `docs/` の更新漏れがないことを確認する。MCP を含む場合は、秘密情報が差分にないこと、manifest と `.mcp.json` の有無が一致することも確認する。無関係な変更を同じコミットに含めない。
