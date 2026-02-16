# Middleware-Level Attack Vector Catalog

Vectors targeting middleware components — message brokers, caches, and object storage.

---

## 1. Message Brokers (Kafka, RabbitMQ, NATS)

**References:** CWE-284, CWE-311

| Technique | Description |
|-----------|-------------|
| ACL bypass | Produce/consume on topics without proper authorization |
| Payload injection | Inject malformed or oversized messages to disrupt consumers |
| Topic squatting | Create topics with names matching internal conventions |
| Unencrypted transport | Sniff plaintext messages on non-TLS connections |
| Dead-letter abuse | Exploit dead-letter queues to recover sensitive payloads |

---

## 2. Cache Stores (Redis, Memcached)

**References:** CWE-284, CWE-502

| Technique | Description |
|-----------|-------------|
| Unauthenticated access | Connect to unprotected Redis/Memcached instances |
| Cache poisoning | Overwrite cached values to serve malicious data |
| Deserialization attacks | Inject crafted serialized objects into cache entries |
| Key enumeration | Scan key-space patterns to discover sensitive cached data |
| Lua script injection (Redis) | Exploit `EVAL` with untrusted input to execute server-side scripts |

---

## 3. Object Storage (S3, GCS, Azure Blob)

**References:** CWE-732, CWE-918

| Technique | Description |
|-----------|-------------|
| Public bucket discovery | Enumerate world-readable bucket configurations |
| ACL misconfiguration | Test for overly permissive bucket policies |
| SSRF via signed URLs | Exploit pre-signed URL generation to access internal resources |
| Path traversal | Manipulate object keys to access files outside intended prefix |
| Metadata leakage | Inspect object metadata for secrets or internal identifiers |

---

## 4. Reverse Proxies & API Gateways

**References:** CWE-444, CWE-918

| Technique | Description |
|-----------|-------------|
| HTTP request smuggling | Exploit parser discrepancies between proxy and backend |
| Header injection | Inject `X-Forwarded-For`, `Host`, or custom headers to bypass controls |
| Rate-limit bypass | Rotate identifiers or use HTTP/2 multiplexing to evade throttling |
| Path normalization abuse | Use URL encoding or double-slashes to bypass route-based ACLs |
