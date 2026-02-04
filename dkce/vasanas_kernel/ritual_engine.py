from ..core.state_enum import SystemState

class RitualEngine:
    def on_state_transition(self, old: SystemState, new: SystemState):
        print(f"[RITUAL] Marking transition {old.name} → {new.name}")
