from app.core.entities.entity import Entity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import desc
from app.model.entities.offer import Offer


class Product(Entity):
    __tablename__ = 'product'
    name = Column(String(100), nullable=False)
    image_url = Column(String(300), nullable=False)
    offers = relationship('Offer', backref='product', lazy='dynamic')

    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

    def maxOfferProduct(self):
        return self.offers.order_by(desc(Offer.price)).first()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url
        }


    def __repr__(self):
        return '<Product %r>' % self.name
