from flask import Flask, render_template, request
import os
from src.predict import predict_audio

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "audio" not in request.files:
        return render_template("index.html",
                               prediction="No file selected")

    file = request.files["audio"]

    if file.filename == "":
        return render_template("index.html",
                               prediction="Please upload an audio file.")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    result, confidence = predict_audio(filepath)

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        filename=file.filename
    )


if __name__ == "__main__":
    app.run(debug=True)
