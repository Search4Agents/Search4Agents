# Why ARD?

Agentic Resource Discovery (ARD) exists to solve a specific gap: agents can now
*talk* to each other, but they still can't reliably *find* and *trust* each
other. Here are the core reasons it matters.

## 1. Discovery is fragmented

Open protocols like **MCP**, **A2A**, and **Skills** standardize how agents talk
once connected — but there's no standard way to *find* a capability in the first
place. The result today is hundreds of disconnected catalogs held together by
brittle, hard-coded integrations. ARD gives the ecosystem **one shared discovery
mechanism**.

## 2. Trust and verification

At runtime an agent must ask: *"Is this endpoint really who it claims to be?"*
Without a shared trust anchor, any endpoint could be an impostor. ARD anchors
identity to **domains you already own** (HTTPS, domain-anchored identifiers, plus
optional attestations and signatures via the Trust Manifest), so publishers can
be verified — no new certificate authority needed.

## 3. No central gatekeeper (open + federated)

Closed registries only solve discovery inside their own walls. ARD is web-native
self-publishing at `/.well-known/ai-catalog.json` — no registration, owned by no
one, with **federated registries** that refer to one another so no single
operator becomes a chokepoint. You remain the source of truth for your own
catalog.

## 4. Selection by intent, not just existence

Knowing a tool *exists* isn't the same as knowing it's the *right one*. ARD lets
an agent query in plain language and get back **ranked, machine-readable
candidates** it can act on.

## 5. Protocol-agnostic interoperability

ARD sits *above* MCP, A2A, and OpenAPI as a discovery and selection layer rather
than replacing them — and indexes heterogeneous artifacts (agents, MCP servers,
skills, datasets, model cards) through **media types**, so each layer can evolve
independently.

## 6. Low barrier, progressive complexity

*"If you can host a file, you can be discovered."* Start with a **Minimal**
catalog (just a list), grow to **Discoverable** (host + well-known URI), then
**Trusted** (publisher identity, attestations, provenance). And the whole
discover → verify → connect loop can run **autonomously at runtime**, with no
human in it.

---

Ready to try it? See the [Catalog](catalog.md) page for a simple, working
example.
