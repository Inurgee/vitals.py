from ..core.event_bus import EventBus
from .coupling_layer import DKCECoupler

class DKCEEngine:
    def __init__(self):
        self.bus = EventBus()
        self.coupler = DKCECoupler(self.bus)

    def run_pulses(self, vitals_sequence):
        print("[DKCE] Engine starting.")
        for vitals in vitals_sequence:
            print(f"[DKCE] Pulse: {vitals}")
            self.coupler.pulse(vitals)
        print("[DKCE] Engine complete.")
