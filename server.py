"""Flask server for emotion detection application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["get"])
def emotion_detector_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get("textToAnalyze")
    output_result = emotion_detector(text_to_analyze)
    dominant_emotion = output_result["dominant_emotion"]
    if dominant_emotion is None:
        return " Invalid text! Please try again!."
    output_result.pop("dominant_emotion")
    result = (
        f"For the given statement, the system response is {output_result}. "
        f"The dominant emotion is {dominant_emotion}"
    )
    return result

@app.route("/")
def load_index():
    """Render the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
