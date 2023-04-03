from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.entities.entity import Entity


class User(Entity):
    __tablename__ = 'user'

    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    offers = relationship('Offer', backref='user', lazy=True)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    @property
    def serialize(self):
        return {
            'id': str(self.id),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email
        }

    def __repr__(self):
        return '<User %r>' % self.firstname
