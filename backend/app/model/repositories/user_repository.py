from app.model.entities.user import User
from app.core.data_access.sql_alchemy_repository import SQLAlchemyRepository
from sqlalchemy.orm import Session


class UserRepository(SQLAlchemyRepository[User, Session]):

    def __init__(self, db: Session):
        super().__init__(db, User)
