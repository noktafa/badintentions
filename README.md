<p align="center">
  <img src="assets/logo.svg" alt="Chaos Security Auditor" width="600" />
</p>

<p align="center">
  <strong>AI-driven adversarial security testing in sandboxed environments</strong>
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> &middot;
  <a href="#audit-scenarios">Scenarios</a> &middot;
  <a href="docs/architecture.md">Architecture</a> &middot;
  <a href="docs/phases.md">Phases</a> &middot;
  <a href="docs/vectors/">Vector Catalog</a>
</p>

---

## What is CSA?

**Chaos Security Auditor** combines chaos engineering principles with automated penetration testing. It maps a target's attack surface, generates prioritized attack vectors, and executes them inside isolated Docker sandboxes — producing a structured Chaos Report with findings, evidence, and remediation guidance.

All testing runs in **fully isolated containers** with no host or internet access. The framework is designed for authorized security testing, red-team exercises, and CI/CD security validation.

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
| 3 | **Execution Loop** | Hypothesize &rarr; Attack &rarr; Observe &rarr; Escalate with adaptive scheduling |

See [docs/phases.md](docs/phases.md) for detailed breakdowns.

## Attack Vector Coverage

| Level | Techniques | Reference |
|-------|-----------|-----------|
| **Application** | BOLA/IDOR, injection (SQL, NoSQL, command, SSTI), business-logic flaws, auth bypass | [Catalog](docs/vectors/application.md) |
| **Middleware** | Broker ACL bypass, cache poisoning, storage misconfiguration, request smuggling | [Catalog](docs/vectors/middleware.md) |
| **Infrastructure** | Container escape, Dockerfile audit, resource exhaustion, orchestration flaws | [Catalog](docs/vectors/infrastructure.md) |

## Audit Scenarios

Pre-built security audit scenarios adapted from real-world AI agent safety testing. All scenarios run locally with no cloud resources required.

| Module | Blocked | Confirm | Safe | What It Tests |
|--------|---------|---------|------|---------------|
| **Command Safety** | 10 | 8 | 6 | Destructive commands, reverse shells, privilege escalation, service management |
| **File Access** | 10 | — | — | Read/write protection for /etc/shadow, SSH keys, /etc/passwd, sudoers, kernel |
| **Secret Detection** | 8 patterns | — | — | OpenAI, AWS, GitHub, GitLab, Slack tokens, JWTs, env var exports |
| **Interpreter Evasion** | 17 | 7 | 9 | python3 -c, eval, bash -c, base64 pipe, PowerShell IEX, crontab, find -delete |
| **Content Scanning** | 9 | — | 3 | Reverse shells in files, curl\|bash, mimikatz, SUID, data exfiltration |
| **Injection Defense** | — | — | — | Output wrapping against prompt injection, write-then-execute detection |

```python
# Example: access scenario catalogs
from chaos_auditor.scenarios import BLOCKED_COMMANDS, SECRET_PATTERNS, EVASION_PATTERNS

for scenario in BLOCKED_COMMANDS:
    print(f"[{scenario.category}] {scenario.command} -> {scenario.expected}")
```

## Quickstart

### Install locally

```bash
pip install -e ".[dev]"
csa --help
```

### Run with Docker (sandboxed)

```bash
docker compose up
```

### Run reconnaissance

```bash
csa recon --repo https://github.com/your-org/target-app
```

### Generate report

```bash
csa report -o reports/chaos_report.md
```

## Project Structure

```
chaos_auditor/
├── cli.py                    # CLI entry point (Click)
├── config.py                 # YAML/TOML config loader
├── recon/                    # Phase 1: Contextual Reconnaissance
│   ├── repo_mapper.py        #   Clone & detect tech stack
│   ├── surface_analyzer.py   #   Map endpoints, webhooks, schemas
│   └── dependency_audit.py   #   Scan manifests for CVEs
├── vectors/                  # Phase 2: Attack Vector Generation
│   ├── application.py        #   BOLA, injection, logic flaws
│   ├── middleware.py          #   Broker, cache, storage audits
│   └── infrastructure.py     #   Container, Dockerfile, resources
├── engine/                   # Phase 3: Execution Loop
│   ├── executor.py           #   H→A→O→E cycle
│   └── scheduler.py          #   Vector prioritization
├── scenarios/                # Audit scenario catalogs
│   ├── command_safety.py     #   Command classification (blocked/confirm/safe)
│   ├── file_access.py        #   Read/write path protection
│   ├── secret_detection.py   #   API key & token redaction
│   ├── interpreter_evasion.py#   Inline exec & script bypass detection
│   ├── content_scanning.py   #   Dangerous file content patterns
│   └── injection_defense.py  #   Prompt injection & write-then-execute
├── reporting/                # Chaos Report output
│   ├── report.py             #   Report model & generator
│   └── templates/            #   Jinja2 markdown templates
└── defender/                 # Defender integration
    └── monitor.py            #   Log watcher & response tracker
```

## Test Suite

```
211 tests, 0.31s
├── tests/                    # Core module tests (51)
│   ├── test_cli.py           #   CLI help, flags, validation
│   ├── test_config.py        #   Config validation & defaults
│   ├── test_recon.py         #   Recon module stubs
│   ├── test_vectors.py       #   Vector generation stubs
│   ├── test_engine.py        #   Executor & scheduler stubs
│   ├── test_reporting.py     #   Report model & severity counting
│   └── test_defender.py      #   Defender metrics & monitor
└── tests/scenarios/          # Scenario validation tests (160)
    ├── test_command_safety.py    # 40 parametrized command tests
    ├── test_file_access.py       # 20 path protection tests
    ├── test_secret_detection.py  # 23 pattern & regex tests
    ├── test_interpreter_evasion.py # 52 evasion & regression tests
    ├── test_content_scanning.py  # 21 content scanning tests
    └── test_injection_defense.py # 4 defense mechanism tests
```

## Safety & Governance

- All tests execute inside **isolated Docker containers** with `internal: true` networking — no host or internet access.
- The framework requires **explicit opt-in** via signed configuration before any active testing.
- Attack vectors are derived from **public vulnerability databases** (OWASP, CWE, NVD).
- All findings are logged with full provenance for audit trails.
- The defender module provides **real-time monitoring** and can halt tests that exceed defined thresholds.
- Audit scenarios are **data-driven** — scenario catalogs define expected classifications, not live exploits.

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with verbose output
pytest -v

# Lint
ruff check chaos_auditor/ tests/

# Type check
mypy chaos_auditor/
```

## License

MIT
