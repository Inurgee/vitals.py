class EndocrineSystem:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.field: Dict[str, float] = {} # Your first code's logic
        self.decay_rate = 0.1

    def secrete(self, chemical: str, intensity: float, origin: str = "ojas_kernel"):
        # Add to existing levels (The "Gas")
        self.field[chemical] = self.field.get(chemical, 0.0) + intensity
        self.field[chemical] = min(self.field[chemical], 1.0) # Cap at 100%

    def process_decay(self):
        """Your 'Brake' logic integrated into the tick."""
        for chem in list(self.field.keys()):
            self.field[chem] *= (1.0 - self.decay_rate)
            
            # Publish the state so Vasanas/Narrative can 'feel' the fade
            self.bus.publish("endocrine_signal", {
                "chemical": chem, 
                "intensity": self.field[chem],
                "origin": "decay_cycle"
            })

            if self.field[chem] < 0.01:
                del self.field[chem]

            

