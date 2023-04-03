from flask import jsonify
import flask

from app.core.entities.response import Response


class LogoutView:
    def response(self) -> tuple[flask.Response, int]:
        response = Response("done sesssion", 200)
        return jsonify(response.serialize), 200
