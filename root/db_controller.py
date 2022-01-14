from sqlalchemy import create_engine
from root import context

engine = create_engine(
    context.connection_string,
    echo=False,
    encoding='utf-8'
)
