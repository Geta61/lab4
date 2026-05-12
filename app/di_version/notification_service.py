class NotificationService:

    def __init__(self, config, auditor):
        self.config = config
        self.auditor = auditor

    def send(self, user, message):

        channel = self.config.provider_type

        result = f"Sent via {channel}"

        if self.config.audit_enabled:
            self.auditor.record(user, channel, result)

        return result
