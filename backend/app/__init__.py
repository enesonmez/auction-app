from app.model import init_db
from app.controller import *
from app.controller.socketio import socket_io
import config

from flask import (
    Flask,
    jsonify
)
from flask_cors import CORS
from flask_session import Session

# Application initialization
app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app,
  resources={r"/*": {"origins": "*"}},
  supports_credentials=True
)

app.config.from_object(config.DevelopmentConfig)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'not found'}), 404


# Database Initialization
init_db()

# Session
Session(app)

# Register Blueprints
app.register_blueprint(main)

# Socket IO
socket_io.init_app(app, cors_allowed_origins="*")

