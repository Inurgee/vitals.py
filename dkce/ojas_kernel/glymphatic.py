import time
from .endocrine_bus import EndocrineSystem

class GlymphaticSystem:
    def __init__(self, endocrine: EndocrineSystem):
        self.endocrine = endocrine
        self.digital_plaque: float = 0.0

    def accumulate_plaque(self, amount: float = 0.1):
        self.digital_plaque += amount
        print(f"[GLYMPHATIC] Plaque += {amount:.2f} -> {self.digital_plaque:.2f}")

    def flush(self):
        print("[GLYMPHATIC] Initiating REM-like flush...")
        # signal GABA release to the system
        self.endocrine.secrete("GABA", 1.0, origin="glymphatic")
        time.sleep(0.5)
        self.digital_plaque = 0.0
        print("[GLYMPHATIC] Flush complete. Plaque cleared.")
