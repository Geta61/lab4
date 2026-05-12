class AppConfig:

    def __init__(self, provider_type: str, audit_enabled: bool):
        self.provider_type = provider_type
        self.audit_enabled = audit_enabled
