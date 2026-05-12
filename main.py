from app.di_version.config import AppConfig
from app.di_version.audit import NotificationAuditor
from app.di_version.notification_service import NotificationService


config = AppConfig(
    provider_type="telegram",
    audit_enabled=True
)

auditor = NotificationAuditor()

service = NotificationService(config, auditor)

service.send("student1", "Request approved")
