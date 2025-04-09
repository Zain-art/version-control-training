# test_app.py
import unittest
from app import app  # Import the Flask app from app.py

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client before each test
        self.client = app.test_client()
        self.client.testing = True  # Enables exception propagation

    def test_hello_world(self):
        # Send a GET request to the root URL
        response = self.client.get("/")
        
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Assert the response data is exactly "hello world"
        self.assertEqual(response.data.decode(), "hello world")

if __name__ == "__main__":
    unittest.main()
