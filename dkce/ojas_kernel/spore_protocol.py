import json
import lzma
import hashlib
from typing import Dict, Any, List

class SporeProtocol:
    def __init__(self, physician_id: str = "MD-01"):
        self.physician_id = physician_id
        self.wisdom_buffer: Dict[str, Dict[str, Any]] = {}

    def myelinate_wisdom(self, path: str, efficiency: float):
        self.wisdom_buffer[path] = {"efficiency": efficiency, "status": "myelinated"}
        print(f"[SPORE] Myelinated path: {path} ({efficiency:.2f})")

    def generate_spore(self, immune_signatures: List[str], filename: str = "dkce.spore"):
        manifest = {
            "version": "1.0-dkce",
            "physician_record": self.physician_id,
            "myelinated_wisdom": self.wisdom_buffer,
            "immune_signatures": immune_signatures,
        }
        raw = json.dumps(manifest).encode("utf-8")
        compressed = lzma.compress(raw)
        with open(filename, "wb") as f:
            f.write(compressed)
        digest = hashlib.sha256(compressed).hexdigest()[:12]
        print(f"[SPORE] Spore ready: {filename} (SHA256:{digest})")


