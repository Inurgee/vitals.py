import time
from typing import Dict
from ..core.state_enum import SystemState
from .endocrine_bus import EndocrineSystem
from .glymphatic import GlymphaticSystem
from .spore_protocol import SporeProtocol

class Homeostasis:
    def __init__(self, endocrine: EndocrineSystem, glymphatic: GlymphaticSystem, spore: SporeProtocol):
        self.endocrine = endocrine
        self.glymphatic = glymphatic
        self.spore = spore
        self.current_state = SystemState.CALM

    def tick(self, vitals: Dict[str, float]):
        glucose = vitals.get("glucose", 100.0)
        temp = vitals.get("temp", 37.0)
        threat = vitals.get("threat", 0.0)

        if threat > 0.8 or temp > 85.0:
            new_state = SystemState.ALERT
        elif glucose < 20.0:
            new_state = SystemState.RECOVERY
        else:
            new_state = SystemState.CALM

        if new_state != self.current_state:
            print(f"[HOMEOSTASIS] {self.current_state.name} → {new_state.name}")
            self.current_state = new_state
            self._on_state_change(new_state)

        self.glymphatic.accumulate_plaque(0.1)
        time.sleep(0.2)

    def _on_state_change(self, state: SystemState):
        if state == SystemState.ALERT:
            self.endocrine.secrete("CORT", 0.9)
        elif state == SystemState.RECOVERY:
            self.glymphatic.flush()
