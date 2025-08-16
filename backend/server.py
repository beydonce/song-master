from flask import Flask, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/data')
def get_time():
    now = datetime.datetime.now()
    return jsonify({
        "Name": "geek",
        "Age": 22,
        "Date": now.strftime("%Y-%m-%d %H:%M:%S"),
        "Programming": "python"
    })

if __name__ == "__main__":
    app.run(debug=True)
