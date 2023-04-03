from typing import TypeVar, Generic
from app.core.data_access.abstract_repository import AbstractRepository

TEntity = TypeVar("TEntity")
TDb = TypeVar("TDb")


class SQLAlchemyRepository(Generic[TEntity, TDb], AbstractRepository[TEntity]):
    def __init__(self, db: TDb, entity: TEntity):
        self._db = db
        self._entity = entity

    def get_all(self) -> list[TEntity]:
        users = self._db.query(self._entity).all()
        return users

    def get(self, **kwargs) -> TEntity:
        return self._db.query(self._entity).filter_by(**kwargs).first()

    def add(self, entity: TEntity) -> bool:
        self._db.add(entity)
        self._db.commit()
        return True
