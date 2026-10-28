"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Display the emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze the supplied text and return a readable result."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return (
            "Emotion detection service is currently unavailable. "
            "Please try again later.",
            502,
        )

    dominant = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {dominant}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
