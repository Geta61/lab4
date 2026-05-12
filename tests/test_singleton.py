from app.singleton_version.audit import NotificationAuditor


def test_audit_add_record():
    auditor = NotificationAuditor.get_instance()

    auditor.record("u1", "email", "ok")

    assert len(auditor.records) == 1


def test_audit_should_be_empty():
    auditor = NotificationAuditor.get_instance()

    assert len(auditor.records) == 0
