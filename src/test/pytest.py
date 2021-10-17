import unittest
from ProgrammingLanguages import python as pythonAnalyzer

class TestPyAnalizerMethods(unittest.TestCase):

    def test_correct(self):
        pythonAnalyzer.analyze("src/test/examples/sample.py")
        print(pythonAnalyzer.get_data())
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()