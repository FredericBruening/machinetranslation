import unittest
from translator import englishtofrench, englishtogerman

class TestTranslator(unittest.TestCase):
    def test_english_to_french_cannot_translate_null(self):
        with self.assertRaises(TypeError):
            englishtofrench()

    def test_english_to_french_translates_a_single_word(self):
        self.assertEqual('Bonjour', englishtofrench('Hello'))

    def test_english_to_french_translates_a_sentence(self):
        self.assertEqual('Parlez-vous anglais?', englishtofrench('Do you speak English?'))

    def test_english_to_german_cannot_translate_null(self):
        with self.assertRaises(TypeError):
            englishtogerman()

    def test_english_to_german_translates_a_single_word(self):
        self.assertEqual('Hallo', englishtogerman('Hello'))

    def test_english_to_german_translates_a_sentence(self):
        self.assertEqual('Sprechen Sie Englisch?', englishtogerman('Do you speak English?'))