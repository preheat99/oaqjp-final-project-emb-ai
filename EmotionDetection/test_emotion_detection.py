import unittest
from emotion_detection import emotion_detector  # Import the function from your main script

class TestEmotionPredictor(unittest.TestCase):

    def test_joy_emotion(self):
        test_text = "I am glad this happened"
        result = emotion_detector(test_text)
        print(result)
        # Check if the joy emotion is present and greater than a certain threshold
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        test_text = "I am really mad about this"
        result = emotion_detector(test_text)
        # Check if the sadness emotion is present and greater than a certain threshold
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        test_text = "I feel disgusted just hearing about this"
        result = emotion_detector(test_text)
        # Check if the anger emotion is present and greater than a certain threshold
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        test_text = "I am so sad about this"
        result = emotion_detector(test_text)
        # Check if the anger emotion is present and greater than a certain threshold
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        test_text = "I am really afraid that this will happen"
        result = emotion_detector(test_text)
        # Check if the anger emotion is present and greater than a certain threshold
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()