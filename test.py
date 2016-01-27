import unittest
import main


class TestEntryNumbers(unittest.TestCase):

    def test_entry_numbers_not_null(self):
        with self.assertRaises(ValueError):
            main.entry_numbers(None)

    def test_entry_numbers_not_negative(self):
        with self.assertRaises(ValueError):
            main.entry_numbers(-10)

    def test_entry_numbers_is_tuple(self):
        self.assertIsInstance(
            main.entry_numbers(3), tuple)

unittest.main()
