import io
from pprint import pprint
import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        translation_table = str.maketrans('', '', ''.join(punctuation))

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower().translate(translation_table)
                words = content.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)

        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            result[name] = words.count(word)

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего