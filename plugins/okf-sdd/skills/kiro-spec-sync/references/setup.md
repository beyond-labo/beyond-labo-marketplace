# 利用環境と配布リソース

## パスと設定

このファイルはインストールされた `kiro-spec-sync` の `references/` にある。
`SKILL_DIR` はその親、つまり `kiro-spec-sync/SKILL.md` のある実ディレクトリを指す。
スキル一覧に渡された実パスから解決し、キャッシュのバージョン名や `.agents/skills/` の存在を推測しない。
以降のコマンドでは `SKILL_DIR` をそのパスに設定し、対象プロジェクトのルートで実行する。
プラグイン内の `rules/`、`references/`、兄弟スキルへのリンクは、参照を書いたファイルを基準に解決する。
`$1` は feature 名、`$ARGUMENTS` は実際のユーザー入力を指す説明用表記であり、シェルへ文字通り渡さない。

`.kiro/settings/templates/` に必要なファイルがあればそれを使い、なければ同じ相対名の [同梱テンプレート](../assets/settings/templates/) を読む。
設定をコピーしなくても作業できる。
プロファイルはプロジェクトの `.kiro/settings/okf-profile.md` があれば読み、なければ [同梱プロファイル](../assets/settings/okf-profile.md) を使う。
既存設定が同梱形式と異なる場合は差を確認する。内容を黙って置換せず、CLI で検査できない部分は制約として報告する。
スキルやモデルに仕様のない製品判断を委ねる許可は含まれない。

## 任意の設定導入・更新

標準ライブラリのみの導入コマンドは、既定で計画表示だけを行う。

```sh
python3 "$SKILL_DIR/scripts/setup_project.py" --root .
python3 "$SKILL_DIR/scripts/setup_project.py" --root . --apply
```

`--apply` は設定導入が依頼範囲に含まれる場合に使う。
対象は profile と templates のみ。既存 AGENTS.md、spec.json、specs、steering 本文、Codex 設定を作成・上書きしない。
初回に既存だったファイルと、導入後に利用者が変更したファイルは `preserve-local` として保持する。
`.kiro/settings/okf-sdd-install.json` は導入した資産のハッシュだけを記録する。
このファイルも設定と一緒にバージョン管理すれば、次回更新で未変更の同梱資産だけを更新できる。
プラグイン更新後も同じコマンドで計画を確認する。
`preserve-local` のファイルは同梱との差分を読み、必要な改善だけを既存許可の範囲で統合する。削除された配布資産は自動削除しない。
複数担当がいる場合はコントローラーだけが設定を導入・更新する。同時実行中には使わない。

## 検査 CLI の依存

Python 3.10 以上と PyYAML 6.0.3 が必要。
既存のプロジェクト管理環境を利用するか、プロジェクト内に専用環境を作る。
インストール時にネットワークや実行権限が必要なら環境の承認手順に従う。
次は専用環境の例で、`.venv-okf/` はプロジェクトの ignore 設定へ追加し、コミットしない。
依存インストールは検査とは別操作であり、読取専用依頼の中で自動実行しない。

```sh
python3 -m venv .venv-okf
.venv-okf/bin/python -m pip install -r "$SKILL_DIR/scripts/requirements.txt"
.venv-okf/bin/python "$SKILL_DIR/scripts/okf.py" check --root . --feature example
```

Windows では `.venv-okf/Scripts/python.exe` を使う。
以降の共通手順の `python3` はこの依存を持つ Python に読み替える。
CLI は外部 URL を取得せず、MCP・API キー・認証を必要としない。

## 既存ローカルスキルからの移行

`kiro-*` 名と `.kiro` の配置は維持する。
同名ローカルスキルがある場合は差分を確認し、どちらを正本として使うか決める。
プラグインを選ぶ場合は呼び出すスキルの実パスを確認する。既存スキルを自動削除しない。
旧 AGENTS.md が `.agents/skills/kiro-*` を指す場合は、その参照をインストール済みスキルの探索へ変更する。
これは対象プロジェクトで依頼されたときに行い、プラグイン導入のみでは書き換えない。
既存 spec.json の未知フィールド、ID、承認は保持し、触れる文書から意味を照合して移行する。

## 独立レビューとモデル

モデル、推論強度、エージェント名を固定しない。
独立レビューが有用で利用可能なら、対象ファイル、許可範囲、読取専用の制約を担当へ渡す。
[spec-reviewer.toml](../assets/spec-reviewer.toml) は任意のレビュアー定義例。自動登録しない。
名前付きエージェントがなくても通常のレビュアーへ同じ観点を渡せる。
一般的な設計原則は利用可能な architecture スキルを必要時に参照できるが、別プラグインを必須依存にはしない。
