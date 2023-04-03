from flask import jsonify
import flask

from app.view.view_model.auth.me_response import MeResponse
from app.model.entities.user import User
from app.core.entities.response import Response


class MeView:
    def __init__(self, result: User) -> None:
        self._result = result

    def response(self) -> tuple[flask.Response, int]:
        if self._result:
            response = MeResponse("current user", self._result, 200)
            return jsonify(response.serialize), 200
        
        response = Response("invalid access token", 400)
        return jsonify(response.serialize), 200
