from flask import Flask, jsonify, Response, make_response, request
import requests
import uuid
import base64
from bs4 import BeautifulSoup
import re
import html

app = Flask(__name__)

captcha = "https://services.gst.gov.in/services/captcha"

sessions = {}

@app.route("/getCaptcha", methods=["GET"])
def getCaptcha():
    try:
        session = requests.Session()
        id = str(uuid.uuid4())

        response = session.get(
            "https://services.gst.gov.in/services/searchtp"
        )

        captchaResponse = session.get(captcha)
        captchaBase64 = base64.b64encode(captchaResponse.content).decode("utf-8")

        # # For Testing Purpose only

        # imageString = f'<img src="data:image/png;base64,{captchaBase64}" alt="captcha">'
        # with open('captcha.html','w') as f:
        #     f.write(imageString)   
        #     f.close()

        # #

        sessions[id] = {
            "session": session
        }

        json_response = {
            "sessionId": id,
            "image": "data:image/png;base64," + captchaBase64,
        }

        return jsonify(json_response)
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching captcha"})
    

@app.route("/getGSTDetails", methods=["POST"])
def getGSTDetails():
    try:
        sessionId = request.json.get("sessionId")
        GSTIN = request.json.get("GSTIN")
        captcha = request.json.get("captcha")

        user = sessions.get(sessionId)

        session = user['session']
        if session is None:
            return jsonify({"error": "Invalid session id"})

        gstData = {
            "gstin": GSTIN,
            "captcha": captcha,
        }

        response = session.post(
            "https://services.gst.gov.in/services/api/search/taxpayerDetails",
            json=gstData
        )

        return jsonify(response.json())
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching GST Details"})


if __name__ == "__main__":
    app.run()
