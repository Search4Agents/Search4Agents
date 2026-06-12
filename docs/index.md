# Search 4 Agents

**Search 4 Agents** is an **education and information** site about
**Agentic Resource Discovery (ARD)** — the open, web-native way for any AI agent,
on any platform, to discover and verify the capabilities it needs: other
**agents**, **MCP servers (tools)**, and **skills**.

!!! info "What this site is"

    This is a learning and reference resource. It explains the concepts, points
    to the underlying open specifications, and provides simple, copy-pasteable
    examples — including a sample [catalog](catalog.md).

!!! example "Live demo catalog"

    For demos, this site hosts a working catalog at the spec's well-known path:
    [`/.well-known/ai-catalog.json`](.well-known/ai-catalog.json). See the
    [Catalog](catalog.md#live-demo-catalog) page for details.

## Why discovery matters

The era of standalone agents is ending. Agents increasingly need to call a
resource — a tool, a skill, or another agent — built by someone else. Open
protocols like **MCP**, **A2A**, and **Skills** standardize how agents *talk*
once connected, but connecting first requires *discovery*:

- **Where does the right capability live?**
- **Is it really who it claims to be?**
- **Which one should I actually use?**

Agentic Resource Discovery answers these by borrowing the best idea the web ever
had: **self-publishing at a well-known location.**

## How it works

1. **Publish a catalog.** Describe your capabilities in a single
   `ai-catalog.json` file — each agent, MCP server, or skill with a stable
   identifier, a description, where to reach it, and example queries.
2. **Host it at a well-known path:**
   `https://yourdomain.com/.well-known/ai-catalog.json`, served over HTTPS from
   your own domain. No registration, no gatekeeper.
3. **Get indexed.** Federated registries crawl published catalogs — like search
   engines crawl websites — and build a searchable index.
4. **Discover by intent.** An agent queries a registry in plain language and
   gets back ranked, machine-readable candidates.
5. **Verify, then connect.** The agent confirms the publisher's identity,
   checks attestations, then hands off to MCP, A2A, or whatever protocol the
   capability speaks.

See the [Catalog](catalog.md) page for a simple, working example.

## Learn more

- AI Catalog specification: <https://agent-card.github.io/ai-catalog/>

## License

The content and examples on this site are licensed under the
**[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)**.

## Requesting features

Have an idea or want something added? **Open a Pull Request** in our GitHub
repository:

[Open a Pull Request :material-source-pull:](https://github.com/Search4Agents/Search4Agents/pulls){ .md-button .md-button--primary }

For substantial changes, please open a PR describing the change so we can discuss
it. (We track feature requests through PRs rather than a separate form.)
