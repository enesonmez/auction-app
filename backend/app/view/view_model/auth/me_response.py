from app.core.entities.response import Response
from app.model.entities.user import User


class MeResponse(Response):
    user: User

    def __init__(self, message: str, user: User, status_code: int) -> None:
        super().__init__(message, status_code)
        self.user = user

    @property
    def serialize(self):
        return {
            'status_code': self.status_code,
            'message': self.message,
            'data': self.user.serialize,
        }
