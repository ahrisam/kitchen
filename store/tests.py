from django.test import TestCase


class SmokeTest(TestCase):
    def test_root_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
