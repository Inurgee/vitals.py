from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Config:
    logging: Dict[str, Any] = None
    runtime: Dict[str, Any] = None

    def as_dict(self):
        return {
            "logging": self.logging or {},
            "runtime": self.runtime or {},
        }
