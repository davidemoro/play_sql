#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_sql` package."""


def test_provider():
    from play_sql import providers
    print_provider = providers.SQLProvider(None)
    assert print_provider.engine is None
    print_provider.command_sql(
        {'provider': 'play_sql',
         'type': 'sql',
         'message': 'Hello, World!'})
