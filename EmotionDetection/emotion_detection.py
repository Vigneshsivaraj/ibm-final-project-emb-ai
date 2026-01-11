import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL,headers = headers,json = input_json)
    
    output_format = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    dominant_emotion = None

    if(response and response.text):
        data = json.loads(response.text)
        data = data["emotionPredictions"]
        if(data and data[0]):
            emotions = data[0]['emotion']
            for key in emotions.keys():
                output_format[key] = emotions[key]     
                if(dominant_emotion is None or emotions[key] > output_format[dominant_emotion]):
                    dominant_emotion = key

    output_format["dominant_emotion"] = dominant_emotion
    return output_format
