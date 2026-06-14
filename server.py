from flask import Flask, render_template, requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detection()
    text_to_analyse = requests.args.get('textToAnalyse')
    emotion_detector(text_to_analyse)