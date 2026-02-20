from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)

# Initialize Firebase
cred = credentials.Certificate("roadwatch-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/add-case", methods=["POST"])
def add_case():
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

    return jsonify({"message": "Case saved successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)