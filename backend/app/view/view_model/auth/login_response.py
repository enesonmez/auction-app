from app.core.entities.response import Response
from app.model.entities.user import User


class LoginResponse(Response):
    access_token: str = ""

    def __init__(self, message: str, user:User, status_code: int) -> None:
        super().__init__(message, status_code)
        self._user = user

    @property
    def serialize(self):
        return {
            'data':self._user.serialize,
            'status_code': self.status_code,
            'message': self.message,
        }
