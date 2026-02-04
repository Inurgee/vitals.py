from typing import Dict, Any
from ..core.event_bus import EventBus

class EndocrineSystem:
    def __init__(self, bus: EventBus):
        self.bus = bus

    def secrete(self, chemical: str, intensity: float, origin: str = "ojas_kernel"):
        signal = {
            "chemical": chemical,
            "intensity": intensity,
            "origin": origin,
        }
        print(f"[ENDOCRINE] {chemical} @ {intensity*100:.0f}% from {origin}")
        self.bus.publish("endocrine_signal", signal)
