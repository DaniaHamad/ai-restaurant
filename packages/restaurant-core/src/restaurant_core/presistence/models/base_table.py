from restaurant_core.presistence.models.base_model import BaseModel
import uuid
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import UUID

class BaseTable(BaseModel):
    __abstract__ = True

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Unique record identifier"
    )
    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
        comment="Record creation time"
    )
    updated_at = Column(
        DateTime,
        onupdate=func.now(),
        nullable=True,
        comment="Record last update time"
    )
