sqlalchemy-citext
=================

Creates a SQLAlchemy user defined type to understand
`PostgreSQL's CIText <http://www.postgresql.org/docs/9.1/static/citext.html>`_
extension.

Installation
------------

This requires some kind of PostgreSQL compatible db-api driver already
installed in order to work.

Make sure you have something like ``psycopg2`` already installed.

.. code-block:: console

    pip install sqlalchemy-citext

Usage
-----

.. code-block:: python

    from sqlalchemy import create_engine, MetaData, Integer
    from sqlalchemy.schema import Column, Table
    import sqlalchemy.orm as orm

    from citext import CIText


    engine = create_engine('postgresql://localhost/test_db')
    meta = MetaData()

    test_table = Table('test', meta,
        Column('id', Integer(), primary_key=True),
        Column('txt', CIText()))

    conn = engine.connect()

    meta.bind = conn
    meta.drop_all()
    meta.create_all()

    class TestObj(object):
        def __init__(self, id_, txt):
            self.id = id_
            self.txt = txt

        def __repr__(self):
            return "TestObj(%r, %r)" % (self.id, self.txt)

    orm.mapper(TestObj, test_table)
    Session = orm.sessionmaker(bind=engine)
    ses = Session()

    to = TestObj(1, txt='FooFighter')
    ses.add(to)
    ses.commit()
    row = ses.query(TestObj).filter(TestObj.txt == 'foofighter').all()
    assert len(row) == 1
    print row
    ses.close()


License
-------

``sqlalchemy-citext`` is an MIT/BSD dual-Licensed library.


Contribute
----------

- Check for open issues or open a fresh issue to start a discussion around a
  feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the master
  branch (or branch off of it).
- Write a test which shows that the bug was fixed or that the feature
  works as expected.
- Send a pull request and bug the maintainer until it gets merged and
  published.
- Make sure to add yourself to the author's file in ``setup.py`` and the
  ``Contributors`` section below :)

Contributors
------------

- `@mahmoudimus <https://github.com/mahmoudimus>`_
- `@vad <https://github.com/vad>`_
- `@dstufft <https://github.com/dstufft>`_
- `@brmzkw <https://github.com/brmzkw>`_
- `@graingert <https://github.com/graingert>`_
- `@cjmayo <https://github.com/cjmayo>`_
- `@libre-man <https://github.com/libre-man>`_
