import time
from typing import Any, Dict, List

class Telemetry:
    def __init__(self):
        self._events: List[Dict[str, Any]] = []

    def log(self, source: str, message: str, payload: Dict[str, Any] = None):
        entry = {
            "ts": time.time(),
            "source": source,
            "message": message,
            "payload": payload or {},
        }
        self._events.append(entry)
        print(f"[TELEMETRY] {source}: {message}")
    
    def events(self):
        return list(self._events)
