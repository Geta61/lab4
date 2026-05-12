from app.singleton_version.app_config import AppConfig
from app.singleton_version.audit import NotificationAuditor


class NotificationService:

    def send(self, user, message):
        config = AppConfig.get_instance()

        channel = config.provider_type

        result = f"Sent via {channel}"

        if config.audit_enabled:
            auditor = NotificationAuditor.get_instance()
            auditor.record(user, channel, result)

        return result
