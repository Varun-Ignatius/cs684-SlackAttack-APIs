import unittest
from app import app


class TestSignIn(unittest.TestCase):

    def test_sign_in_valid(self):
        with app.test_client() as client:
            response = client.get('/signIn/shreya121&Tintin@11')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['Code'], 200)
            self.assertEqual(data['Message'], 'Signed In Successfully')

    def test_sign_in_invalid(self):
        with app.test_client() as client:
            response = client.get('/signIn/shreya121&Tintin@12')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['Code'], 401)
            self.assertEqual(data['Message'], 'Invalid UserName or Password')


if __name__ == '__main__':
    unittest.main()
