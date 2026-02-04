class EndocrineSystem:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.field: Dict[str, float] = {}  # chemical → intensity

    def secrete(self, chemical: str, intensity: float, origin: str = "ojas_kernel"):
        self.field[chemical] = self.field.get(chemical, 0.0) + intensity
        signal = {
            "chemical": chemical,
            "intensity": intensity,
            "origin": origin,
        }
        print(f"[ENDOCRINE] {chemical} @ {intensity*100:.0f}% from {origin}")
        self.bus.publish("endocrine_signal", signal)

    def decay(self, rate: float = 0.1):
        """Simple exponential-ish decay of hormone levels."""
        for chem in list(self.field.keys()):
            self.field[chem] *= (1.0 - rate)
            if self.field[chem] < 0.01:
                del self.field[chem]

