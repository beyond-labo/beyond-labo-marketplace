# OKF + SDD

OKF 0.2 の知識文書と `.kiro` の仕様駆動開発を扱う、18スキルのプラグインです。
バージョンは `0.1.0`。
既存の specs と steering 本文へ新しい根拠を統合し、要件・設計・タスク・承認・検証の食い違いを直します。
OKR（Objectives and Key Results）の目標管理は対象に含みません。

## 導入

[マーケットプレイスの追加手順](../install.html)に従って追加した後、`okf-sdd` を選びます。

```sh
codex plugin add okf-sdd@personal
```

## 最初の利用

マーケットプレイスから `okf-sdd` を導入し、新しいタスクで目的に合うスキルを呼び出します。
モデルは固定せず、利用者が選んだモデルとエージェント環境を使います。

```text
$kiro-discovery この機能追加について、既存仕様の更新範囲と新規仕様が必要な範囲を整理してください。
```

既存仕様の保守だけなら、次から始められます。

```text
$kiro-spec-sync --check この変更と関連する要件・設計・実装の整合性を読み取り専用で確認してください。
```

仕様生成を連続実行する場合は `$kiro-spec-quick <feature>`、複数仕様は `$kiro-spec-batch`、承認済みタスクの実装は `$kiro-impl <feature>` を使います。
`--auto` または既存の明示的な一括許可の範囲で工程承認を反映します。
スキルの選択、品質合格、検査成功だけでは承認を付与しません。
小さな修正を全工程へ通す必要はありません。

## 配布と導入設定

[利用環境と移行手順](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-spec-sync/references/setup.md) に、パス解決、任意のテンプレート導入、安全な更新、同名ローカルスキルとの共存を記載しています。
同梱テンプレートは直接読めるため、`.kiro/settings/` のコピーは必須ではありません。
既存の設定がある場合はそれを確認して使い、異なる形式を黙って上書きしません。
導入 CLI は `--apply` なしでは読取専用です。
AGENTS.md、Codex のモデル・エージェント設定、仕様本文、承認状態は自動導入しません。

検査 CLI は Python 3.10 以上、PyYAML 6.0.3 を使用します。
依存は [requirements.txt](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-spec-sync/scripts/requirements.txt) に固定し、プロジェクトの管理環境または専用仮想環境へ入れます。
MCP、API キー、サービス認証は不要です。

## 知識と承認

