# 2026-05-26 — Policy CLI `matches` operator uses `re.search`

PR: jessburnett/agent-governance-toolkit#2 — branch `feat/asi-09-edu-safety-packs`
Commit: `fix(policies): use re.search in CLI condition matcher to mirror evaluator`
File: [agent_os/policies/cli.py](../../agent-governance-python/agent-os/src/agent_os/policies/cli.py)

## What changed and why

`_evaluate_condition` in the policy CLI implemented the `matches` operator with
`re.match`, which anchors the pattern at the start of the string. The runtime
`PolicyEvaluator` uses `re.search`, which matches anywhere in the string. The
two condition matchers therefore disagreed: a mid-string pattern (for example
the SSN `\b...\b` detector) matched at runtime but silently failed in the CLI.

The fix switches the CLI to `re.search` so the offline tool mirrors the live
evaluator exactly:

```python
if operator == "matches":
    # re.search (not re.match) to mirror the runtime PolicyEvaluator;
    # anchored patterns (^...$) still anchor, but mid-string patterns
    # like the SSN \b...\b regex now match as the evaluator intends.
    return bool(re.search(str(value), str(ctx_value)))
```

Anchored patterns (`^...$`) keep identical behavior; only mid-string patterns
change, and they change to agree with the evaluator that already ships.

## Threat model impact

This change **closes a detection gap**; it adds no new capability or power.

| Dimension | Direction |
|---|---|
| CLI / evaluator divergence | **Removed.** The CLI no longer under-matches `matches` conditions relative to the runtime evaluator. |
| Sensitive-data detection (e.g. SSN regex) | **Improved.** Mid-string detectors that previously passed silently in the CLI now flag, matching enforced runtime behavior. |
| New attack surface | **None.** Single-line change to an existing operator; no new inputs, deps, or execution paths. |
| Risk of over-matching | **Low.** Behavior is now identical to the evaluator that policies are already authored against; anchored patterns are unaffected. |

## Test coverage

- Existing policy-condition tests under
  [agent_os/policies](../../agent-governance-python/agent-os/src/agent_os/policies)
  exercise the `matches` operator against both anchored and mid-string patterns.
- The change makes the CLI result equal the `PolicyEvaluator` result for the
  same condition and context, so evaluator parity tests cover the new behavior.
