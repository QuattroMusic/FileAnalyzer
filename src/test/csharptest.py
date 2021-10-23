import unittest
from ProgrammingLanguages import csharp as cSharpAnalyzer

class TestCSharpAnalizerMethods(unittest.TestCase):

    def test_correct(self):
        cSharpAnalyzer.analyze("src/test/examples/HelloWorld.cs")
        rows_data, chars_data = cSharpAnalyzer.get_data()
        self.assertEqual(rows_data["lang"], "CSharp")
        self.assertEqual(rows_data["extension"], ".cs")
        self.assertEqual(rows_data["rows"], 14)
        self.assertEqual(rows_data["non_empty_rows"], 14)
        self.assertEqual(rows_data["empty_rows"], 0)
        self.assertEqual(rows_data["comment_rows"], 1)
        self.assertEqual(rows_data["import_rows"], 1)

        self.assertEqual(chars_data["lang"], "CSharp")
        self.assertEqual(chars_data["letters"], 165)
        self.assertEqual(chars_data["symbols"], 32)
        self.assertEqual(chars_data["whitespaces"], 101)
        self.assertEqual(chars_data["digits"], 0)
        self.assertEqual(chars_data["numbers"], 0)
        self.assertEqual(chars_data["total"], 298)
    
    def test_comment_simple(self):
        cSharpAnalyzer.analyze_rows("// this is a comment")
        rows_data, _ = cSharpAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_comment_inline(self):
        cSharpAnalyzer.analyze_rows("a = 10; // this is a comment in the same line")
        rows_data, _ = cSharpAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_comment_inline_with_string(self):
        cSharpAnalyzer.analyze_rows("a = \"this // is in a string\"; // this is a comment in the same line")
        rows_data, _ = cSharpAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 1)
    
    def test_string_with_comment_symbol(self):
        cSharpAnalyzer.analyze_rows("a = \"this // is in a string\";")
        rows_data, _ = cSharpAnalyzer.get_data()
        self.assertEqual(rows_data["comment_rows"], 0)
        
    def tearDown(self):
        cSharpAnalyzer.reset()

if __name__ == '__main__':
    unittest.main()