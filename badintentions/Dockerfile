FROM python:3.12-slim AS base

LABEL maintainer="CSA Team"
LABEL description="Chaos Security Auditor — sandboxed runner"

# Security: run as non-root
RUN groupadd --gid 1000 csa \
    && useradd --uid 1000 --gid csa --shell /bin/bash --create-home csa

# System dependencies for security tooling
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Install semgrep
RUN pip install --no-cache-dir semgrep

WORKDIR /app

# Install Python dependencies
COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir .

# Copy application code
COPY chaos_auditor/ ./chaos_auditor/

# Drop to non-root user
USER csa

ENTRYPOINT ["csa"]
CMD ["--help"]
