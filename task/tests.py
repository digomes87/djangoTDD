from django.test import TestCase
from task.models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='My task title')

    def test_task_model_exists(self):
        tasks = Task.objects.count() # type ignore

        self.assertEqual(tasks, 1)

    def test_model_has_string_representation(self):
        task = Task(title='My task title')
        self.assertEqual(str(task), 'My task title')


class IndexPageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='My task title')

    def test_index_page_returns_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'task/index.html')
        self.assertEqual(response.status_code, 200)

    def test_index_page_has_tasks(self):
        response = self.client.get('/')

        self.assertContains(response, self.task.title)
