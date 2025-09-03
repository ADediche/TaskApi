from pydantic import Field, BaseModel


# models for API
class Base(BaseModel):
    pass


class Task(Base):
    title: str = Field()
    description: str = Field()
