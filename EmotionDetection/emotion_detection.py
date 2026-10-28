"""Emotion detection using the IBM Watson NLP service."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return None

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            URL, headers=HEADERS, json=payload, timeout=30
        )
        if response.status_code == 400:
            return None
        response.raise_for_status()
        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]

        scores = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
        }
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return None
