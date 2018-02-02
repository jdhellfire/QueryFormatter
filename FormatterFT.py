import unittest
from Formatter import QueryFormatter


class QueryFormatterFT(unittest.TestCase):
    def setUp(self):
        self.formatter = QueryFormatter()

    def test_lower_query_str(self):
        """
        GIVEN:query str with Upper chars
        WHEN :call translate interface
        THEN :translate all Upper chars to lower in query str
        """
        ret = self.formatter.translate("HellO")
        self.assertEqual("hello", ret)
        """
        GIVEN:query str with -
        WHEN :call translate interface
        THEN :trans - to \- in query str
        """
        ret = self.formatter.translate("HellO-World")
        self.assertEqual("hello\\-world", ret)


    def test_repalce_dish(self):
        pass


if __name__ == "__main__":
    unittest.main()
