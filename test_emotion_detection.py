import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_successful_emotion_detection(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.05,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.85,
                        "sadness": 0.05
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy today")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.85)

    def test_blank_input(self):
        self.assertIsNone(emotion_detector(""))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("test text")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
