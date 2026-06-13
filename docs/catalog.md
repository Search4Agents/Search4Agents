# Catalog

A **catalog** is a single JSON file — `ai-catalog.json` — that lists the agentic
resources you publish. Each entry declares **what** the resource is (via a media
type), gives it a **stable identifier**, and says **where** to reach it.

This page walks through a simple example catalog with a few entries for each kind
of agent resource. You can [view the raw file](.well-known/ai-catalog.json) or
copy the snippets below.

## Live demo catalog

For demos, this site hosts a working catalog at the spec's well-known path —
served over HTTPS, exactly where agents and registries look for it:

```
https://search4agents.github.io/.well-known/ai-catalog.json
```

[:material-file-code: View the demo catalog](.well-known/ai-catalog.json){ .md-button .md-button--primary }

!!! tip "This site practices what it preaches"

    Every page also advertises this catalog via the `ai-catalog` link relation in
    its HTML `<head>`, so crawlers and agents can discover it automatically.
    Host yours the same way: `https://yourdomain.com/.well-known/ai-catalog.json`

## Anatomy of an entry

Every entry needs four things, plus a few optional but recommended fields:

| Field | Required | Description |
| --- | --- | --- |
| `identifier` | yes | A stable URN/URI, e.g. `urn:search4agents:a2a:research-assistant` |
| `displayName` | yes | Human-readable name |
| `mediaType` | yes | What kind of artifact this is (see below) |
| `url` *or* `data` | yes | Where to fetch it, or the artifact inline |
| `description` | recommended | A short summary |
| `version` | recommended | The artifact version (SemVer recommended) |
| `tags` | recommended | Keywords for filtering and discovery |

Media types identify each resource type:

| Resource | `mediaType` |
| --- | --- |
| Agent (A2A) | `application/a2a-agent-card+json` |
| MCP server (tools) | `application/mcp-server-card+json` |
| Skill | `application/agentskill+zip` |

## Examples by resource type

=== "Agents (A2A)"

    ```json
    {
      "identifier": "urn:search4agents:a2a:research-assistant",
      "displayName": "Research Assistant",
      "mediaType": "application/a2a-agent-card+json",
      "url": "https://agents.example.com/research-assistant",
      "description": "Plans and runs multi-step web research and returns cited summaries.",
      "version": "1.2.0",
      "tags": ["agent", "a2a", "research"]
    }
    ```

    Other examples in the catalog: **Travel Booking Agent**, **Code Review Agent**.

=== "MCP servers (tools)"

    ```json
    {
      "identifier": "urn:search4agents:mcp:weather",
      "displayName": "Weather MCP Server",
      "mediaType": "application/mcp-server-card+json",
      "url": "https://api.example.com/weather/.well-known/mcp/server-card.json",
      "description": "MCP tools for current conditions and forecasts by location.",
      "version": "1.0.0",
      "tags": ["mcp", "tools", "weather"]
    }
    ```

    Other examples in the catalog: **GitHub MCP Server**, **Database Query MCP Server**.

=== "Skills"

    ```json
    {
      "identifier": "urn:search4agents:skill:rubber-duck-debugger",
      "displayName": "Rubber Duck Debugger",
      "mediaType": "application/agentskill+zip",
      "url": "https://search4agents.github.io/skills/rubber-duck-debugger/skill.zip",
      "description": "A patient (slightly smug) rubber duck that helps you debug by making you explain your code line by line until you spot the bug yourself. Quack.",
      "version": "1.0.0",
      "tags": ["skill", "fun", "debugging", "demo"]
    }
    ```

    Other examples in the catalog: **Dad Joke Generator**, **Code Review Skill**,
    **PDF Summarizer Skill**, **Data Cleaning Skill**.

## Fun demo skills

Unlike the illustrative entries above, these two skills are **real and
downloadable** — packaged as `application/agentskill+zip` and hosted right here.
Crack one open to see the `SKILL.md` inside.

[:material-duck: Rubber Duck Debugger](skills/rubber-duck-debugger/skill.zip){ .md-button .md-button--primary }
[:material-emoticon-happy-outline: Dad Joke Generator](skills/dad-joke-generator/skill.zip){ .md-button .md-button--primary }

## The full catalog

The complete file ties it together — a `host` block plus an `entries` array with
three agents, three MCP servers, and five skills (including the two fun,
downloadable demo skills above).

[:material-download: Download `ai-catalog.json`](.well-known/ai-catalog.json){ .md-button }

```json title=".well-known/ai-catalog.json"
--8<-- "docs/.well-known/ai-catalog.json"
```

## Conformance levels

The specification defines three levels you can grow into:

- **Minimal** — just `specVersion` + `entries` (this example).
- **Discoverable** — add a `host` block and serve at the well-known URI.
- **Trusted** — add `publisher` and `trustManifest` for verifiable identity,
  attestations, and provenance.

Read the full specification at
[agent-card.github.io/ai-catalog](https://agent-card.github.io/ai-catalog/).
