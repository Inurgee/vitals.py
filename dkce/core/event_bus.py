from typing import Callable, Dict, List, Any

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}

    def subscribe(self, topic: str, handler: Callable[[Dict[str, Any]], None]):
        self._subscribers.setdefault(topic, []).append(handler)

    def publish(self, topic: str, payload: Dict[str, Any]):
        for handler in self._subscribers.get(topic, []):
            try:
                handler(payload)
            except Exception as e:
                print(f"[EventBus] handler error for topic={topic}: {e}")
