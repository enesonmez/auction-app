from flask import jsonify
import flask

from app.model.entities.user import User
from app.view.view_model.user.get_all_user_response import GetAllUserResponse


class GetAllUserView:
    def __init__(self, result: list[User]) -> None:
        self._result = result

    def response(self) -> tuple[flask.Response, int]:
        response = GetAllUserResponse("listed users", self._result, 200)
        return jsonify(response.serialize), 200
