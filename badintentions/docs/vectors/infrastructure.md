# Infrastructure-Level Attack Vector Catalog

Vectors targeting the container, orchestration, and host infrastructure layers.

---

## 1. Container Escape

**References:** CWE-250, CWE-269

| Technique | Description |
|-----------|-------------|
| Privileged container abuse | Exploit `--privileged` mode to access host devices |
| Mount namespace leak | Escape via bind-mounted host paths (`/var/run/docker.sock`) |
| Kernel exploit via capabilities | Leverage `CAP_SYS_ADMIN`, `CAP_NET_RAW`, etc. |
| `nsenter` / `unshare` abuse | Use namespace tools to break container boundaries |
| cgroup escape | Exploit writable cgroup `release_agent` for host code execution |

---

## 2. Dockerfile Security Audit

**References:** CWE-250, CWE-522, CIS Docker Benchmark

| Technique | Description |
|-----------|-------------|
| Running as root | Detect missing `USER` directive (default root execution) |
| Secrets in layers | Scan `COPY`, `ENV`, and `ARG` for embedded credentials |
| Unpinned base images | Flag `FROM` directives without digest or version pins |
| Excessive capabilities | Identify `--cap-add` or `--privileged` in compose/run configs |
| Unnecessary packages | Detect installation of debug tools (`curl`, `wget`, `netcat`) in production images |
| Multi-stage leaks | Check for secrets carried between build stages |

---

## 3. Resource Exhaustion

**References:** CWE-400, CWE-770

| Technique | Description |
|-----------|-------------|
| CPU bomb | Infinite loops or compute-heavy payloads to starve the container |
| Memory exhaustion | Allocate unbounded memory to trigger OOM kills |
| Fork bomb | Rapidly spawn processes to exhaust PID limits |
| Disk fill | Write large files to fill container or volume storage |
| File descriptor exhaustion | Open sockets/files without closing to hit `ulimit` |
| Network bandwidth saturation | Generate high-volume traffic within the sandbox network |

---

## 4. Orchestration (Kubernetes / Docker Compose)

**References:** CWE-284, CIS Kubernetes Benchmark

| Technique | Description |
|-----------|-------------|
| Service account token theft | Access the default mounted SA token for API server calls |
| Network policy bypass | Test for missing or permissive `NetworkPolicy` rules |
| Secret enumeration | List Kubernetes secrets via the API with over-privileged RBAC |
| Sidecar injection | Exploit admission controller gaps to inject malicious sidecars |
| Resource quota bypass | Deploy pods without limits to starve co-tenant workloads |

---

## 5. Host-Level (When Applicable)

**References:** CWE-732, CWE-269

| Technique | Description |
|-----------|-------------|
| SUID binary abuse | Discover and exploit SUID/SGID binaries for privilege escalation |
| Writable system paths | Check for world-writable directories in `$PATH` or `/etc` |
| Kernel module loading | Attempt to `insmod` / `modprobe` from within the container |
| Metadata service access | Query cloud instance metadata (169.254.169.254) for credentials |
