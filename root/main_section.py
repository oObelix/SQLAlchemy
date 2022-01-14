from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, Session

from root.db_controller import engine
import root.models as models

session = Session(bind=engine)
# Session = sessionmaker(bind=engine)
# session = Session()


class MS:
    @classmethod
    def select(cls):
        persons = session.execute(
            select(models.Person)
        ).all()
        return [person[0].name for person in persons]

    @classmethod
    def select_scalars(cls):
        return session.execute(
            select(models.Person.name)
        ).scalars().all()

    @classmethod
    def inner_join(cls):
        result = session.execute(
            select(
                models.Person,
                models.Position
            ).join(
                models.Position,
                models.Person.position == models.Position.id
            )
        ).scalars().all()
        return [(item.id, item.name, item.position) for item in result]

    @classmethod
    def outer_join(cls):
        result = session.execute(
            select(
                models.Person,
                models.Position
            ).join(
                models.Position,
                models.Person.position == models.Position.id,
                isouter=True
            )
        ).all()
        return [
            (item.Person.id, item.Person.name, item.Position and item.Position.title)
            for item in result
        ]
