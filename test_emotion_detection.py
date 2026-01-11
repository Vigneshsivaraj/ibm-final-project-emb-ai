from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_joy(self):
        input = "I am glad this happened"
        response = emotion_detector(input)
        self.assertEqual(response['dominant_emotion'], "joy")

    def test_emotion_detector_anger(self):
        input = "I am really mad about this"
        response = emotion_detector(input)
        self.assertEqual(response['dominant_emotion'], "anger")

    def test_emotion_detector_disgust(self):
        input = "I feel disgusted just hearing about this"
        response = emotion_detector(input)
        self.assertEqual(response['dominant_emotion'], "disgust")

    def test_emotion_detector_sadness(self):
        input = "I am so sad about this"
        response = emotion_detector(input)
        self.assertEqual(response['dominant_emotion'], "sadness")

    def test_emotion_detector_fear(self):
        input = "I am really afraid that this will happen"
        response = emotion_detector(input)
        self.assertEqual(response['dominant_emotion'], "fear")
