<!-- Copyright (c) Microsoft Corporation. -->
<!-- Licensed under the MIT License. -->

# agent-mcp-governance

> **Public Preview** — Standalone Python package that exposes the
> Agent Governance Toolkit's MCP (Model Context Protocol) governance
> primitives for use outside the full AGT monorepo.

## Overview

`agent_mcp_governance` provides a typed re-export surface over the
MCP-specific governance modules in
[`agent-os-kernel`](https://pypi.org/project/agent-os-kernel/).  It is
**not** zero-dependency — it requires `agent-os-kernel >=3.0.0,<4.0.0`.

## Installation

```bash
pip install agent-mcp-governance
```

This will pull in `agent-os-kernel` automatically.

## Quick Start

```python
import warnings
from agent_mcp_governance import (
    # Tool-poisoning defence
    MCPSecurityScanner,
    MCPThreatType,
    # Gateway (request-level policy enforcement)
    MCPGateway,
    ResponsePolicy,
    # Session authentication
    MCPSessionAuthenticator,
    # Auth-method enforcement
    McpAuthPolicy,
    McpServerEntry,
)

# 1. Scan an MCP tool definition for poisoning / hidden instructions
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    scanner = MCPSecurityScanner()

threats = scanner.scan_tool(
    "web-search",
    "Search the web for information.",
    server_name="search-tools",
)
assert threats == []  # clean tool

# 2. Authenticate agent sessions
auth = MCPSessionAuthenticator()
token = auth.create_session("analyst-001")
session = auth.validate_session("analyst-001", token)
assert session is not None

# 3. Enforce per-server auth methods
policy = McpAuthPolicy(
    servers=[
        McpServerEntry(name="finance", allowed_auth_methods=["mtls"]),
    ]
)
result = policy.check("finance", auth_method="oauth2")
print(result.allowed, result.reason)  # False — not in allowlist
```

## API Reference

### Tool-poisoning defence

| Export | Source | Description |
|--------|--------|-------------|
| `MCPSecurityScanner` | `agent_os.mcp_security` | Scans tool definitions for poisoning, rug-pulls, cross-server attacks |
| `MCPSecurityConfig` | `agent_os.mcp_security` | Structured configuration (loadable from YAML) |
| `load_mcp_security_config` | `agent_os.mcp_security` | Load config from a YAML file |
| `MCPThreatType` | `agent_os.mcp_security` | Enum: `TOOL_POISONING`, `RUG_PULL`, `HIDDEN_INSTRUCTION`, … |
| `MCPSeverity` | `agent_os.mcp_security` | Enum: `INFO`, `WARNING`, `CRITICAL` |
| `MCPThreat` | `agent_os.mcp_security` | Single threat finding |
| `ScanResult` | `agent_os.mcp_security` | Aggregate scan outcome |
| `ToolFingerprint` | `agent_os.mcp_security` | Cryptographic tool fingerprint for rug-pull detection |

### Gateway (request-level policy enforcement)

| Export | Source | Description |
|--------|--------|-------------|
| `MCPGateway` | `agent_os.mcp_gateway` | Policy-enforcing gateway between MCP clients and servers |
| `GatewayConfig` | `agent_os.mcp_gateway` | Configuration produced by `MCPGateway.wrap_mcp_server` |
| `MCPResponseDecision` | `agent_os.mcp_gateway` | Verdict from `intercept_tool_response` |
| `ApprovalStatus` | `agent_os.mcp_gateway` | Enum: `PENDING`, `APPROVED`, `DENIED` |
| `ResponsePolicy` | `agent_os.mcp_gateway` | Enum: `BLOCK`, `SANITIZE`, `LOG` |
| `AuditEntry` | `agent_os.mcp_gateway` | Audit-log record for a tool call |

### Session authentication

| Export | Source | Description |
|--------|--------|-------------|
| `MCPSessionAuthenticator` | `agent_os.mcp_session_auth` | Creates, validates, and revokes cryptographic session tokens |
| `MCPSession` | `agent_os.mcp_session_auth` | An authenticated MCP session bound to an agent identity |

### Message signing / verification

| Export | Source | Description |
|--------|--------|-------------|
| `MCPMessageSigner` | `agent_os.mcp_message_signer` | Signs MCP messages with HMAC-SHA256 |
| `MCPSignedEnvelope` | `agent_os.mcp_message_signer` | Signed message envelope |
| `MCPVerificationResult` | `agent_os.mcp_message_signer` | Verification result |

### Auth-method enforcement

| Export | Source | Description |
|--------|--------|-------------|
| `McpAuthPolicy` | `agent_os.mcp_auth_enforcement` | Enforce per-server auth method allowlists |
| `McpServerEntry` | `agent_os.mcp_auth_enforcement` | Per-server auth configuration entry |
| `AuthCheckResult` | `agent_os.mcp_auth_enforcement` | Auth enforcement check result |

### Response scanning

| Export | Source | Description |
|--------|--------|-------------|
| `MCPResponseScanner` | `agent_os.mcp_response_scanner` | Scans tool responses for injection / PII / exfiltration |
| `MCPResponseScanResult` | `agent_os.mcp_response_scanner` | Scan result |
| `MCPResponseThreat` | `agent_os.mcp_response_scanner` | Individual response threat finding |

### Rate limiting

| Export | Source | Description |
|--------|--------|-------------|
| `MCPSlidingRateLimiter` | `agent_os.mcp_sliding_rate_limiter` | Sliding-window per-agent rate limiter |

### Protocol stores

| Export | Source | Description |
|--------|--------|-------------|
| `MCPAuditSink` / `InMemoryAuditSink` | `agent_os.mcp_protocols` | Audit record persistence |
| `MCPSessionStore` / `InMemorySessionStore` | `agent_os.mcp_protocols` | Session store backend |
| `MCPNonceStore` / `InMemoryNonceStore` | `agent_os.mcp_protocols` | Nonce store (replay protection) |
| `MCPRateLimitStore` / `InMemoryRateLimitStore` | `agent_os.mcp_protocols` | Rate-limit bucket storage |

### Metrics

| Export | Source | Description |
|--------|--------|-------------|
| `MCPMetrics` | `agent_os._mcp_metrics` | Default in-memory metrics recorder |
| `MCPMetricsRecorder` | `agent_os._mcp_metrics` | Protocol for custom metrics backends |

## Compatibility

| Python | agent-os-kernel |
|--------|----------------|
| ≥ 3.10 | ≥ 3.0.0, < 4.0.0 |

## License

[MIT](../../LICENSE) — Copyright (c) Microsoft Corporation.
