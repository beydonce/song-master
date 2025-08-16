from flask import Flask, jsonify, request
from models.User import User
from pymongo import MongoClient
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:9000"])

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client['mydatabase']
users = db['users']

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if users.find_one({'username': username}):
        return jsonify({'message': "usernmae already exist ."}), 400
    new_user = User(username, password)
    users.insert_one(new_user.to_dict())
    return jsonify({'message': 'user registered my nigga!'}), 201

@app.route('/users', methods=['GET'])
def allusers():
    all_users = list(users.find({}, {"_id": 0}))  # שולף את כל המשתמשים בלי ה־_id
    return jsonify(all_users), 200


# @app.route('/data')
# def get_time():
#     now = datetime.datetime.now()
#     return jsonify({
#         "Name": "geek",
#         "Age": 22,
#         "Date": now.strftime("%Y-%m-%d %H:%M:%S"),
#         "Programming": "python"
#     })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
