# Emotion Detection Web Application

## Overview
This project analyzes text and identifies five emotions using the IBM Watson NLP Emotion Prediction service.

## Emotions Detected
- Anger
- Disgust
- Fear
- Joy
- Sadness

The dominant emotion is the emotion with the highest score returned by the service.

## Technologies
- Python
- Flask
- Requests
- HTML, CSS, and JavaScript
- IBM Watson NLP Emotion Prediction API
- Unittest
- Pylint

## Project Structure
```text
EmotionDetection/
  __init__.py
  emotion_detection.py
static/mywebscript.js
templates/index.html
test_emotion_detection.py
server.py
README.md
```

## Installation
Activate your Python virtual environment and install the required packages:
```bash
python -m pip install Flask requests pylint
```

## Run Tests
```bash
python -m unittest -v test_emotion_detection.py
```

## Start the Application
```bash
python server.py
```
Open http://127.0.0.1:5000 in your browser.

## Static Code Analysis
```bash
python -m pylint server.py
```

## Error Handling
The application handles blank input and HTTP 400 responses. If the external emotion detection service is unavailable, it displays an error instead of fabricated scores.

## Note
Live emotion detection requires a working connection to the IBM Watson NLP service. Unit tests use mocked responses and do not verify live service availability.
