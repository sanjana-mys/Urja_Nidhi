from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np
import os

CWD = os.path.dirname(__file__)
app = Flask(__name__, template_folder=os.path.join(CWD, 'templates'))
CORS(app)

# Load model once when server starts
model_path = os.path.join(CWD, "urja_nidhi_ensemble_model.pkl")
try:
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route("/")
def home():
    return render_template("urja-nidhi-dashboard.html")

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Backend is running",
        "model_loaded": model is not None
    })

@app.route("/api/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        
        prediction = model.predict(features)
        
        return jsonify({
            "prediction": float(prediction[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("Starting URJA NIDHI Backend Server...")
    print("Frontend: http://localhost:5000/")
    print("API Health: http://localhost:5000/api/health")
    app.run(debug=True, host="0.0.0.0", port=5000)
