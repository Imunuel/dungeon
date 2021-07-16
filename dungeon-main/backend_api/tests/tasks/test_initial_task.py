import pytest

from users.tasks import init_task, another_task

pytestmark = [pytest.mark.django_db]


@pytest.mark.slow
@pytest.mark.usefixtures('celery_session_app', 'celery_session_worker')
class TestTasks:

    def test_initial_task_running(self, get_data):
        init_task()  # act

        get_data.assert_called_once()

    def test_chained_tasks(self, mocker):
        mocked = mocker.patch('users.tasks.init_task.delay')

        another_task()  # act

        mocked.assert_called()
