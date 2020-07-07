# To run test just run python file like normal

import unittest
# imports unit file wanting to be tested
import unit

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = unit.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multple_words(self):
        text = 'monty python'
        result = unit.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()


