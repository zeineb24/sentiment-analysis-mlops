# test_predict.py
import unittest
from predict import app

class PredictTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_prediction_positive(self):
        response = self.app.post('/predict', json={"review": "This movie is great!"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json)

    def test_prediction_negative(self):
        response = self.app.post('/predict', json={"review": "I hated this movie"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json)

if __name__ == '__main__':
    unittest.main()
