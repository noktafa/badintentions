# System Architecture

## Overview

The Chaos Security Auditor (CSA) is structured as a modular CLI framework with four core subsystems orchestrated inside Docker-based sandboxes.

## Component Diagram

```mermaid
graph TB
    subgraph CLI["CSA CLI (Click)"]
        Config[Config Loader]
        CLI_Entry[Entry Point]
    end

    subgraph Recon["Phase 1: Reconnaissance"]
        RM[Repo Mapper]
        SA[Surface Analyzer]
        DA[Dependency Audit]
    end

    subgraph Vectors["Phase 2: Vector Generation"]
        AV[Application Vectors]
        MV[Middleware Vectors]
        IV[Infrastructure Vectors]
    end

    subgraph Engine["Phase 3: Execution"]
        EX[Executor<br/>H→A→O→E Loop]
        SC[Scheduler]
    end

    subgraph Reporting["Output"]
        RP[Report Generator]
        TM[Jinja2 Templates]
    end

    subgraph Sandbox["Docker Sandbox Network"]
        Target[Target Service]
        Defender[Defender Monitor]
    end

    CLI_Entry --> Config
    CLI_Entry --> Recon
    Recon --> Vectors
    Vectors --> SC
    SC --> EX
    EX -->|attacks| Target
    Target -->|responses| EX
    EX -->|findings| RP
    RP --> TM
    Defender -->|monitors| Target
    Defender -->|metrics| RP
```

## Data Flow

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant Recon
    participant Vectors
    participant Scheduler
    participant Executor
    participant Target
    participant Defender
    participant Reporter

    User->>CLI: csa recon --repo <url>
    CLI->>Recon: clone & analyze
    Recon-->>CLI: RepoProfile + AttackSurface

    User->>CLI: csa attack --level all
    CLI->>Vectors: generate(profile, surface)
    Vectors-->>Scheduler: unordered vectors
    Scheduler-->>Executor: prioritized queue

    loop For each vector
        Executor->>Executor: hypothesize()
        Executor->>Target: attack(payload)
        Target-->>Executor: response
        Executor->>Executor: observe(response)
        Defender-->>Defender: detect & log
        Executor->>Executor: escalate(observations)
    end

    User->>CLI: csa report -o report.md
    CLI->>Reporter: generate(records, metrics)
    Defender-->>Reporter: DefenderMetrics
    Reporter-->>User: chaos_report.md
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Click-based CLI | Composable sub-commands, rich help text, easy testing |
| Docker isolation | All active testing runs in sandboxed containers with no host access |
| Internal bridge network | `internal: true` prevents sandbox containers from reaching the internet |
| Jinja2 reporting | Flexible template-based output; supports Markdown, HTML, JSON |
| Dataclass models | Immutable, typed data structures for passing findings between phases |
