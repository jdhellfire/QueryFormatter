import unittest
from Formatter import QueryFormatter
from FTData import TestData


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

    def test_repalce_dish(self):
        """
        GIVEN:query str with -
        WHEN :call translate interface
        THEN :trans - to \- in query str
        """
        for data in TestData['REPLACE_DISH']:
            ret = self.formatter.translate(data['INPUT'])
            self.assertEqual(data['EXPECT'], ret)

    def test_query_str_with_dish_and_no_replace_secen(self):
        """
        GEVEN:query str with - and start with " and end with "
        WEHN : call translate interface
        THEN : not translate - in query str
        """
        ret = self.formatter.translate("\"HellO-World\"")
        self.assertEqual("\"hello-world\"", ret)


if __name__ == "__main__":
    unittest.main()
