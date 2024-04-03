from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models import ApplicationInfo


class DeviceType(Base):
    """Модель типа устройства, с которого выполнен вход.

    Например: "Android", "iOS", "WebFirefox", "WebChrome" и т.д.
    """

    __tablename__ = "device_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    application_info: Mapped["ApplicationInfo"] = relationship("device_type")
