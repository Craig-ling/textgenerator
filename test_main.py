import unittest
from main import clean_text


class MainTestCase(unittest.TestCase):
    def test_clean_text(self):
        result_list = clean_text("This string with punctuation. IT? is A test!")
        self.assertEqual(result_list, ['this', 'string', 'with', 'punctuation', 'it', 'is', 'a', 'test'])
