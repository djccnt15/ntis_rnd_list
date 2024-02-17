from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

ID = TypeVar("ID", int, UUID)


class IdModel(BaseModel, Generic[ID]):
    id: ID
