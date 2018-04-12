========
play sql
========


.. image:: https://img.shields.io/pypi/v/play_sql.svg
        :target: https://pypi.python.org/pypi/play_sql

.. image:: https://travis-ci.org/davidemoro/play_sql.svg?branch=develop
       :target: https://travis-ci.org/davidemoro/play_sql

.. image:: https://readthedocs.org/projects/play-sql/badge/?version=latest
        :target: https://play-sql.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/davidemoro/play_sql/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/davidemoro/play_sql


pytest-play support for SQL expressions and assertions

More info and examples on:

* pytest-play_, documentation
* cookiecutter-qa_, see ``pytest-play`` in action with a working example if you want to start hacking


Features
--------

This project defines a new pytest-play_ command:

::

    {'type': 'sql',
     'provider': 'play_sql',
     'database_url': 'postgresql://$db_user:$db_pwd@$db_host/$db_name',
     'query': 'SELECT id, title FROM invoices',
     'variable': 'invoice_id',
     'variable_expression': 'results.first()[0]',
     'assertion': 'invoice_id == $invoice_id'}

where:

* ``database_url`` follows the format described 
  http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls
* ``variable_expression`` is a Python expression
    * ``results.fetchone()`` returns an array whose elements matches with the next row's
      columns and it could be invoked many times until there will be no more rows (eg: first call
      ``(1, 'first',)``, second call ``(2, 'second')``)
    * ``results.first()`` returns an array whose elements matches with the first row's colums and it
      can be invoked exactly one time
    * ``results.fetchall()`` returns an array of tuples whose elements matches with the selected
      colums (eg: ``[(1, 'first'), (2, 'second'), (3, 'third')]``)

Twitter
-------

``pytest-play`` tweets happens here:

* `@davidemoro`_

Credits
-------

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/davidemoro/cookiecutter-play-plugin
.. _pytest-play: https://github.com/pytest-dev/pytest-play
.. _cookiecutter-qa: https://github.com/davidemoro/cookiecutter-qa
.. _`@davidemoro`: https://twitter.com/davidemoro
