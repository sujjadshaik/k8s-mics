from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/weather/<location>")
def get_weather(location):
    time_response = requests.get("http://time-service:5001/time").json()
    current_time = time_response["timestamp"]
    return jsonify({"location": location, "timestamp": current_time, "weather": "sunny"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
