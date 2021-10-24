import unittest
from src.analyzer.ProgrammingLanguages import python as pythonAnalyzer

class TestPyAnalizerMethods(unittest.TestCase):

    def test_correct(self):
        pythonAnalyzer.analyze("src/test/examples/sample.py")
        rows_data, chars_data = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["lang"], "Python")
        self.assertEqual(rows_data["extension"], ".py")
        self.assertEqual(rows_data["rows"], 11)
        self.assertEqual(rows_data["non_empty_rows"], 6)
        self.assertEqual(rows_data["empty_rows"], 5)
        self.assertEqual(rows_data["comment_rows"], 2)
        self.assertEqual(rows_data["import_rows"], 1)

        self.assertEqual(chars_data["lang"], "Python")
        self.assertEqual(chars_data["letters"], 86)
        self.assertEqual(chars_data["symbols"], 17)
        self.assertEqual(chars_data["whitespaces"], 40)
        self.assertEqual(chars_data["digits"], 2)
        self.assertEqual(chars_data["numbers"], 2)
        self.assertEqual(chars_data["total"], 145)
    
    def test_comment_simple(self):
        pythonAnalyzer.analyze_rows("# this is a comment")
        rows_data, _ = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_comment_inline(self):
        pythonAnalyzer.analyze_rows("a = 10 # this is a comment in the same line")
        rows_data, _ = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_comment_inline_with_string(self):
        pythonAnalyzer.analyze_rows("a = \"this # is in a string\" # this is a comment in the same line")
        rows_data, _ = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_comment_inline_with_string_alternative(self):
        pythonAnalyzer.analyze_rows("a = 'this # is in a string' # this is a comment in the same line")
        rows_data, _ = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_string_with_comment_symbol(self):
        pythonAnalyzer.analyze_rows("a = \"this # is in a string\"")
        rows_data, _ = pythonAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 0)
        
    def tearDown(self):
        pythonAnalyzer.reset()

if __name__ == '__main__':
    unittest.main()