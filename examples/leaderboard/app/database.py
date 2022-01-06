from sqlalchemy.engine import create_engine
from core.config import settings
from databases import Database
import sqlalchemy


metadata = sqlalchemy.MetaData()

user_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.String(40), primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("country", sqlalchemy.String(50), nullable=False),
)

score_table = sqlalchemy.Table(
    "scores",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("point", sqlalchemy.Integer, nullable=False),
)

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(40) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL
)
"""

CREATE_SCORE_TABLE = """
CREATE TABLE IF NOT EXISTS scores (
    user_id VARCHAR(40) NOT NULL,
    point INTEGER NOT NULL
)
"""


CREATE_USERS_WITH_SCORES_VIEW = """
CREATE OR REPLACE VIEW users_with_scores AS
SELECT 
    u.user_id,
    u.name,
    u.country,
    (
        SELECT COALESCE(SUM(s.point), 0)
        FROM scores s
        WHERE u.user_id=s.user_id
    ) AS points
FROM users u
"""

CREATE_LEADERBOARD_VIEW = """
CREATE OR REPLACE VIEW leaderboard AS SELECT *, DENSE_RANK() OVER (ORDER BY points desc) AS "rank"
FROM users_with_scores
"""

# write an mysql query that creates a view called leaderboard
# it queries everything from users_with_scores table and adds a rank column
# the rank will be calculated by sorting the users by points in descending order
# https://www.youtube.com/watch?v=0sZ_JkQs1xk&t=10s

# the query should look like this:


GET_LEADERBOARD = """
SELECT *
FROM leaderboard l
ORDER BY l.rank
"""


database = Database(settings.DATABASE_URI)