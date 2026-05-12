# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""agent_mcp_governance — MCP governance primitives for the Agent Governance Toolkit.

Re-exports the Model Context Protocol (MCP) governance classes from
``agent-os-kernel`` so that downstream consumers can depend on a single,
focused package without importing the full kernel namespace.

Available symbols
-----------------
Tool-poisoning defence
    ``MCPSecurityScanner``, ``MCPSecurityConfig``, ``load_mcp_security_config``
    ``MCPThreatType``, ``MCPSeverity``, ``MCPThreat``, ``ScanResult``,
    ``ToolFingerprint``

Gateway (request-level policy enforcement)
    ``MCPGateway``, ``GatewayConfig``, ``MCPResponseDecision``,
    ``ApprovalStatus``, ``ResponsePolicy``

Session authentication
    ``MCPSessionAuthenticator``, ``MCPSession``

Message signing / verification
    ``MCPMessageSigner``, ``MCPSignedEnvelope``, ``MCPVerificationResult``

Auth-method enforcement
    ``McpAuthPolicy``, ``McpServerEntry``, ``AuthCheckResult``

Response scanning
    ``MCPResponseScanner``, ``MCPResponseScanResult``, ``MCPResponseThreat``

Sliding rate limiter
    ``MCPSlidingRateLimiter``

Protocol store interfaces (in-memory implementations included)
    ``MCPAuditSink``, ``InMemoryAuditSink``
    ``MCPSessionStore``, ``InMemorySessionStore``
    ``MCPNonceStore``, ``InMemoryNonceStore``
    ``MCPRateLimitStore``, ``InMemoryRateLimitStore``

Metrics
    ``MCPMetrics``, ``MCPMetricsRecorder``
"""

from __future__ import annotations

# NOTE: __version__ must match the [project] version in pyproject.toml.
__version__ = "3.5.0"

# ── Tool-poisoning defence ────────────────────────────────────────────────────
from agent_os.mcp_security import (
    MCPSecurityConfig,
    MCPSecurityScanner,
    MCPSeverity,
    MCPThreat,
    MCPThreatType,
    ScanResult,
    ToolFingerprint,
    load_mcp_security_config,
)

# ── Security gateway (request-level policy enforcement) ───────────────────────
from agent_os.mcp_gateway import (
    ApprovalStatus,
    AuditEntry,
    GatewayConfig,
    MCPGateway,
    MCPResponseDecision,
    ResponsePolicy,
)

# ── Session authentication ────────────────────────────────────────────────────
from agent_os.mcp_session_auth import (
    MCPSession,
    MCPSessionAuthenticator,
)

# ── Message signing / verification ────────────────────────────────────────────
from agent_os.mcp_message_signer import (
    MCPMessageSigner,
    MCPSignedEnvelope,
    MCPVerificationResult,
)

# ── Auth-method enforcement ───────────────────────────────────────────────────
from agent_os.mcp_auth_enforcement import (
    AuthCheckResult,
    McpAuthPolicy,
    McpServerEntry,
)

# ── Response scanning ─────────────────────────────────────────────────────────
from agent_os.mcp_response_scanner import (
    MCPResponseScanResult,
    MCPResponseScanner,
    MCPResponseThreat,
)

# ── Sliding rate limiter ──────────────────────────────────────────────────────
from agent_os.mcp_sliding_rate_limiter import MCPSlidingRateLimiter

# ── Protocol store interfaces + in-memory implementations ────────────────────
from agent_os.mcp_protocols import (
    InMemoryAuditSink,
    InMemoryNonceStore,
    InMemoryRateLimitStore,
    InMemorySessionStore,
    MCPAuditSink,
    MCPNonceStore,
    MCPRateLimitStore,
    MCPSessionStore,
)

# ── Metrics ───────────────────────────────────────────────────────────────────
from agent_os._mcp_metrics import MCPMetrics, MCPMetricsRecorder

__all__ = [
    "__version__",
    # Tool-poisoning defence
    "MCPSecurityScanner",
    "MCPSecurityConfig",
    "load_mcp_security_config",
    "MCPThreatType",
    "MCPSeverity",
    "MCPThreat",
    "ScanResult",
    "ToolFingerprint",
    # Gateway
    "MCPGateway",
    "GatewayConfig",
    "MCPResponseDecision",
    "ApprovalStatus",
    "ResponsePolicy",
    "AuditEntry",
    # Session authentication
    "MCPSessionAuthenticator",
    "MCPSession",
    # Message signing
    "MCPMessageSigner",
    "MCPSignedEnvelope",
    "MCPVerificationResult",
    # Auth-method enforcement
    "McpAuthPolicy",
    "McpServerEntry",
    "AuthCheckResult",
    # Response scanning
    "MCPResponseScanner",
    "MCPResponseScanResult",
    "MCPResponseThreat",
    # Sliding rate limiter
    "MCPSlidingRateLimiter",
    # Protocol stores
    "MCPAuditSink",
    "InMemoryAuditSink",
    "MCPSessionStore",
    "InMemorySessionStore",
    "MCPNonceStore",
    "InMemoryNonceStore",
    "MCPRateLimitStore",
    "InMemoryRateLimitStore",
    # Metrics
    "MCPMetrics",
    "MCPMetricsRecorder",
]

