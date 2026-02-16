# Chaos Security Auditor (CSA)

An AI-driven adversarial security testing framework that combines chaos engineering principles with automated penetration testing — executed entirely within sandboxed environments.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   CSA CLI (Click)                    │
├──────────┬──────────────┬───────────┬───────────────┤
│  Recon   │   Vectors    │  Engine   │   Reporting   │
│          │              │           │               │
│ • Repo   │ • Application│ • Execute │ • Markdown    │
│   Mapper │ • Middleware │   Loop    │   Reports     │
│ • Surface│ • Infra      │ • Schedule│ • Jinja2      │
│   Analyze│              │   & Rank  │   Templates   │
│ • Dep    │              │           │               │
│   Audit  │              │           │               │
├──────────┴──────────────┴───────────┴───────────────┤
│              Docker Sandbox (Isolated)               │
│  ┌─────────┐   ┌──────────┐   ┌──────────────────┐ │
│  │   CSA   │◄─►│  Target  │◄─►│    Defender       │ │
│  │ Runner  │   │  Service │   │  (Log + Respond)  │ │
│  └─────────┘   └──────────┘   └──────────────────┘ │
└─────────────────────────────────────────────────────┘
```

## Phases

| Phase | Name | Description |
|-------|------|-------------|
| 1 | **Contextual Reconnaissance** | Clone repo, detect tech stack, map endpoints, audit dependencies for known CVEs |
| 2 | **Attack Vector Generation** | Generate application-, middleware-, and infrastructure-level attack vectors |
| 3 | **Execution Loop** | Hypothesize → Attack → Observe → Escalate with adaptive scheduling |

## Quickstart

```bash
# Install
pip install -e ".[dev]"

# Run the CLI
csa --help

# Run with Docker (sandboxed)
docker compose up
```

## Project Structure

```
chaos_auditor/
├── cli.py              # CLI entry point (Click)
├── config.py           # YAML/TOML config loader
├── recon/              # Phase 1: Reconnaissance
├── vectors/            # Phase 2: Attack Vector Generation
├── engine/             # Phase 3: Execution Loop
├── reporting/          # Chaos Report generation
└── defender/           # Defender integration & monitoring
```

## Safety & Governance

- All tests execute inside **isolated Docker containers** — never on host systems.
- The framework requires **explicit opt-in** via signed configuration before any active testing.
- Attack vectors are derived from **public vulnerability databases** (OWASP, CWE, NVD).
- All findings are logged with full provenance for audit trails.
- The defender module provides **real-time monitoring** and can halt tests that exceed defined thresholds.

## License

MIT
