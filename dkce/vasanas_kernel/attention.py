from typing import Any

class AttentionSystem:
    def __init__(self):
        self.focus: Any = None

    def set_focus(self, obj: Any):
        self.focus = obj
        print(f"[ATTENTION] Focus set to: {obj}")
