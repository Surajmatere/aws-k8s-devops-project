from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "AWS DevOps CI/CD Application",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "1.0")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
