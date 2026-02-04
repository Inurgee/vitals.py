# core/metabolism.py
from dataclasses import dataclass

@dataclass
class MetabolicState:
    glucose: float = 100.0
    temp: float = 37.0
    threat: float = 0.0

    def step(self, actions: dict) -> None:
        """
        Advance internal vitals one timestep based on actions.

        Args:
            actions: Dict with optional keys like 'eat', 'rest', 'expose_threat'.
        """
        eat = actions.get("eat", 0.0)
        rest = actions.get("rest", 0.0)
        expose_threat = actions.get("expose_threat", 0.0)

        # crude but alive:
        self.glucose += 10.0 * eat - 2.0  # baseline burn
        self.glucose = max(self.glucose, 0.0)

        self.temp += 0.2 * expose_threat - 0.1 * rest
        self.threat += 0.3 * expose_threat - 0.2 * rest
        self.threat = max(0.0, min(1.0, self.threat))
