from flask import Flask, render_template, jsonify
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

r = sr.Recognizer()
engine = pyttsx3.init()

def recognize_speech():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            engine.say(text)
            engine.runAndWait()
            return text
    except sr.RequestError as e:
        return f"Error: {e}"
    except sr.UnknownValueError:
        return "Tidak dapat mengenali ucapan."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listen", methods=["GET"])
def listen():
    result = recognize_speech()
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
