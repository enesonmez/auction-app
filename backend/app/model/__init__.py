from app.model.repositories.user_repository import UserRepository
from app.model.repositories.product_repository import ProductRepository
from app.model.repositories.offer_repository import OfferRepository
from app.model.services.user_service import UserService
from app.model.services.auth_service import AuthService
from app.model.services.product_service import ProductService
from app.model.services.offer_service import OfferService
from app.core.entities.entity import Entity
import config

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    config.Config.SQLALCHEMY_DATABASE_URI
)

db_session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)


def init_db():
    Entity.metadata.create_all(bind=engine)
    print("Initialized the db")


# IoC Singleton
user_repository = UserRepository(db=db_session)
user_service = UserService(user_repoistory=user_repository)

auth_service = AuthService(user_service=user_service)

product_repository = ProductRepository(db=db_session)
product_service = ProductService(product_repoistory=product_repository)


offer_repository = OfferRepository(db=db_session)
offer_service = OfferService(offer_repoistory=offer_repository,
                             user_service=user_service, product_service=product_service)
