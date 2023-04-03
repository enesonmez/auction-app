class Response:
    message: str = ""
    status_code: int

    def __init__(self, message: str, status_code: str) -> None:
        self.message = message
        self.status_code = status_code

    @property
    def serialize(self):
        return {
            'status_code': self.status_code,
            'message': self.message,
        }
