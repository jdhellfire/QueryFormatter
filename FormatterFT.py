import unittest
from Formatter import QueryFormatter


class QueryFormatterFT(unittest.TestCase):
    def test_lower_query_str(self):
        """
        GIVEN:query str with Upper chars
        WHEN :call translate interface
        THAN :translate all Upper chars to lower in query str
        """
        formatter = QueryFormatter()
        ret = formatter.translate("HellO")
        self.assertEqual("hello", ret)


if __name__ == "__main__":
    unittest.main()
