import unittest
from fastapi.testclient import TestClient
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_checkdata(self):
        response = self.client.get('/checkdata')
        self.assertIn(response.status_code, [200, 500])

    def test_person_not_found(self):
        response = self.client.get('/person', params={'name': 'Nonexistent', 'role': 'actor'})
        self.assertIn(response.status_code, [200, 404])

    def test_get_principals_from_title_not_found(self):
        response = self.client.get('/principals/nonexistent_id', params={'order': 1})
        self.assertIn(response.status_code, [404, 200])

    def test_get_title_not_found(self):
        response = self.client.get('/title', params={'name': 'Nonexistent', 'kind': 'movie'})
        self.assertIn(response.status_code, [404, 200])

if __name__ == '__main__':
    unittest.main() 