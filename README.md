# Search 4 Agents

An education and information site about **Agentic Resource Discovery (ARD)** —
the open, web-native way for any AI agent, on any platform, to discover and
verify the capabilities it needs: other **agents**, **MCP servers (tools)**, and
**skills**.

Built with [MkDocs](https://www.mkdocs.org/) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Live site

- **Site:** https://search4agents.github.io/
- **Catalog (spec well-known root):** https://search4agents.github.io/.well-known/ai-catalog.json
- **Fun skills:**
  - https://search4agents.github.io/skills/rubber-duck-debugger/skill.zip
  - https://search4agents.github.io/skills/dad-joke-generator/skill.zip

## Develop locally

```bash
pip install -r requirements.txt
mkdocs serve            # live preview at http://127.0.0.1:8000
mkdocs build --strict   # production build into ./site
```

## Demo skills

The two fun skills are real `application/agentskill+zip` artifacts. Edit the
source in `skills/<name>/SKILL.md`, then repackage the zips:

```bash
python3 skills/build_skills.py
```

## Publishing

- **Manual:** `mkdocs gh-deploy --clean` builds the site and pushes it to the
  `gh-pages` branch.
- **Automated:** pushing to `main` runs `.github/workflows/docs.yml`, which
  builds (`--strict`) and deploys to GitHub Pages.

> Pick a single GitHub Pages source to match your method: *Deploy from a branch
> → `gh-pages`* for the manual route, or *GitHub Actions* for the automated one.

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
Feature requests are welcome — please open a Pull Request.
