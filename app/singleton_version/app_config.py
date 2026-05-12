import threading
import os


class AppConfig:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, provider_type: str, audit_enabled: bool):
        self.provider_type = provider_type
        self.audit_enabled = audit_enabled

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    provider = os.getenv("PROVIDER_TYPE", "email")
                    audit = os.getenv("AUDIT_ENABLED", "true") == "true"

                    cls._instance = cls(provider, audit)

        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None
