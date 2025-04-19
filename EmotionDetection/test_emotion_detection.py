import unittest
from emotion_detection import emotion_detector  # Import the function from your main script

class TestEmotionPredictor(unittest.TestCase):

    def test_joy_emotion(self):
        test_text = "I feel so happy and full of energy today!"
        result = emotion_detector(test_text)
        # Check if the joy emotion is present and greater than a certain threshold
        self.assertGreater(float(result['joy'].replace('%', '')), 0)

    def test_sadness_emotion(self):
        test_text = "I am feeling really down and depressed."
        result = emotion_detector(test_text)
        # Check if the sadness emotion is present and greater than a certain threshold
        self.assertGreater(float(result['sadness'].replace('%', '')), 0)

    def test_anger_emotion(self):
        test_text = "I am so angry right now!"
        result = emotion_detector(test_text)
        # Check if the anger emotion is present and greater than a certain threshold
        self.assertGreater(float(result['anger'].replace('%', '')), 0)

    def test_empty_text(self):
        test_text = ""
        result = emotion_detector(test_text)
        # Ensure that no emotion is detected for an empty string (can be handled as per the function behavior)
        self.assertEqual(result, {'joy': '0.00%', 'anger': '0.00%', 'fear': '0.00%', 'sadness': '0.00%', 'disgust': '0.00%'})

if __name__ == "__main__":
    unittest.main()