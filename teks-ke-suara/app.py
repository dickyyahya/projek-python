from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        tts = gTTS(text)
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join("static", filename)
        tts.save(filepath)
        return render_template("index.html", audio_file=filename)
    return render_template("index.html", audio_file=None)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