- 文書形式は [OKF プロファイル](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-spec-sync/assets/settings/okf-profile.md)、検査と入力記録は [共通手順](https://github.com/beyond-labo/beyond-labo-marketplace/blob/main/plugins/okf-sdd/skills/kiro-spec-sync/references/okf-workflow.md) に従います。
- `sources` は出典、`kiro.depends_on` は契約・設定依存を表します。外部資料の到達性や更新は自動検査しません。
- ハッシュ変更は意味の再確認を要求します。承認の自動失効・付与や、意味整合の保証ではありません。
- `spec.json` が承認・進行状態の正本です。要件の意味変更では下流の承認と完了を再評価し、誤字では適用可能な承認と検証証拠を再利用します。
- brief や steering だけの作業に spec.json を追加しません。重要判断のみ MADR の本文構成で記録します。
- 共有索引と共有方針はコントローラーが更新し、並列担当の書き込みを競合させません。

## 責務の境界

このプラグインは `.kiro` の文書と工程状態を所有します。
一般的なアーキテクチャ設計は System Architecture Design、文章の推敲は Communication Writing、グラフ探索は Graphify / CodeGraph、Git 操作は Git & GitHub Workflow の担当です。
それらを必須依存にせず、必要な場面だけ利用します。
同名ローカルスキルから移る場合は差分と呼び出す実パスを確認し、旧スキルや独自設定を自動削除しません。
プラグイン更新とプロジェクト設定更新は別です。更新後に setup の計画を読み、未変更の配布資産だけを更新してください。

## 開発検証

リポジトリルートで、依存を導入した環境から実行します。

```sh
python3 -B -m unittest discover -s plugins/okf-sdd/skills/kiro-spec-sync/tests -v
```

テストは CLI の変更検出・状態保持・参照境界と、配置を移した配布物のリンク解決・テンプレート適用・更新時の既存設定保持を確認します。
これらは実プロジェクトの意味整合や、すべての Codex 実行環境での挙動を保証しません。

## 含まれる SKILL

- [kiro-debug](../skills/kiro-debug.md)：.kiro の仕様駆動開発で、実装・検証失敗の原因を調べ、根拠のある修正と再検証を決める。原因不明の失敗や繰り返すレビュー指摘に使う。
- [kiro-discovery](../skills/kiro-discovery.md)：.kiro の仕様駆動開発で、新規・既存仕様・直接実装への振り分けと brief / roadmap を作る。方針やコードの一般的な調査だけには使わない。
- [kiro-impl](../skills/kiro-impl.md)：.kiro の仕様駆動開発で、承認済み仕様のタスクを実装・検証し、実装で得た知見を現行仕様へ同期する。タスク指定時はその範囲、未指定時は未完了タスクを扱う。
- [kiro-review](../skills/kiro-review.md)：.kiro の仕様駆動開発で、実装差分を現行の承認済み仕様・責務境界・検証証拠に照らしてレビューする。実装後、修正後、タスク受け入れ時に使う。
- [kiro-spec-batch](../skills/kiro-spec-batch.md)：.kiro の roadmap にある複数仕様を依存順に生成・更新する。仕様間レビューと共有索引の更新を統括する。
- [kiro-spec-design](../skills/kiro-spec-design.md)：.kiro の承認済み要件を設計文書と調査記録へ具体化し、工程の生成・承認状態を扱う。一般的なアーキテクチャ設計のみには使わない。
- [kiro-spec-init](../skills/kiro-spec-init.md)：.kiro に新しい機能仕様の制御 JSON と要件の雛形を作る。既存仕様の更新には sync を使う。
- [kiro-spec-quick](../skills/kiro-spec-quick.md)：単一の .kiro 仕様の要件・設計・タスクを必要な段階から連続生成する。--auto または既存の一括許可の範囲で承認を反映する。
- [kiro-spec-requirements](../skills/kiro-spec-requirements.md)：.kiro の機能仕様の要件と受け入れ条件を生成・更新する。一般的な文章推敲には使わない。
- [kiro-spec-status](../skills/kiro-spec-status.md)：.kiro の仕様駆動開発で、仕様の生成、承認、実装進捗と文書の同期状態を読み取り専用で確認する。
- [kiro-spec-sync](../skills/kiro-spec-sync.md)：.kiro の仕様駆動開発で、要件、設計、実装、方針の変更を関連文書へ反映し、古い承認と完了状態を再評価する。文書の矛盾発見、仕様変更、実装完了時に使う。--check は読み取り専用の整合性点検。
- [kiro-spec-tasks](../skills/kiro-spec-tasks.md)：.kiro の要件と設計から、依存関係と検証条件を持つ実装タスクを生成・更新する。
- [kiro-steering](../skills/kiro-steering.md)：.kiro の仕様駆動開発で、コードと決定の根拠をもとに、プロジェクト方針を作成または更新する。古い方針の置換と関連仕様への影響確認を含む。
- [kiro-steering-custom](../skills/kiro-steering-custom.md)：.kiro の仕様駆動開発で、API、テスト、セキュリティなど特定領域のプロジェクト方針を作成または更新する。
- [kiro-validate-design](../skills/kiro-validate-design.md)：.kiro の仕様駆動開発で、要件、関連仕様、実装上の根拠と設計を照合し、実装へ進める品質かをレビューする。
- [kiro-validate-gap](../skills/kiro-validate-gap.md)：.kiro の仕様駆動開発で、現行の要件と既存コードの差分を調べ、実装方針を選ぶための根拠を記録する。
- [kiro-validate-impl](../skills/kiro-validate-impl.md)：.kiro の仕様駆動開発で、実装後の機能について要件充足・設計整合・タスク間統合と検証証拠を確認する。対象タスク指定時は範囲を限定する。
- [kiro-verify-completion](../skills/kiro-verify-completion.md)：.kiro の仕様駆動開発で、タスク完了、修正成功、検証成功、機能 GO の主張を対象状態に対応する証拠と照合する。

[構成と検証記録](../research/okf-sdd.md)
