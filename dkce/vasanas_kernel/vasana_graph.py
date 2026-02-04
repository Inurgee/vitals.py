from typing import Dict, Any

class VasanaGraph:
    def __init__(self):
        self.tendencies: Dict[str, float] = {}

    def reinforce(self, pattern: str, delta: float = 0.1):
        self.tendencies[pattern] = self.tendencies.get(pattern, 0.0) + delta
        print(f"[VASANA] Reinforced {pattern} → {self.tendencies[pattern]:.2f}")
