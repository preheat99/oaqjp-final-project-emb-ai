import requests, json # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers
    return response.json()

required_response = emotion_detector('I love this new technology')
emotion_from_response = required_response['emotionPredictions'][0]['emotion']
dominant_emotion = 'anger'
for emotion in emotion_from_response.keys():
    if emotion_from_response[emotion] > emotion_from_response[dominant_emotion]:
        dominant_emotion = emotion

emotion_from_response['dominant_emotion'] = dominant_emotion
print(emotion_from_response)
