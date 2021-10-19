import unittest
from ProgrammingLanguages import python as pythonAnalyzer

class TestPyAnalizerMethods(unittest.TestCase):

    def test_correct(self):
        pythonAnalyzer.analyze("src/test/examples/sample.py")
        rows_data, chars_data = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["lang"], "Python")
        self.assertEqual(rows_data["extension"], ".py")
        self.assertEqual(rows_data["rows"], 8)
        self.assertEqual(rows_data["non_empty_rows"], 6)
        self.assertEqual(rows_data["empty_rows"], 2)
        self.assertEqual(rows_data["comment_rows"], 2)
        self.assertEqual(rows_data["import_rows"], 1)

        self.assertEqual(chars_data["lang"], "Python")
        self.assertEqual(chars_data["letters"], 86)
        self.assertEqual(chars_data["symbols"], 17)
        self.assertEqual(chars_data["whitespaces"], 36)
        self.assertEqual(chars_data["digits"], 2)
        self.assertEqual(chars_data["numbers"], 2)
        self.assertEqual(chars_data["total"], 141)


if __name__ == '__main__':
    unittest.main()