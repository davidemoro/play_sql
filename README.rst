========
play sql
========


.. image:: https://img.shields.io/pypi/v/play_sql.svg
        :target: https://pypi.python.org/pypi/play_sql

.. image:: https://img.shields.io/travis/tierratelematics/play_sql.svg
        :target: https://travis-ci.org/tierratelematics/play_sql

.. image:: https://readthedocs.org/projects/play-sql/badge/?version=latest
        :target: https://play-sql.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/tierratelematics/play_sql/shield.svg
     :target: https://pyup.io/repos/github/tierratelematics/play_sql/
     :alt: Updates


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
     'query': 'SELECT *',
     'variable': 'invoice_id',
     'variable_expression': 'results[0][0]',
     'assertion': 'invoice_id == $invoice_id'}

where:

* ``database_url`` follows the format described 
  http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls

* ``autocommit``, by default it is false. If true executes and commits too.

Twitter
=======

``pytest-play`` tweets happens here:

* `@davidemoro`_

Credits
=======

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/tierratelematics/cookiecutter-play-plugin
.. _pytest-play: https://github.com/tierratelematics/pytest-play
.. _cookiecutter-qa: https://github.com/tierratelematics/cookiecutter-qa
.. _`@davidemoro`: https://twitter.com/davidemoro