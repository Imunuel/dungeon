from celery import shared_task

from users import services


@shared_task
def init_task():
    data = services.test_service()
    if data:
        return data["name"]
    return None


@shared_task
def another_task():
    init_task.delay()
