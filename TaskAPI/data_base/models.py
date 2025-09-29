from enum import Enum
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    pass


class TaskStatus(Enum):
    """
    This class contain the task statuses
    """
    CREATED = 'created'
    IN_WORK = 'in_work'
    COMPLETED = 'completed'


class DB_Task(Base):
    """
    This class is for creating a table
    Args:
        id (num): primary key
        title (str): title of task
        description (str): full information of task
        status (select): task status from TaskStatus
    """
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.CREATED)

    def __init__(self, title: str, description: str, **kw):
        super().__init__(**kw)
        self.title = title
        self.description = description

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, description: {self.description}, status: {self.status}'
