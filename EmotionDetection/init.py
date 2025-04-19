from emotion_detection import emotion_detector


if __name__ == "__main__":
    test_text = "I hate working long hours."
    result = emotion_detector(test_text)
    print(result)