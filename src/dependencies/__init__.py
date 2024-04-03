"""Реализует функции для получения распространённых зависимостей.

Например: `db: Annotated[AsyncSession, Depends(get_db)]`. Данные зависимости
являются глобальными и могут быть использована в любой фиче приложения.
"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database import async_session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Возвращает сессию для работы с базой данных."""
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
