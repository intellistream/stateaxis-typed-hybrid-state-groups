"""Typed hybrid state-group activation contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass

MOD_ID = "org.vllm-hust.stateaxis-typed-hybrid-state-groups"


@dataclass(frozen=True, slots=True)
class TypedHybridStateGroupsConfig:
    """Exact bounded Qwen3.8 recurrent/full-KV authority contract."""

    enabled: bool = True
    model_family: str = "qwen38"
    wire_schema_version: int = 1
    plan_identity_sha256: str = "a5" * 32
    recurrent_groups: int = 1
    full_kv_groups: int = 1
    recurrent_layer_count: int = 48
    full_kv_layer_count: int = 16
    recurrent_bytes_per_state: int = 38_486_016
    full_kv_bytes_per_token: int = 16_384
    atomic_cohort_publication: bool = True
    joint_admission: bool = True
    generation_qualified_release: bool = True
    recurrent_copy_on_write: bool = True
    immutable_kv_sharing: bool = True
    snapshot_capture_required: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        expected = {
            "enabled": True,
            "model_family": "qwen38",
            "wire_schema_version": 1,
            "plan_identity_sha256": "a5" * 32,
            "recurrent_groups": 1,
            "full_kv_groups": 1,
            "recurrent_layer_count": 48,
            "full_kv_layer_count": 16,
            "recurrent_bytes_per_state": 38_486_016,
            "full_kv_bytes_per_token": 16_384,
            "atomic_cohort_publication": True,
            "joint_admission": True,
            "generation_qualified_release": True,
            "recurrent_copy_on_write": True,
            "immutable_kv_sharing": True,
            "snapshot_capture_required": True,
            "fail_closed": True,
        }
        if asdict(self) != expected:
            raise ValueError("typed hybrid state groups require the reviewed contract")


def typed_hybrid_state_groups() -> TypedHybridStateGroupsConfig:
    return TypedHybridStateGroupsConfig()


__all__ = ["MOD_ID", "TypedHybridStateGroupsConfig", "typed_hybrid_state_groups"]
