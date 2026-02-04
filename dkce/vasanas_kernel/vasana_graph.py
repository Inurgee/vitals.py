class VasanaGraph:
    def __init__(self):
        self.tendencies: Dict[str, float] = {}

    def reinforce(self, pattern: str, delta: float = 0.1):
        self.tendencies[pattern] = self.tendencies.get(pattern, 0.0) + delta
        print(f"[VASANA] Reinforced {pattern} → {self.tendencies[pattern]:.2f}")

    def bias_actions(self, actions: Dict[str, float]) -> Dict[str, float]:
        """
        Modulate action intensities based on tendencies.

        Example:
            - High CORT vasana → more 'avoid' / 'rest'
            - High GABA vasana → more 'explore'
        """
        cort = self.tendencies.get("CORT", 0.0)
        gaba = self.tendencies.get("GABA", 0.0)

        actions = dict(actions)
        actions["rest"] += 0.2 * cort
        actions["expose_threat"] -= 0.2 * cort
        actions["explore"] += 0.2 * gaba

        return actions
