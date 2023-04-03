from flask import jsonify
import flask

from app.model.entities.product import Product
from app.view.view_model.product.get_all_product_response import GetAllProductResponse


class GetAllProductView:
    def __init__(self, result: list[Product]) -> None:
        self._result = result

    def response(self) -> tuple[flask.Response, int]:
        response = GetAllProductResponse("listed products", self._result, 200)
        return jsonify(response.serialize), 200
