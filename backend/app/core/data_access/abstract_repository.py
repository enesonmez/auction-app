import abc
from typing import TypeVar, Generic

TEntity = TypeVar("TEntity")

class AbstractRepository(Generic[TEntity], abc.ABC):

    @abc.abstractmethod
    def add(self, entity: TEntity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, **kwargs):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError