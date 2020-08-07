import sqlalchemy
from project.settings import settings
import databases

database = databases.Database(settings.SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Put your database models here | Below


# ----- Example ------
#
# test_db = sqlalchemy.Table(
#     "test",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String),
# )


# Put your database models here | Above


engine = sqlalchemy.create_engine(settings.SQLALCHEMY_DATABASE_URL)
metadata.create_all(engine)

