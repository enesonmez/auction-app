from app.core.entities.response import Response
from app.model.entities.user import User


class GetAllUserResponse(Response):
    user: User

    def __init__(self, message: str, users: list[User], status_code: int) -> None:
        super().__init__(message, status_code)
        self.users = users

    @property
    def serialize(self):
        return {
            'status_code': self.status_code,
            'message': self.message,
            'data': [i.serialize for i in self.users],
        }
