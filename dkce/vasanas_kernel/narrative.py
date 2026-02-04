from typing import Dict, Any

class NarrativeEngine:
    def __init__(self):
        self.current_story: str = "System booted."

    def update_from_state(self, state_name: str):
        self.current_story = f"Organism is now in {state_name}."
        print(f"[NARRATIVE] {self.current_story}")

    def integrate_endocrine_signal(self, signal: Dict[str, Any]):
        chem = signal.get("chemical")
        print(f"[NARRATIVE] Interpreting endocrine signal: {chem}")
