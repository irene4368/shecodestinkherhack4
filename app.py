import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Flask Setup
# ----------------------------
app = Flask(__name__, template_folder='.')
CORS(app)

# ----------------------------
# Firebase Setup
# ----------------------------
firebase_creds = os.getenv("FIREBASE_CREDENTIALS")
print(f"Firebase credentials loaded: {firebase_creds is not None}")
if firebase_creds:
    cred_dict = json.loads(firebase_creds)
    cred = credentials.Certificate(cred_dict)
else:
    raise ValueError("FIREBASE_CREDENTIALS environment variable not set")

firebase_admin.initialize_app(cred)
db = firestore.client()


# ----------------------------
# Home Route (Frontend)
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")
# ----------------------------
# Add Case API
# ----------------------------
@app.route("/add-case", methods=["POST"])
def add_case():
    try:
        data = request.json

        case_data = {
            "officerName": data.get("officerName"),
            "designation": data.get("designation"),
            "code": data.get("code"),
            "mobile": data.get("mobile"),
            "missingName": data.get("missingName"),
            "missingAge": data.get("missingAge"),
        }

        db.collection("cases").add(case_data)

        return jsonify({"message": "Case saved successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ----------------------------
# Get Cases API
# ----------------------------
@app.route("/get-cases", methods=["GET"])
def get_cases():
    try:
        cases = db.collection("cases").stream()
        case_list = []

        for case in cases:
            case_data = case.to_dict()
            case_data["id"] = case.id
            case_list.append(case_data)

        return jsonify(case_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)