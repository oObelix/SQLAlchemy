from sqlalchemy import Column, Integer, String

import root.models as models


class Position(models.Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __init__(
            self,
            title: str
    ):
        self.title = title
