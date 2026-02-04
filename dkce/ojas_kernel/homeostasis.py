class Homeostasis:
    def __init__(self, endocrine, glymphatic, spore):
        self.endocrine = endocrine
        self.glymphatic = glymphatic
        self.spore = spore
        self.current_state = SystemState.CALM

    def tick(self, vitals: Dict[str, float]):
        cortisol = self.endocrine.field.get("CORT", 0.0)
        gaba = self.endocrine.field.get("GABA", 0.0)

        glucose = vitals.get("glucose", 100.0)
        temp = vitals.get("temp", 37.0)
        threat = vitals.get("threat", 0.0)

        # cortisol makes threat "feel" higher, GABA dampens it
        effective_threat = max(0.0, min(1.0, threat + 0.5 * cortisol - 0.5 * gaba))

        if effective_threat > 0.8 or temp > 85.0:
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
        self.endocrine.decay()

