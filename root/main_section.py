from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from root.db_controller import engine
import root.models as models

Session = sessionmaker(bind=engine)
session = Session()
# from sqlalchemy.orm import Session
# session = Session(bind=engine)


class MS:
    @classmethod
    def select(cls):
        persons = session.execute(
            select(models.Person)
        ).all()
        # Possible use index, but not recommended:
        # return [person[0].name for person in persons]
        return [person.Person.name for person in persons]

    @classmethod
    def select_scalars(cls):
        """
        Using scalars()
        :return:
        """
        return session.execute(
            select(models.Person.name)
        ).scalars().all()

    @classmethod
    def inner_join(cls):
        """
        Use scalars() only if no need access to the right model in most cases
        with INNER JOIN
        :return:
        """
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
        """
        Not used scalars() to get access to models.* in result tuples
        :return:
        """
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
