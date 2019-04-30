import unittest
from redact_problem import redact_words

class RedactClass(unittest.TestCase):

    def testNormal(self):
        
        words = ["Hello", "Shit", "Medi"]
        banned = ["Shit", "Stupid", "Evil"]

        assert "Shit" not in redact_words(words, banned)
        assert "Hello" in redact_words(words, banned)
        assert "Medi" in redact_words(words, banned)


if __name__ == '__main__':
    unittest.main()