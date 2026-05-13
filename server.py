from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def analize_emotion():
    """
    emotionDetector route
    """
    text = request.args.get("textToAnalyze")
    
    emotions =  emotion_detector(text)
    if emotions["dominant_emotion"] is None:
        return "<b>Invelid text! Please try again!"
    result = f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']}, 'sadness': {emotions['sadness']}. The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
    return result

@app.route("/")
def root():
    """
    root path
    """

    return(render_template("index.html"))

app.run()