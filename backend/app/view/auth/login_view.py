from flask import jsonify
import flask

from app.view.view_model.auth.login_response import LoginResponse
from app.core.entities.response import Response
from app.model.entities.user import User


class LoginView():
    def __init__(self, result: User | None) -> None:
        self._result = result

    def response(self) -> tuple[flask.Response, int]:
        if self._result:
            response = LoginResponse("login user", self._result, 200)
            return jsonify(response.serialize), 200

        response = Response("wrong email or password", 400)
        return jsonify(response.serialize), 400
