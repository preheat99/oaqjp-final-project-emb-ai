from emotion_detection import emotion_detector


if __name__ == "__main__":
    test_text = "I love this new technology"
    result = emotion_detector(test_text)
    print(result)