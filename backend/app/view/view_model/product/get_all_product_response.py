from app.core.entities.response import Response
from app.model.entities.product import Product


class GetAllProductResponse(Response):
    user: Product

    def __init__(self, message: str, products: list[Product], status_code: int) -> None:
        super().__init__(message, status_code)
        self.products = products

    @property
    def serialize(self):
        return {
            'status_code': self.status_code,
            'message': self.message,
            'data': [i.serialize for i in self.products],
        }
