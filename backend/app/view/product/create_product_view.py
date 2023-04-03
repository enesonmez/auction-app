from flask import jsonify
import flask

from app.model.entities.product import Product
from app.core.entities.response import Response


class CreateProductView:
    def __init__(self, result: bool) -> None:
        self._result = result
        self._status_code = 200

    def response(self) -> tuple[flask.Response, int]:
        if self._result:
            response = Response("created user", self._status_code)
        else:
            self._status_code = 400
            response = Response("didnt create user", self._status_code)
        return jsonify(response.serialize), self._status_code
