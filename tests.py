import warnings
from dock.main import app
warnings.filterwarnings("ignore")
import unittest
import logging
import time
from detoxify import Detoxify

# Use log instead of print
logger = logging.getLogger()
logger.setLevel(logging.INFO)

CLASSES = [
    "toxicity",
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]


class TestApi(unittest.TestCase):

    URL = "http://localhost:5000/post_text"

    def test_server_is_up(self):
        tester=app.test_client(self)
        response = tester.get("/test_text")
        statuscode=response.status_code
        self.assertEqual(statuscode,200)

   

    def test_original(self):
        model = Detoxify("original")
        results = model.predict(["shut up, you liar", "you look like Marilyn Monroe"])
        assert len(results) == 6
        assert all(cl in results for cl in CLASSES[:6])
        assert results["toxicity"][0] >= 0.7
        assert results["toxicity"][1] < 0.5

            
if __name__ == '__main__':
    unittest.main()