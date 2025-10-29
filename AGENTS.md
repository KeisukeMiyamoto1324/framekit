# Repository Guidelines

## Project Structure & Module Organization
The `framekit/` package exposes the fluent video API; `master_scene_element.py` and `scene_element.py` orchestrate timelines, while the `*_element.py` files deliver renderable media primitives. Tests reside in `tests/` as runnable scripts (`basic.py`, `multi_scene.py`) that also serve as regression samples. Shared assets stay in `sample_asset/`, generated media in `output/`, and supporting metadata at the root (`deploy.sh`, `requirements.txt`, `design.md`).

## Build, Test, and Development Commands
Enable editable installs with `python -m pip install -e .` on Python 3.12. Refresh dependencies through `python -m pip install -r requirements.txt` when you need repeatable environments. Render smoke samples via `python tests/basic.py` or `python tests/multi_scene.py`, and run `python -m pytest tests` for automated coverage. Package checks use `python -m build` once sample renders pass.

## Coding Style & Naming Conventions
Keep the fluent chaining style—public mutators return `self`, factories may return new scenes. Use the mandated banner-style block comments, avoid docstrings, and stick to four-space indentation with early returns to limit nesting. Every function argument and return needs explicit type annotations; prefer concise constructs like comprehensions. Name modules and classes with clear nouns (`VideoElement`, `AudioElement`) and align filenames with their primary definitions.

## Testing Guidelines
Pytest discovers items in `tests/`; add new files as scripts with an optional guarded entry point when interactive runs help debugging. Compose scenes that stress new behaviours, asserting on durations, element counts, or file creation. Route media output to `output/` and clean up inside the test to keep the tree tidy. Document asset prerequisites in the leading comment block so contributors know which fonts or clips to fetch.

## Commit & Pull Request Guidelines
Keep commits short, imperative, and under 72 characters, matching the existing history. Combine related API, test, and docs changes to minimise noise, and avoid WIP commits. Pull requests should describe the scenario exercised, reference issues, and list repro commands or render notes. Before requesting review, rerun `python -m pytest tests` and confirm the sample scripts still render without errors.

## Asset & Configuration Notes
Store large binaries outside the repo and share scripted download steps when needed. Record new environment variables or codec requirements in `design.md` and the PR description. When adjusting packaging or `deploy.sh`, sync version updates in `pyproject.toml`. Keep secrets in ignored `.env` files and explain usage here.

## framekitについて
- framekitはpythonで動画編集するための全く新しいフレームワークです。
- framekitはfluent APIを採用します。全てのAPIメソッドはmethod chainに対応しています。

## コーディングスタイル
- コメントはラインバイラインで書いてはいけません。その代わり、処理の各ブロックにつき以下のように書いてください。

    # ---------------------------------------------------------
    # Comment here in English (up to 3 lines)
    # ---------------------------------------------------------
    Some code ...

- docstringを書いてはいけません。
- ネストを深くしてはいけません。Early break, early return, early continue を遵守してください。
- 全ての関数の引数と返り値には適切な型アノテーションをつけてください
- 関数の数をやたらに増やしてはいけません。
- コードはできるだけ最小の行数でかける書き方を採用してください。例えは配列内包表記[x for x in y]などを使用してスマートかつシンプルに書いてください。
