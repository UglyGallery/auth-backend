from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models import DeviceType, RefreshToken


class ApplicationInfo(Base):
    """Модель информации о версии приложения, с которого выполнен вход."""

    __tablename__ = "application_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    device_type_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    version: Mapped[int]  # "1", "2", ..., "42" и т.д.

    refresh_token: Mapped["RefreshToken"] = relationship(
        back_populates="application_info"
    )
    device_type: Mapped["DeviceType"] = relationship(back_populates="application_info")
