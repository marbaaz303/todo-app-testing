import unittest
import json
import todo_app  # updated import based on your filename

class EnhancedTodoAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = todo_app.app.test_client()
        with open(todo_app.DATA_FILE, 'w') as f:
            json.dump([], f)

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Smart To-Do List', response.data)

    def test_add_task_with_priority_and_due(self):
        response = self.client.post('/add', data={
            'task': 'Test Task',
            'priority': 'High',
            'due': '2025-05-01'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)
        self.assertIn(b'High', response.data)
        self.assertIn(b'2025-05-01', response.data)

    def test_delete_task(self):
        self.client.post('/add', data={'task': 'Delete Me', 'priority': 'Low'}, follow_redirects=True)
        response = self.client.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Delete Me', response.data)

    def test_bva_empty_task(self):
        response = self.client.post('/add', data={'task': '', 'priority': 'Low'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_ecp_invalid_delete(self):
        response = self.client.get('/delete/999', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()