from enum import Enum
from typing import Optional

from pydantic import Field, BaseModel


class TaskStatus(Enum):
    """
    This class contain the task statuses
    """
    CREATED = 'created'
    IN_WORK = 'in_work'
    COMPLETED = 'completed'


class Base(BaseModel):
    pass


class ApiTask(Base):
    """
    This class for creating tasks

    Args:
        title (str): title of task
        description (str): full information of task
    """
    title: str = Field(max_length=50)
    description: str = Field(max_length=500, default=None)


class ApiTaskChange(ApiTask):
    """
    This class for updating tasks
    """
    status: Optional[TaskStatus] = None
