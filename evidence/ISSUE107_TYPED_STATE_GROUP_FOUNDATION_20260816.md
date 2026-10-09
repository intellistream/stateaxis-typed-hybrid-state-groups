# Issue #107 typed state-group coordinator foundation

> **Point-in-time closure report, not current repository status.** The
> repository-wide current classification is maintained in
> [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md); raw and historical
> conclusions remain append-only in [`RESULTS.md`](../../RESULTS.md).

## Decision

The independently reviewable foundation slice of #17 is accepted as a
default-off software capability. It does not establish real hybrid-model
serving, NPU correctness, HBM reduction, or performance.

Issue #17 combined two different dependency levels. The repository already had
a structural IR for full/SWA/MLA/indexer semantics, but real full-model hybrid
execution remains unavailable: MiniMax coverage is component/single-layer and
end-to-end TP/EP serving is tracked by #66. Closing #17 with CPU mocks would
therefore be false. #107 isolates the allocator and identity work that can be
proved without that runtime.

## Implemented contract

`StateGroupPlan::compile` consumes a validated `NativeModelIr` and emits an
ordered plan containing:

- stable group IDs and ordered layer membership;
- full-KV or block-aligned SWA-KV kind and growth rule;
- tensor semantic, dtype, storage scope and elements/bytes per token;
- block geometry, operator binding and conservative prefix policy; and
- a domain-separated SHA-256 identity over the complete ordered plan, including
  a separately domain-bound full source-IR SHA and total model layer count.

The compiler accepts only GQA full attention and block-aligned GQA SWA in this
foundation. MLA, sparse indexer, recurrent state, plan-dependent tensor size,
and unaligned SWA fail closed. A uniform Qwen-shaped IR produces one full-KV
group whose state bytes equal the pre-existing static calculation. Compilation
is explicit and does not mutate the Qwen execution config, state compatibility
identity, resident worker, or public protocol.

`StateGroupCoordinator` owns an independent pool, block reference table,
generation-checked state table and telemetry record per group, including
separate cancel and eviction reclaim counts. One shadow
transaction applies create, append, fork/COW, cancel and eviction to every required
group. The first operation error permanently poisons the transaction, so a
partial shadow cannot be committed after an ignored error. Commit verifies the
owner epoch, every pool invariant, and identical state/generation/token
publication across groups before replacing the owner.

SWA rollover removes expired blocks before allocating retained blocks, which
allows progress when a correctly sized window pool is full. Joint admission
uses the resulting net physical demand. Prefix reuse is the safe intersection
of group policies and returns zero when an SWA group is present.

## Verification

The focused suite covers:

- uniform single-group bytes and create/append/fork/COW/cancel/evict trace;
- stable full/SWA grouping and identity-bound descriptors;
- descriptor reorder/substitution and plan mutation rejection;
- group exhaustion with all-group rollback and poisoned-commit rejection;
- per-group joint admission and pool-full SWA rollover;
- independent shared-tail COW/refcounts in every group;
- bounded window retention and conservative prefix intersection;
- state-ID generation advance and stale-key rejection;
- stale transaction epoch rejection; and
- deterministic repeated create/append/fork/cancel/evict faults with zero final
  states and zero used blocks.

The exact offline command was:

```text
PATH=/home/shuhao/toolchain-scratch-v301-release-r02/imported/toolchain/bin:$PATH \
  cargo test --all-targets --offline
```

It passed 297 library tests, eight `native_state_engine` tests, the existing
binary-specific tests, and all zero-test binary targets. Formatting and
`git diff --check` also passed. No container or NPU was started.

## Claim boundary

The accepted claim is limited to identity-bound GQA full/SWA state planning and
an atomic software coordinator. The online Qwen worker still uses its existing
single `PagedKvAllocator`; no public wire field or production scheduler path
changed. Real hybrid checkpoint parity, typed operator views, MLA/indexer or
recurrent state, NPU HBM reduction and the 20% capacity target are not evidence
from #107 and remain part of #17 after #66 provides a runnable hybrid model.
