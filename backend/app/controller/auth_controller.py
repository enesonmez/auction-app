from flask import Blueprint, jsonify, request, session
from app.core.decorators.validationDecorator import *
from app.model.entities.user import User
from app.model.entities.dtos.login_dto import LoginDto
from app.controller.validation.authValidation import LoginSchema, AccessTokenSchema
from app.model import auth_service
from app.view.auth.login_view import LoginView
from app.view.auth.logout_view import LogoutView
from app.view.auth.me_view import MeView
from app.core.decorators.login_required_decorator import login_required

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.post("/login")
@validate_json
@validate_schema(LoginSchema())
def login():
    data = request.json
    login_dto = LoginDto(email=data["email"], password=data["password"])

    result = auth_service.login(login_dto)

    return LoginView(result).response()


@auth.get("/logout")
def logout():
    auth_service.logout()
    return LogoutView().response()


@auth.get("/me")
@login_required
def val():
    result = auth_service.me()
    return MeView(result).response()
