import threading

from app.singleton_version.app_config import AppConfig


instances = []


def create_instance():
    instances.append(AppConfig.get_instance())


def test_single_instance_created():

    threads = []

    for _ in range(10):
        t = threading.Thread(target=create_instance)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    first = instances[0]

    assert all(obj is first for obj in instances)
