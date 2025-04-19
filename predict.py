from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("review", "")
    X = vectorizer.transform([review])
    prediction = model.predict(X)[0]
    return jsonify({"prediction": prediction})



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # ✅ Dynamic port binding for Cloud Run
    app.run(host="0.0.0.0", port=port)


