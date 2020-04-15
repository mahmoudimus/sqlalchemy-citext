import unittest

from citext import CIText
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql


class TestCIText(unittest.TestCase):

    def test_field_concatenable(self):
        self.assertEqual(
            str(Column(CIText(), name='field') + 'value'),
            'field || :field_1'
        )

    def test_field_compare_string(self):
        self.assertEqual(
            str(Column(CIText(), name='field') == 'NON_EXISTING'),
            "field = :field_1")

        self.assertEqual(
            str((Column(CIText(), name='field') == 'NON_EXISTING').compile(
                dialect=postgresql.dialect(),
                compile_kwargs={'literal_binds': True})),
            "field = 'NON_EXISTING'")

        self.assertEqual(
            str((Column(CIText(), name='field') == "NON|'_EXISTING%").compile(
                dialect=postgresql.dialect(),
                compile_kwargs={'literal_binds': True})),
            "field = 'NON|''_EXISTING%%'")
