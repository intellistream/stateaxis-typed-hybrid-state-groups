# Current HyStateBench execution blocker

This is a current, reproducible blocker record, not a benchmark result. No NPU
context was opened and no performance number is inferred.

## Required formal cell

The checked-in HyStateBench 1.2 contract requires Qwen3.8-27B BF16 in graph
mode, TP4PP1 on physical NPU4–7, 308 cases and at least three fresh paired
service lifecycles for unchanged `stateaxis-base1` and the candidate. Reducing
the topology to the two visible devices would change the preregistered workload
and is therefore forbidden.

## Current audit

- StateAxis: `16f6c9178c4a7820b4175e34829fa357e6c9ba80`, clean.
- MOD repository parent: `8e962e7e98ab75c0baa0521ba05cb793aa4b25c9`.
- Available hardware: two idle Ascend 910B2 devices, physical NPU4 and NPU5.
- Device nodes: `/dev/davinci4`, `/dev/davinci5` and manager only.
- Qwen3.8-27B model, ShareGPT dataset and frozen prompt selection exist.
- Neither `sudo` nor `docker` exists in this container, while the frozen
  provider requires an identity-qualified immutable runtime image.

Current plan expansion was attempted with the exact checked-in contract and
prompt selection. It exited 2 before device admission because
`runtime-integrations/candidate.json` still binds vLLM tree `2464899...`, while
current `main` contains tree `3a401e7...`. The vLLM-Ascend trees likewise differ
(`1486dd9...` versus `e9d4403...`). This is an identity failure, not an NPU
failure and not a performance result.

Two four-device admission-ready receipts from 2026-09-21 are preserved under
`/data`, but they bind StateAxis dev15 and an authorization that expired that
day. No formal HyStateBench campaign/result directory exists. Those receipts
cannot be reused or reported as performance evidence.

## Reproduce the current plan failure

```bash
python3 /root/stateaxis/scripts/expand_hystatebench.py \
  --contract /root/stateaxis/benchmarks/hystatebench_v1.json \
  --prompt-selection \
    /data/statecentric-builds/hystatebench-prompts-sharegpt-v1-20260921-r001/selection.json \
  --repo-root /root/stateaxis \
  --integration-index /root/stateaxis/runtime-integrations/candidate.json \
  --output \
    /data/statecentric-builds/hystatebench-plan-stateaxis-main-20261013-r002.json
```

Expected current exit: 2 with
`checked-out owned runtime tree differs: vllm`.

## Unblock conditions

1. Publish a current integration record binding both owned runtime trees.
2. Build immutable base1 and candidate images with matching tree labels.
3. Run in an environment exposing idle physical NPU4–7 with a fresh plan-bound
   authorization.
4. Execute all three paired lifecycles and retain correctness, activation,
   ownership cleanup, capacity, HBM, latency and throughput evidence.

Until then the MOD remains performance-unqualified. The absence of a result is
now explicit and reproducible instead of being represented by an empty field.
