from ..core.state_enum import SystemState
from ..core.event_bus import EventBus
from ..ojas_kernel.endocrine_bus import EndocrineSystem
from ..ojas_kernel.glymphatic import GlymphaticSystem
from ..ojas_kernel.homeostasis import Homeostasis
from ..ojas_kernel.spore_protocol import SporeProtocol
from ..vasanas_kernel.narrative import NarrativeEngine
from ..vasanas_kernel.vasana_graph import VasanaGraph
from ..vasanas_kernel.ritual_engine import RitualEngine

class DKCECoupler:
    def __init__(self, bus: EventBus):
        # Ojas side
        self.endocrine = EndocrineSystem(bus)
        self.glymphatic = GlymphaticSystem(self.endocrine)
        self.spore = SporeProtocol()
        self.homeostasis = Homeostasis(self.endocrine, self.glymphatic, self.spore)

        # Vasanas side
        self.narrative = NarrativeEngine()
        self.vasana_graph = VasanaGraph()
        self.ritual = RitualEngine()

        # Wiring
        bus.subscribe("endocrine_signal", self._on_endocrine_signal)

        self._last_state = self.homeostasis.current_state

    def pulse(self, vitals):
        self.homeostasis.tick(vitals)
        if self.homeostasis.current_state != self._last_state:
            self.ritual.on_state_transition(self._last_state, self.homeostasis.current_state)
            self.narrative.update_from_state(self.homeostasis.current_state.name)
            self._last_state = self.homeostasis.current_state

    def _on_endocrine_signal(self, signal):
        self.narrative.integrate_endocrine_signal(signal)
        self.vasana_graph.reinforce(signal.get("chemical", "unknown"))
