from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import func
from app.core.utilities.guid import GUID
import uuid

Base = declarative_base()


class Entity(Base):
    __abstract__ = True

    id = Column(GUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime,
                        default=func.current_timestamp(),
                        onupdate=func.current_timestamp())
