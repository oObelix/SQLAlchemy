from sqlalchemy import Column, Integer, String

import root.models as models


class Person(models.Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(Integer)

    def __init__(
            self,
            name: str,
            position: int
    ):
        self.name = name
        self.position = position
