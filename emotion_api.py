from flask import Flask, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "🎉 API تعمل بنجاح! استخدم /analyze مع صورة مشفرة Base64."

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    data = request.json
    img_data = base64.b64decode(data['image'])
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
    emotion_result = {k: float(v) for k, v in result[0]['emotion'].items()}
    return jsonify(emotion_result)

import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
