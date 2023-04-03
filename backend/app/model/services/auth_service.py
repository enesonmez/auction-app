from app.model.services.user_service import UserService
from app.model.entities.user import User
from app.model.entities.dtos.login_dto import LoginDto
from app.core.utilities.redis_service import redis

from werkzeug.security import check_password_hash
import json
from flask import session

class AuthService:
    _userservice: UserService = None

    def __init__(self, user_service: UserService) -> None:
        self._userservice = user_service

    def login(self, login_dto: LoginDto) -> User | None:
        user = self._userservice.get(email=login_dto.email)

        if user and check_password_hash(user.password, login_dto.password):
            # redis.hset("flask-session:123", str(user.id), json.dumps(user.serialize))
            session['user'] = user
            session['is_login'] = True
            return user

        return None

    def logout(self) -> None:
        try:
            session['is_login'] = False
            # redis.hdel("flask-session:123",access_token)
        except:
            pass

    def me(self) -> User | None:
        try:
            #user = json.loads(redis.hget("flask-session:123", access_token))
            user = session['user']
            return user
        except:
            return None
