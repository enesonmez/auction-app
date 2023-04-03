from flask import Blueprint, jsonify, request
from app.model.entities.user import User
from app.core.decorators.validationDecorator import *
from app.controller.validation.userValidation import CreateUserSchema
from app.model import user_service
from app.view.user.get_all_user_view import GetAllUserView
from app.view.user.create_user_view import CreateUserView


user = Blueprint('user', __name__, url_prefix='/user')


@user.get("")
def getAllUser():
    users = user_service.get_all()
    return GetAllUserView(users).response()


@user.post("")
@validate_json
@validate_schema(CreateUserSchema())
def createUser():
    data = request.json
    user = User(firstname=data["firstname"], lastname=data["lastname"],
                email=data["email"], password=data["password"])
    result = user_service.add(user)

    return CreateUserView(result).response()
