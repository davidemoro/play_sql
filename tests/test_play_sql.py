#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_sql` package."""

import pytest


@pytest.fixture(scope='session')
def variables():
    return {'skins': {'skin1': {'base_url': 'http://', 'credentials': {}}}}


@pytest.mark.parametrize("query, expected_len", [
    ('SELECT id FROM invoices', 4,),
    ('SELECT id as invoice_id FROM invoices', 4,),
    ('SELECT id FROM invoices where id>10', 0,),
    ('SELECT id FROM invoices where id<3', 2,),
])
def test_query(query, expected_len, play_json):
    import os
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'database.db')
    database_url = 'sqlite:///{0}'.format(db_path)
    from play_sql import providers
    print_provider = providers.SQLProvider(play_json)
    assert print_provider.engine is play_json
    sql = print_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'query': query})
    results = [result for result in sql]
    assert len(results) == expected_len

    if expected_len != 0:
        assert results[0][0] == 1


def test_multiple_commands(play_json):
    query1 = 'select * from invoices;'
    query2 = 'select id from invoices where id=1;'
    import os
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'database.db')
    database_url = 'sqlite:///{0}'.format(db_path)
    from play_sql import providers
    print_provider = providers.SQLProvider(play_json)
    assert print_provider.engine is play_json
    sql = print_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'query': query1})
    results = [result for result in sql]
    assert len(results) == 4
    assert results[0][0] == 1
    assert results[0][1] == 'invoice 1'

    sql = print_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'query': query2})
    results = [result for result in sql]
    assert len(results) == 1
    assert results[0][0] == 1
