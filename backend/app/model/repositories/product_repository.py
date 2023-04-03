from app.model.entities.product import Product
from app.model.entities.offer import Offer
from app.model.entities.user import User
from app.core.data_access.sql_alchemy_repository import SQLAlchemyRepository
from sqlalchemy import desc, asc, func
from sqlalchemy.sql.functions import coalesce, max, concat
from sqlalchemy.orm import Session

from app.model.entities.dtos.product_price_dto import ProductPriceDto


class ProductRepository(SQLAlchemyRepository[Product, Session]):

    def __init__(self, db: Session):
        super().__init__(db, Product)

    def get_max_offer_product(self, product: Product) -> Offer:
        return product.offers.order_by(desc(Offer.price)).first()

    def get_all_max_offer_product(self):
        result = self._db.query(self._entity.id, self._entity.name, self._entity.image_url, coalesce(max(Offer.price), 0).label("price"), coalesce(User.email, 'Dont Offer').label("full_name")).join(
            Offer, self._entity.id == Offer.product_id, isouter=True).join(User, Offer.user_id == User.id).group_by(self._entity.id).all()

        output: list[ProductPriceDto] = list()
        for row in result:
            output.append(ProductPriceDto(
                row.id, row.name, row.image_url, row.price, row.full_name))

        return output
