import logging
from pytest_play.providers import BaseProvider
from sqlalchemy.pool import NullPool
from sqlalchemy import (
    create_engine,
    text,
)


class SQLProvider(BaseProvider):
    """ SQL provider """

    def __init__(self, engine):
        super(SQLProvider, self).__init__(engine)
        self.logger = logging.getLogger()

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
        with db.begin() as connection:
            rows = connection.execute(text(command['query']))
            try:
                self._make_variable(command, results=rows)
                self._make_assertion(command, results=rows)
            except Exception as e:
                self.logger.exception(
                    'Exception for command %r',
                    command,
                    e)
                raise e

    def _make_assertion(self, command, **kwargs):
        """ Make an assertion based on python
            expression against kwargs
        """
        assertion = command.get('assertion', None)
        if assertion:
            self.engine.execute_command(
                {'provider': 'python',
                 'type': 'assert',
                 'expression': assertion
                 },
                **kwargs,
            )

    def _make_variable(self, command, **kwargs):
        """ Make a variable based on python
            expression against kwargs
        """
        expression = command.get('variable_expression', None)
        if expression:
            self.engine.execute_command(
                {'provider': 'python',
                 'type': 'store_variable',
                 'name': command['variable'],
                 'expression': expression
                 },
                **kwargs,
            )
