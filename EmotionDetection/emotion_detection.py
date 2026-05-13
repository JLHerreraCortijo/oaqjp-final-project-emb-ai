import requests
import json

def emotion_detector(text_to_analyze):
    """
    Runs emotion detection
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url,headers = headers, json = input_obj)
    
    emotions = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    
    highest_score = 0
    dominant_emotion = None

    for emotion, score in emotions.items():
        if score > highest_score:
            dominant_emotion = emotion
            highest_score = score


    emotions["dominant_emotion"] = dominant_emotion
    return emotions