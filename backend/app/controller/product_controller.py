from flask import Blueprint, jsonify, request, session
from app.model.entities.product import Product
from app.core.decorators.validationDecorator import *
from app.controller.validation.productValidation import CreateProductSchema
from app.core.decorators.login_required_decorator import login_required
from app.view.product.get_all_product_view import GetAllProductView
from app.view.product.create_product_view import CreateProductView

from app.model import product_service

product = Blueprint('product', __name__, url_prefix='/product')


@product.get("")
@login_required
def getAllProduct():
    products = product_service.get_all_by_max_price()
    return GetAllProductView(products).response()


@product.post("")
@login_required
@validate_json
@validate_schema(CreateProductSchema())
@login_required
def createProduct():
    data = request.json
    product = Product(name=data["name"], image_url=data["image_url"])
    result = product_service.add(product)
    return CreateProductView(result).response()
