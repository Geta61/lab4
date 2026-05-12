from app.di_version.config import AppConfig
from app.di_version.audit import NotificationAuditor
from app.di_version.notification_service import NotificationService


def test_send_notification():

    config = AppConfig("email", True)

    auditor = NotificationAuditor()

    service = NotificationService(config, auditor)

    result = service.send("u1", "hello")

    assert result == "Sent via email"

    assert len(auditor.records) == 1
