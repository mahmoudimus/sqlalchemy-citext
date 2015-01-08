import unittest

from sqlalchemy import Column

from citext import CIText


class TestCIText(unittest.TestCase):

    def test_field_concatenable(self):
        self.assertEqual(
            str(Column(CIText(), name='field') + 'value'),
            'field || :field_1'
        )
