# Application-Level Attack Vector Catalog

Vectors targeting the application layer of the target service.

---

## 1. Broken Object Level Authorization (BOLA / IDOR)

**References:** OWASP API1:2023, CWE-639

Attempt to access or modify resources belonging to other users by manipulating object identifiers in API requests.

| Technique | Description |
|-----------|-------------|
| Sequential ID enumeration | Iterate numeric IDs to access unauthorized records |
| UUID prediction | Test for predictable UUID generation patterns |
| Parameter tampering | Swap user/tenant IDs in request bodies and query strings |
| GraphQL node traversal | Exploit relay-style node IDs to fetch unauthorized objects |

---

## 2. Injection

**References:** OWASP A03:2021, CWE-89, CWE-78, CWE-94

Inject malicious payloads into input fields that are processed by interpreters.

| Technique | Description |
|-----------|-------------|
| SQL injection | Classic `' OR 1=1 --` and blind/time-based variants |
| NoSQL injection | MongoDB `$gt`, `$ne` operator injection |
| Command injection | Shell metacharacters in system-call parameters |
| Template injection (SSTI) | Jinja2/Twig/Freemarker expression payloads |
| LDAP injection | Wildcard and filter manipulation in LDAP queries |

---

## 3. Business-Logic Flaws

**References:** OWASP A04:2021, CWE-362, CWE-841

Exploit assumptions in the application's state machine or workflow.

| Technique | Description |
|-----------|-------------|
| Race conditions (TOCTOU) | Concurrent requests to exploit check-then-act gaps |
| State-machine bypass | Skip steps in multi-stage workflows (e.g., checkout) |
| Privilege escalation | Modify role or permission fields in self-service endpoints |
| Price/quantity manipulation | Alter pricing or inventory values in client-controlled data |
| Replay attacks | Re-submit captured tokens or transaction requests |

---

## 4. Authentication & Session

**References:** OWASP A07:2021, CWE-287, CWE-384

| Technique | Description |
|-----------|-------------|
| Credential stuffing | Automated login with known leaked credential pairs |
| JWT manipulation | Algorithm confusion (`none`, `HS256` vs `RS256`), claim tampering |
| Session fixation | Force a known session ID before authentication |
| Password reset abuse | Token prediction, email-based account takeover |
