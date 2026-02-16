# Audit Phases

The Chaos Security Auditor operates in three sequential phases.

---

## Phase 1: Contextual Reconnaissance

**Goal:** Build a comprehensive understanding of the target before any active testing.

### Steps

1. **Repository Mapping** (`recon/repo_mapper.py`)
   - Clone or mount the target repository.
   - Detect languages, frameworks, and build systems.
   - Produce a `RepoProfile` describing the technology stack.

2. **Attack Surface Analysis** (`recon/surface_analyzer.py`)
   - Parse route definitions, controller files, and API schemas.
   - Enumerate HTTP/gRPC/WebSocket endpoints with auth metadata.
   - Discover webhook receivers and outbound integrations.
   - Map database schemas from migration files and ORM models.

3. **Dependency Audit** (`recon/dependency_audit.py`)
   - Locate package manifests (`requirements.txt`, `package.json`, `go.mod`, etc.).
   - Cross-reference installed versions against NVD, OSV, and GitHub Advisories.
   - Flag dependencies with known CVEs and suggest fixed versions.

### Outputs

- `RepoProfile` — technology stack metadata
- `AttackSurface` — endpoints, webhooks, DB schemas
- `list[VulnerablePackage]` — dependencies with known CVEs

---

## Phase 2: Attack Vector Generation

**Goal:** Produce a scored catalog of attack vectors from reconnaissance data.

### Levels

| Level | Module | Techniques |
|-------|--------|------------|
| Application | `vectors/application.py` | BOLA/IDOR, SQL/NoSQL/command injection, business-logic flaws |
| Middleware | `vectors/middleware.py` | Broker ACL bypass, cache poisoning, storage misconfiguration |
| Infrastructure | `vectors/infrastructure.py` | Container escape, Dockerfile audit, resource exhaustion |

### Scoring

Each vector receives a composite score computed from:

- **Severity** (0.0–10.0) — CVSS-aligned impact rating.
- **Likelihood** (0.0–1.0) — estimated exploitation probability.
- **Blast radius** (0.0–1.0) — scope of potential damage.

The scheduler (`engine/scheduler.py`) sorts vectors by composite score while respecting dependency ordering.

### Outputs

- Ordered list of `ScoredVector` objects ready for execution.

---

## Phase 3: Execution Loop

**Goal:** Execute vectors against the sandboxed target using the H→A→O→E cycle.

### Cycle

```
┌──────────────┐
│  Hypothesize │  Predict expected outcome
└──────┬───────┘
       ▼
┌──────────────┐
│    Attack    │  Send payload to target
└──────┬───────┘
       ▼
┌──────────────┐
│   Observe    │  Capture response + side effects
└──────┬───────┘
       ▼
┌──────────────┐
│   Escalate   │  Generate follow-up vectors if weakness confirmed
└──────────────┘
```

### Execution Rules

- Each vector runs with an individual timeout (configurable, default 30 s).
- The executor records every step as an immutable `ExecutionRecord`.
- Escalation vectors are appended to the scheduler queue in real-time.
- The defender monitor tracks detection events in parallel.

### Outputs

- `list[ExecutionRecord]` — full attack history
- `DefenderMetrics` — detection rate, TTD, TTR
- Final `ChaosReport` rendered from the Jinja2 template
