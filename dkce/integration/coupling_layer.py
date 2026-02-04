from typing import Dict, Any
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
    """
    The integration bridge of the Dual-Kernel Consciousness Engine.
    It synchronizes physiological states (Ojas) with cognitive narrative (Vasanas).
    """
    def __init__(self, bus: EventBus):
        # --- Ojas Kernel (Physiological Layer) ---
        self.bus = bus
        self.endocrine = EndocrineSystem(bus)
        self.glymphatic = GlymphaticSystem(self.endocrine)
        self.spore = SporeProtocol()
        self.homeostasis = Homeostasis(self.endocrine, self.glymphatic, self.spore)

        # --- Vasanas Kernel (Cognitive Layer) ---
        self.narrative = NarrativeEngine()
        self.vasana_graph = VasanaGraph()
        self.ritual = RitualEngine()

        # --- System Wiring ---
        # Listens for chemical changes to reinforce cognitive patterns
        self.bus.subscribe("endocrine_signal", self._on_endocrine_signal)
        self._last_state = self.homeostasis.current_state

    def pulse(self, vitals: Dict[str, Any]):
        """
        The Master System Heartbeat.
        Executes the Homeostatic Mirror -> Endocrine Brake -> Cognitive Sync loop.
        """
        # 1. Homeostatic Mirror: Analyze vitals and trigger secretions
        self.homeostasis.tick(vitals)
        
        # 3. Cognitive Synchronization: Update Narrative and Rituals on state change
        current_state = self.homeostasis.current_state
        if current_state != self._last_state:
            self.ritual.on_state_transition(self._last_state, current_state)
            self.narrative.update_from_state(current_state.name)
            self._last_state = current_state

    def _on_endocrine_signal(self, signal: Dict[str, Any]):
        """
        The bridge: Physiological signals are interpreted as cognitive focus.
        """
        chem = signal.get("chemical", "unknown")
        
        # Log the signal into the narrative engine
        self.narrative.integrate_endocrine_signal(signal)
        
        # Reinforce the cognitive graph based on the active chemical
        self.vasana_graph.reinforce(pattern=chem, delta=0.1)

