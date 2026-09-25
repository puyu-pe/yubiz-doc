---
name: yubiz-source-backed-ficha
description: "Trigger: Yubiz ficha, source-backed documentation, sales guide refresh. Review and maintain public-safe operational fichas."
license: Apache-2.0
metadata:
  author: "puyu-pe"
  version: "1.0"
---

## Activation Contract

Load when creating or refreshing a Yubiz source-backed operational ficha.

## Hard Rules

- Review the pinned source revision without mutating source repositories.
- Admit a ficha only with a declared menu and a direct or indirect browser UI path.
- Do not treat App APIs as UI authority unless the browser path invokes them.
- Keep internal paths, ranges, and traces in private Engram evidence.
- Keep source, runtime, and deployed uncertainty in metadata and private Engram evidence; never expose it in a ficha.

## Decision Gates

| Evidence state | Action |
|---|---|
| Declared menu plus direct/indirect browser UI path | Write neutral Spanish guidance. |
| Historical menu only or no declared UI path | Exclude it from this documentation scope without calling the feature disabled. |
| Label, entitlement, or outcome is unobserved | Record the uncertainty in metadata and private evidence; keep reader guidance neutral. |
| Source revision changes | Refresh inventory and checkpoint metadata. |

## Execution Steps

1. Confirm the pinned source revision and inspect the declared browser-facing path.
2. Record detailed trace and uncertainties in private Engram evidence.
3. Write the ficha with objective, preconditions, steps, result, and operational caveats only.
4. Treat permissions, users, roles, and grants as neither an admission requirement nor an analysis step; record access variation in metadata and private evidence. Update the v2 inventory, capability dispositions, and checkpoint together;
   retain only opaque IDs in public capability metadata.
5. Keep `scope_state: slice_pending` and source/runtime/deployed states independent
   until private evidence and final reconciliation authorize completion.
6. Run the portable validator, fixture regression, and strict local documentation
   build.

## Manual Sync

1. Resolve `YUBIZ_SOURCE_DIR` before source work; its read-only default is `../yubiz`. Read `documentation/source-checkpoint.yml`, its existing owner exclusions, and the current catalog before assessing the range.
2. Resolve the immutable target from the declared `source_sync.source_branch`. Read `VERSION` with `git show <target>:VERSION`, never from the source worktree. If it is absent, record `source_version: null` with a brief reason; commit authority still applies.
3. Compare `source_sync.completed.source_commit` to the target with `git diff --name-status --find-renames <base> <target>`. If no completed commit exists, use only the approved bootstrap base and state that adoption is scoped and incremental, not a full historical audit.
4. Classify every added, changed, renamed, and deleted path as documented, no documentation impact, excluded, or pending. Check an exclusion against the target hunk and its declared scope; path hints are never file-wide exclusions. Do not infer new exclusions.
5. Use CodeGraph only when it matches the immutable target; otherwise inspect target bytes with `git show <target>:<path>`. Search similar fichas before creating one. A current declared menu plus a direct or indirect browser UI path admits a ficha; old or legacy menu presence alone does not. Do not perform role or grants analysis.
6. Keep audit paths and detailed evidence private in Engram. The public checkpoint contains only counts, safe reasons, and opaque IDs.
7. Do not advance `completed`, top-level `source_revision`, or inventory pins while any path is pending. After the full range is resolved and current validation passes, update those fields deliberately. `scope_complete` covers documentation content only, not Git-range completion, runtime, or deployment.
8. Never fetch, checkout, mutate, or otherwise change the Yubiz source. Do not claim remote freshness or deployment synchronization without separate evidence.

## Output Contract

Return the source revision, reviewed scope, public files changed, metadata/private-evidence
uncertainties, and strict-build result.

## References

- `../../../../documentation/source-checkpoint.yml` — public review checkpoint.
- `../../../../documentation/inventory.yml` — public ficha inventory.
- `../../../../documentation/capability-dispositions.yml` — public-safe capability ledger.
- `../../../../scripts/validate_manual.py` — portable structural/privacy validator.
