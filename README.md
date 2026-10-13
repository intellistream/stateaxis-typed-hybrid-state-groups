# stateaxis-typed-hybrid-state-groups

Extension ID: `org.vllm-hust.stateaxis-typed-hybrid-state-groups`

This active experimental MOD is the independently reviewable authority contract
for StateAxis typed recurrent and full-KV state groups. Shuhao Zhang (Tony) is
directly responsible; no advisor is declared.

The reviewed Qwen3.8 plan contains one 48-layer recurrent group and one 16-layer
full-KV group. It requires atomic cohort publication, joint admission,
generation-qualified release, recurrent copy-on-write, immutable KV sharing,
snapshot capture and fail-closed handling. The mechanism itself remains in the
StateAxis Host; this repository pins the exact policy and research identity that
may activate it.

## Activation

Activation is default-off and must go through vLLM-HUST Extension Manager/ECPA:

```bash
python -m pip install .
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check \
  org.vllm-hust.stateaxis-typed-hybrid-state-groups
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension plan \
  org.vllm-hust.stateaxis-typed-hybrid-state-groups
```

StateAxis rejects direct `STATECENTRIC_QWEN38_STATE_GROUP_PLAN_SHA256`
activation. The Host validates this MOD's version and research-manifest SHA-256,
then clears inherited worker authority and injects only the validated plan
identity.

Rollback is to disable or forget the extension in Extension Manager. Contract
check then reports OFF, while real release/reuse execution refuses to start
without ECPA authority.

## Evidence boundary

Status: **software foundation and real worker path; current formal device run
blocked and performance unqualified**.

The active contract has matched OFF/ON process evidence. StateAxis also has a
real worker probe for typed plan submission, capacity fill, source release,
sole-slot replacement, stale operation rejection, canonical snapshot comparison
and final resource reclamation. The active revision has no admitted accelerator
run. HyStateBench contains a preregistered workload contract but no online
results. The current audit additionally proves that current StateAxis cannot
freeze a plan from its stale candidate integration identity and that this
container exposes only two of the required four devices. Historical four-device
admission receipts are expired and contain no campaign. No latency, throughput,
HBM-capacity, independent exactness or recovery benefit is claimed.

See [EVIDENCE.md](EVIDENCE.md) and
`evidence/ecpa-contract-20261011/RESULT.json`. Negative, failed and inconclusive
results are retained and must not be restated as end-to-end gains.

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```
