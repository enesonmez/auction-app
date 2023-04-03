from sqlalchemy import Column, ForeignKey, Integer
from app.core.entities.entity import Entity
from app.core.utilities.guid import GUID


class Offer(Entity):
    __tablename__ = 'offer'
    user_id = Column(GUID, ForeignKey(
        'user.id'), nullable=False)
    product_id = Column(GUID, ForeignKey(
        'product.id'), nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, user_id, product_id, price):
        self.user_id = user_id
        self.product_id = product_id
        self.price = price

    @property
    def serialize(self):
        return {
            'user_id': self.user_id,
            'product_id': self.product_id,
            'price': self.price
        }

    def __repr__(self):
        return '<Offer %r>' % self.price
