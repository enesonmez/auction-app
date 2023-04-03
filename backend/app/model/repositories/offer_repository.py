from app.model.entities.offer import Offer
from app.core.data_access.sql_alchemy_repository import SQLAlchemyRepository
from sqlalchemy.orm import Session


class OfferRepository(SQLAlchemyRepository[Offer, Session]):

    def __init__(self, db: Session):
        super().__init__(db, Offer)
