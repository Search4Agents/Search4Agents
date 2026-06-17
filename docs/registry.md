# Known catalogs

This is the public, federated **registry** of agentic-resource catalogs we know
about. Each row points at a catalog hosted and owned by its publisher — we link
to it, we don't host it.

Want to be listed? Follow the [Register a service](register.md) plan: publish
your `ai-catalog.json`, then open a pull request adding **one row** to the table
below.

!!! info "How to read this list"

    The **Catalog URL** is the live, well-known endpoint an agent or registry
    crawls. The **GitHub repository** is where the catalog (and often the
    services) are maintained. **Kinds** shows what the catalog publishes:
    `agents` (A2A), `mcp` (servers/tools), and/or `skills`.

<!-- BEGIN KNOWN CATALOGS -->
<!-- Add new entries in alphabetical order by Name. Keep one entry per row. -->

| Name | GitHub repository | Catalog URL | Kinds | Notes |
| --- | --- | --- | --- | --- |
| Search 4 Agents | [Search4Agents/Search4Agents.github.io](https://github.com/Search4Agents/Search4Agents.github.io) | <https://search4agents.github.io/.well-known/ai-catalog.json> | agents, mcp, skills | This site's own demo catalog, including downloadable demo skills. |

<!-- END KNOWN CATALOGS -->

## Add your catalog

1. Fork [`Search4Agents/Search4Agents.github.io`](https://github.com/Search4Agents/Search4Agents.github.io).
2. Add your row above (keep the table alphabetical by **Name**).
3. Open a pull request — see the full checklist on
   [Register a service](register.md#acceptance-checklist).

[Add your catalog via Pull Request :material-source-pull:](https://github.com/Search4Agents/Search4Agents.github.io/edit/main/docs/registry.md){ .md-button .md-button--primary }
