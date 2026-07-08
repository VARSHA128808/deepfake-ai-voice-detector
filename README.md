🎙️ Deepfake AI Voice Detector

An AI-powered application that detects whether an uploaded voice sample is **Real** or **AI Generated** using Machine Learning and MFCC (Mel-Frequency Cepstral Coefficients) feature extraction. This project helps identify synthetic voices created using deepfake technology.

📖 Overview

Deepfake voice generation has become increasingly realistic, making it difficult to distinguish AI-generated speech from genuine human voices. This project analyzes audio signals, extracts MFCC features, and uses a Machine Learning model to classify audio as **Real** or **Fake**.

✨ Features

- 🎤 Upload voice/audio files
- 🔍 Audio preprocessing
- 🎵 MFCC feature extraction
- 🤖 Machine Learning-based classification
- 📊 Displays prediction result
- 💻 Simple and user-friendly interface


🛠️ Technologies Used

- Python
- Librosa
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Flask

---

## 📂 Project Structure


deepfake-ai-voice-detector/
│
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   └── predict.py
├── models/
│   └── model.pkl
├── screenshots/
└── dataset/
```

---

⚙️ Installation



cd deepfake-ai-voice-detector

pip install -r requirements.txt

python app.py
```

---

## 🔄 Workflow

1. Upload an audio file.
2. Preprocess the audio.
3. Extract MFCC features.
4. Feed features into the trained Machine Learning model.
5. Predict whether the voice is Real or AI Generated.
6. Display the prediction result.


 Future Enhancements

- Real-time microphone support
- Deep Learning model integration
- Mobile application
- Higher detection accuracy
- Cloud deployment



 📌 Skills Demonstrated

- Machine Learning
- Audio Signal Processing
- Feature Engineering
- Python Programming
- Model Training
- Flask Web Development

 Author

Varsha

B.Tech Computer Engineering Student

Passionate about Artificial Intelligence, Machine Learning, and Software Development.
