#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_sql` package."""

import pytest


@pytest.fixture(scope='session')
def variables():
    return {'skins': {'skin1': {'base_url': 'http://', 'credentials': {}}}}


@pytest.mark.parametrize("query", [
    'SELECT id FROM invoices WHERE id=1',
    'SELECT id FROM invoices WHERE id<2',
])
def test_query(query, play_json):
    import os
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'database.db')
    database_url = 'sqlite:///{0}'.format(db_path)
    from play_sql import providers
    sql_provider = providers.SQLProvider(play_json)
    assert sql_provider.engine is play_json
    sql_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'variable': 'invoice_id',
         'variable_expression': 'results.fetchone()',
         'query': query})
    play_json.variables['invoice_id'][0] == 1


@pytest.mark.parametrize("query, variable_expression", [
    ('SELECT id FROM invoices WHERE id>10', 'results.fetchone()',),
    ('SELECT id FROM invoices WHERE id>10', 'results.first()',),
])
def test_query_no_results(query, variable_expression, play_json):
    import os
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'database.db')
    database_url = 'sqlite:///{0}'.format(db_path)
    from play_sql import providers
    sql_provider = providers.SQLProvider(play_json)
    assert sql_provider.engine is play_json
    sql_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'variable': 'invoice_id',
         'variable_expression': variable_expression,
         'query': query})
    play_json.variables['invoice_id'] is None


@pytest.mark.parametrize("query, variable_expression", [
    ('SELECT id FROM invoices WHERE id>10', 'results.fetchone()',),
])
def test_query_no_results_assertion(query, variable_expression, play_json):
    import os
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'database.db')
    database_url = 'sqlite:///{0}'.format(db_path)
    from play_sql import providers
    sql_provider = providers.SQLProvider(play_json)
    assert sql_provider.engine is play_json
    with pytest.raises(AssertionError):
        sql_provider.command_sql(
            {'provider': 'play_sql',
             'type': 'sql',
             'database_url': database_url,
             'variable': 'invoice_id',
             'variable_expression': variable_expression,
             'assertion': 'variables["invoice_id"] is not None',
             'query': query})
    play_json.variables['invoice_id'] is None


def test_multiple_commands(play_json):
    query1 = 'select * from invoices;'
    query2 = 'select id from invoices where id=1;'
    import os
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'database.db')
    database_url = 'sqlite:///{0}'.format(db_path)
    from play_sql import providers
    sql_provider = providers.SQLProvider(play_json)
    assert sql_provider.engine is play_json
    import pdb; pdb.set_trace()
    sql_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'variable': 'all_invoices',
         'variable_expression': 'results.fetchall()',
         'assertion': 'len(variables["all_invoices"]) == 4 and '
                      'variables["all_invoices"][0][1] == "invoice 1"',
         'query': query1})

    sql_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'database_url': database_url,
         'variable': 'invoice_id',
         'variable_expression': 'results.fetchone()[0]',
         'assertion': '$invoice_id == variables["all_invoices"][0][0]',
         'query': query2})
