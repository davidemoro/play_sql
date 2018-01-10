from pytest_play.providers import BaseProvider
from sqlalchemy.pool import NullPool
from sqlalchemy import (
    create_engine,
    text,
)


class SQLProvider(BaseProvider):
    """ SQL provider """

    def get_db(self, database_url):
        """ Return a cached db engine if available """
        if not hasattr(self.engine, 'play_sql'):
            self.engine.play_sql = {}
        db = self.engine.play_sql.get(database_url)
        if not db:
            db = create_engine(
                database_url,
                poolclass=NullPool)
            self.engine.play_sql[database_url] = db
        return db

    def command_sql(self, command, **kwargs):
        database_url = command['database_url']
        db = self.get_db(database_url)
        rows = db.execute(text(command['query']))
        return rows
