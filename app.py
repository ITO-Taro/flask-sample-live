import os
from dotenv import load_dotenv
from flask import Flask, jsonify


server = Flask(__name__)

@server.route("/", methods=['Get'])
def api_welcome():
    """
    welcome page
    """
    return "welcome to the main page"
@server.route("/api/ping", methods=['GET'])
def api_ping():
    """
    api ping
    """
    return jsonify({"message": "pong"})


@server.route("/api/hello/<string:name>", methods=['GET'])
def api_hello(name: str):
    """
    api hello
    """
    load_dotenv()
    env = os.getenv("ENV")
    return jsonify({"message": f"Hi {name}!", "env": env})
if __name__ == '__main__':
    server.run(host='0.0.0.0',port=8000, debug=True)
