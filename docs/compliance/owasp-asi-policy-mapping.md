# OWASP ASI Policy Mapping

<!-- Copyright (c) Microsoft Corporation. -->
<!-- Licensed under the MIT License. -->

Cross-references every rule in the ASI starter policy packs
(`examples/policy-templates/`) to the OWASP Agentic Security Initiative
(ASI) Top 10 risk it mitigates. Use this table during security audits.

**References:** 
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Arcanum-Sec: Prompt Injection Taxonomy](https://github.com/Arcanum-Sec/arc_pi_taxonomy)
- [Arcanum-Sec: sec-context (Code Anti-Patterns)](https://github.com/Arcanum-Sec/sec-context)

---

## Cross-Reference Table

| Rule Name | Pack(s) | ASI Risk(s) | AGT Component |
|-----------|---------|-------------|---------------|
| `asi01-prompt-injection-override` | All | ASI-01 | Agent OS — Policy Engine |
| `asi01-prompt-injection-role-hijack` | All | ASI-01 | Agent OS — Policy Engine |
| `asi01-prompt-injection-delimiter` | All | ASI-01 | Agent OS — MCP Proxy Sanitizer |
| `healthcare-asi01-cbrn-guardrail` | healthcare | ASI-01 | Agent OS — Policy Engine |
| `asi01-prompt-injection-jailbreak` | general-saas | ASI-01 | Agent OS — Policy Engine |
| `asi01-integrity-shipping-guardrail` | All | ASI-01, ASI-02 | Business Continuity — Logistics Guard |
| `asi01-integrity-fraud-guardrail` | All | ASI-01, ASI-02 | Business Continuity — Fraud Guard |
| `asi01-nested-swarm-guardrail` | general-saas | ASI-01 | AgentMesh — Delegation Guard |
| `asi02-block-shell-execution` | All | ASI-02 | Agent OS — Capability Sandboxing |
| `asi02-block-network-exfiltration` | All | ASI-02 | Agent OS — Capability Sandboxing |
| `asi02-block-file-deletion` | healthcare | ASI-02 | Agent OS — Capability Sandboxing |
| `asi02-block-destructive-operations` | financial-services, general-saas | ASI-02 | Agent OS — Capability Sandboxing |
| `financial-asi02-obfuscation-guardrail` | financial-services | ASI-02 | Agent OS — Binary Inspector |
| `asi02-block-database-mutation` | general-saas | ASI-02 | Agent SRE — Audit Trail |
| `asi03-block-privilege-escalation` | All | ASI-03 | AgentMesh — DID Identity & Trust |
| `asi03-block-credential-access` | All | ASI-03 | AgentMesh — DID Identity & Trust |
| `financial-asi03-identity-guardrail` | financial-services | ASI-03 | AgentMesh — Trust Boundary |
| `asi03-block-user-impersonation` | general-saas | ASI-03 | AgentMesh — DID Identity & Trust |
| `asi03-account-mfa-bypass` | All | ASI-03 | AgentMesh — Identity Governance |
| `asi03-account-admin-promotion` | All | ASI-03 | AgentMesh — Identity Governance |
| `asi03-account-password-reset` | All | ASI-03 | AgentMesh — Identity Governance |
| `asi03-account-audit-tampering` | All | ASI-03 | AgentMesh — Identity Governance |
| `asi04-supply-chain-tool-enumeration` | All | ASI-04 | Agent OS — Recon Guard |
| `asi04-supply-chain-dependency-poisoning` | All | ASI-04 | Agent OS — Payload Guard |
| `asi04-supply-chain-plugin-hijack` | All | ASI-04 | Agent OS — Registry Proxy |
| `asi04-supply-chain-config-mutation` | All | ASI-04 | Agent OS — State Guard |
| `asi05-block-code-execution` | All | ASI-05 | Agent Runtime — Execution Rings |
| `asi05-block-dynamic-eval` | All | ASI-05 | Agent Runtime — Execution Rings |
| `asi05-sandbox-anti-pattern-detection` | All | ASI-05 | Agent Runtime — Context Guard |
| `asi05-block-ssh` | general-saas | ASI-05 | Agent Runtime — Execution Rings |
| `asi06-context-budget-limit` | All | ASI-06 | Agent OS — VFS / ContextScheduler |
| `asi06-block-context-manipulation` | All | ASI-06 | Agent OS — Context Integrity Firewall |
| `asi07-hidden-channel-guardrail` | All | ASI-07 | AgentMesh — Signal Monitor |
| `asi08-session-tool-call-limit` | All | ASI-08 | Agent SRE — Circuit Breakers |
| `asi08-swarm-heat-guardrail` | All | ASI-08 | Agent SRE — Swarm Monitor |
| `asi09-trust-payment-redirection` | All | ASI-09 | Business Continuity — Trust Firewall |
| `asi09-trust-vip-impersonation` | All | ASI-09 | Business Continuity — Trust Firewall |
| `asi09-trust-urgency-pretext` | All | ASI-09 | Business Continuity — Trust Firewall |
| `asi09-trust-phishing-link` | All | ASI-09 | Business Continuity — Trust Firewall |
| `asi10-charter-roleplay-block` | All | ASI-10 | Agent OS — Charter Enforcement |
| `asi10-charter-purpose-override` | All | ASI-10 | Agent OS — Charter Enforcement |
| `asi10-charter-autonomous-loop` | All | ASI-10 | Agent OS — Charter Enforcement |
| `asi03-block-credentials-in-output` | All | ASI-02, ASI-03 | Agent OS — Policy Engine |
| `asi06-block-pii-ssn` | All | ASI-01, ASI-06 | Agent OS — PII Protection |
| `healthcare-block-phi-mrn` | healthcare | ASI-01, ASI-06 | Agent OS — PII Protection |
| `healthcare-block-phi-dea` | healthcare | ASI-01, ASI-06 | Agent OS — PII Protection |
| `healthcare-enforce-deidentification` | healthcare | ASI-02, ASI-06 | Agent OS — Data Pipeline Security |
| `financial-block-pii-credit-card` | financial-services | ASI-01, ASI-06 | Agent OS — PII Protection |
| `saas-block-pii-email-bulk` | general-saas | ASI-02, ASI-06 | Agent OS — PII Protection |
| `edu-socratic-bypass-prevention` | education | ASI-01, ASI-10 | Agent OS — Charter Enforcement |
| `edu-parasocial-bond-prevention` | education | ASI-09 | Business Continuity — Trust Firewall |
| `edu-identity-reset-trigger` | education | ASI-09 | Business Continuity — Trust Firewall |
| `edu-ban-emotion-recognition` | education | EU AI Act Art 5 | Agent OS — Affect Guard |
| `edu-block-biometric-leak` | education | ASI-06 (COPPA 2026) | Agent OS — PII Protection |
| `edu-coppa-minor-location-block` | education | COPPA 2026 | Agent OS — PII Protection |
| `edu-parental-consent-check` | education | COPPA 2026 | Agent OS — Consent Gate |
| `edu-block-pii-ssn` | education | ASI-01, ASI-06 | Agent OS — PII Protection |
| `edu-restrict-untrusted-tools` | education | ASI-04 | Agent OS — Registry Proxy |
| `edu-v2-recursive-attestation` | education | ASI-04 | AgentMesh — SBOM Attestation |
| `edu-v2-entropy-binary-gate` | education | ASI-06 | Agent OS — Binary Inspector |
| `edu-v2-sentiment-anchor` | education | ASI-09 | Business Continuity — Static Professional Anchor |
| `edu-v2-art5-hard-block` | education | EU AI Act Art 5 | Agent OS — Affect Guard |
| `edu-v2-audit-tamper-chain` | education | EU AI Act Art 12 | Agent SRE — DID-Mesh Audit Chain |
| `cs-block-grooming` | education | ASI-09 (Child Safety) | Business Continuity — Trust Firewall |
| `cs-escalate-self-harm` | education | ASI-09 (Child Safety) | Agent SRE — Safety Escalation |
| `cs-block-contact-solicitation` | education | ASI-09 (Child Safety) | Agent OS — PII Protection |
| `cs-block-meeting-arrangement` | education | ASI-09 (Child Safety) | Business Continuity — Trust Firewall |

> `education` also adopts the generic `asiNN-` rules tagged **All** above
> (ASI-01/02/03/05/06/07/08/10), including the `asi10-charter-*` rules.

---

## ASI Risk Coverage Matrix

| ASI Risk | healthcare | financial-services | general-saas | education |
|----------|:----------:|:-----------------:|:------------:|:--------:|
| ASI-01 Agent Goal Hijack | ✅ | ✅ | ✅ | ✅ |
| ASI-02 Tool Misuse & Exploitation | ✅ | ✅ | ✅ | ✅ |
| ASI-03 Identity & Privilege Abuse | ✅ | ✅ | ✅ | ✅ |
| ASI-04 Agentic Supply Chain | 🔗 | 🔗 | 🔗 | ✅ |
| ASI-05 Unexpected Code Execution | ✅ | ✅ | ✅ | ✅ |
| ASI-06 Memory & Context Poisoning | ✅ | ✅ | ✅ | ✅ |
| ASI-07 Insecure Inter-Agent Communication | 🔗 | 🔗 | 🔗 | ✅ |
| ASI-08 Cascading Agent Failures | ✅ | ✅ | ✅ | ✅ |
| ASI-09 Human-Agent Trust Exploitation | 🔗 | 🔗 | 🔗 | ✅ |
| ASI-10 Rogue Agents | 🔗 | 🔗 | 🔗 | ✅ |

**Legend:**
- ✅ Direct policy rule(s) in this starter pack mitigate this risk
- 🔗 Covered by the AGT runtime stack — see [OWASP ASI coverage](owasp-agentic-top10-architecture.md)

> ASI-04, ASI-07, ASI-09, and ASI-10 are primarily mitigated at the infrastructure
> layer (AgentMesh IATP, approval workflows, execution ring isolation). Policy-level
> controls for those risks require runtime context fields not universally available.
> These are tracked for future starter pack versions.
>
> `education` is a K-12 and minor-facing domain pack with **full ASI-01..10 policy
> coverage**. It adopts the generic `asiNN-` hard-gates plus the `asi10-charter-*`
> rules, and adds domain controls: Socratic goal-integrity (ASI-01/10), parasocial
> guardrails (ASI-09), a supply-chain tool allowlist (ASI-04), COPPA 2026 + EU AI
> Act Art 5/12 compliance, v2 cryptographic-governance rules, and child-safety
> controls (grooming, self-harm escalation, contact solicitation, in-person meeting).

---

## Default Posture by Pack

| Pack | Default Action | Max Tokens | Max Tool Calls | Confidence |
|------|:--------------:|:----------:|:--------------:|:----------:|
| `healthcare` | `deny` | 8,192 | 15 | 0.95 |
| `financial-services` | `deny` | 6,000 | 20 | 0.95 |
| `general-saas` | `deny` | 12,000 | 30 | 0.85 |
| `education` | `deny` | 4,000 | 15 | 0.95 |

All packs implement **deny-all by default**, enforcing the
[Least Agency principle](owasp-agentic-top10-architecture.md). `education`
additionally sets `audit_level: high`. Context-budget thresholds
(`asi06-context-budget-limit`) sit below each pack's `max_tokens` so the rule
stays reachable.

---

## Regulatory Alignment

| Regulation | Pack | Controls Applied |
|------------|------|-----------------|
| HIPAA §164.514 (PHI De-identification) | healthcare | SSN, MRN, DEA, NPI blocking |
| HIPAA §164.530 (Minimum Necessary) | healthcare | Deny-all default, read-only allowlist |
| PCI DSS Req 3 (Protect Account Data) | financial-services | PAN/SSN blocking in output |
| PCI DSS Req 6 (Secure Systems) | financial-services | Shell/code execution deny |
| SOX §302/906 (Financial Reporting) | financial-services | Transaction action audit trail |
| AML / BSA (Structuring Detection) | financial-services | Bulk transaction blocking |
| GDPR / CCPA (PII Minimization) | general-saas | SSN, bulk email blocking |
| COPPA 2026 (Verifiable Parental Consent, biometric PII) | education | Parental-consent gate, biometric-identifier leak block, <13 data-collection restriction, SSN blocking |
| EU AI Act Art 5 (Prohibited emotion recognition) | education | Affect/emotion-detection action + domain hard-block |
| EU AI Act Art 12 / FERPA / COPPA 2026 (Audit retention & data minimization) | education | DID-Mesh tamper-evident audit chain; records subject to FERPA / COPPA retention-limitation schedules |
| Child Safety (grooming / self-harm / solicitation) | education | Grooming, self-harm escalation, contact-solicitation, in-person-meeting blocks |

---

## Prior Art & Acknowledgments

These packs extend existing patterns from this repository:

- `examples/policies/production/healthcare.yaml` — PHI detection patterns
- `examples/policies/production/financial.yaml` — PCI/SOX patterns
- `examples/policies/production/enterprise.yaml` — general enterprise deny rules
- `examples/policies/prompt-injection-safety.yaml` — ASI-01 injection detection
- **Arcanum-Sec Intelligence**: Rules prefixed with `(Arcanum-Sec)` leverage the Arcanum-Sec Prompt Injection Taxonomy or `sec-context` anti-pattern library for high-fidelity detection.

**OWASP reference:** [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

---

*Last updated: May 2026*

**[⬅ Back to Compliance index](index.md)** · **[🛡️ Full OWASP ASI Coverage](owasp-agentic-top10-architecture.md)**
