from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import os
import json
import src.libapi as libapi

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize rate limiting

if os.environ.get("FLASK_PRODUCTION") == "true":
    limiter = Limiter(
        get_remote_address,
        app=app,
        storage_uri="redis://localhost:6379",
        strategy="fixed-window",
    )
else:
    limiter = Limiter(
        get_remote_address,
        app=app,
        strategy="fixed-window",
    )

VISITS_FILE = "visits.txt"

@app.route('/v1/increment_views', methods=['GET'])
@limiter.limit("10 per minute")
def getplusincrement():
    visits = libapi.get_visits()
    libapi.increment_visits()
    return visits
    # Client-side configured to accept plaintext

@app.route('/v1/views', methods=['GET'])
@limiter.limit("20 per minute")
def retrieve():
    visits = libapi.get_visits()
    return visits
    # Client-side configured to accept plaintext

if __name__ == '__main__':
    app.run(port=5000, debug=True)