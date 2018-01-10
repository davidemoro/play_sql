from pytest_play.providers import BaseProvider


class SQLProvider(BaseProvider):
    """ SQL provider """

    def command_sql(self, command, **kwargs):
        pass
