import unittest
import os

def analyze_text(filename):
    """Calculate number of lines and chars in file

    Args:
        filename: Name of the file to be analyzed

    Raises:
        IOError: If ''filename'' does not exist or cant be read

    Returns: A tupe where first element is number of lines
        in the file and second element is number of characters
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines +=1
            chars += len(line)
        return(lines,chars)    

class TextAnalysisTests(unittest.TestCase):
    """Tests for the analyze_text() function"""

    def setUp(self):
        """Fixture that creates a file for text method to use"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in creating a program.\n'
                    'and testing whether that program,\n'
                    'can work properly')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.filename)
        except:
            pass
        #test is stable

    def test_function_runs(self):
        """Does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_character_count(self):
        """Check that the char count is correct"""
        self.assertEqual(analyze_text(self.filename)[1],93)

    def test_no_such_file(self):
        """Check proper exception is thrown for missing file"""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == "__main__":
    unittest.main()

