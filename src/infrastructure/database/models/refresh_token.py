from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models import ApplicationInfo, User


class RefreshToken(Base):
    """Модель refresh токена."""

    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    application_info_id: Mapped[int]
    token: Mapped[str]
    blocked: Mapped[bool]

    owner: Mapped["User"] = relationship(back_populates="refresh_tokens")
    application_info: Mapped["ApplicationInfo"] = relationship(
        back_populates="refresh_token"
    )
