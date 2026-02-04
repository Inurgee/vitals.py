import time
import random

class Chronos:
    def __init__(self, engine: DKCEEngine, tick_rate: float = 1.0):
        self.engine = engine
        self.tick_rate = tick_rate  # Seconds per pulse
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"[CHRONOS] Heartbeat started at {self.tick_rate}s interval.")
        
        while self.is_running:
            # 1. Generate/Fetch current "Vitals" (The variation)
            vitals = self._get_current_vitals()
            
            # 2. Trigger the Pulse
            self.engine.coupler.pulse(vitals)
            
            # 3. Rest until the next heartbeat
            time.sleep(self.tick_rate)

    def _get_current_vitals(self) -> Dict[str, float]:
        # Here we simulate real-time variation
        # In a real app, this would poll sensors or system resources
        return {
            "glucose": random.uniform(70, 110),
            "temp": random.uniform(36.5, 37.5),
            "threat": 0.1 if random.random() > 0.9 else 0.0
        }

    def stop(self):
        self.is_running = False
