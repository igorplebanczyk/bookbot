import re


class TextAnalyzer:
    def __init__(self, text):
        self.text: str = text

        self.word_count: int = self.get_num_words()
        self.unique_word_count: int = self.get_unique_word_count()
        self.sentence_count: int = self.get_num_sentences()
        self.syllable_count: int = self.get_num_syllables()

        self.letter_frequency: list = self.get_letter_frequency()
        self.word_frequency: list = self.get_word_frequency(25)
        self.punctuation_frequency: list = self.get_punctuation_frequency()

        self.average_word_length: float = self.get_average_word_length()
        self.readability_score: float = self.get_flesch_kincaid_score()



    def get_num_words(self) -> int:
        return len(self.text.split())


    def get_letter_frequency(self) -> list:
        letter_count_dict = {}
        for letter in self.text.lower():
            if letter.isalpha():
                letter_count_dict[letter] = letter_count_dict.get(letter, 0) + 1

        return sorted(letter_count_dict.items(), key=lambda item: item[1], reverse=True)


    def get_word_frequency(self, n: int) -> list:
        words = self.text.split()
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        return sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:n]


    def get_unique_word_count(self) -> int:
        return len(set(self.text.split()))


    def get_average_word_length(self) -> float:
        words = self.text.split()
        if len(words) == 0:
            return 0.0

        return sum(len(word) for word in words) / len(words)


    def get_punctuation_frequency(self) -> list:
        punctuation_count = {}
        for char in self.text:
            if not char.isalnum() and not char.isspace():
                punctuation_count[char] = punctuation_count.get(char, 0) + 1

        return sorted(punctuation_count.items(), key=lambda item: item[1], reverse=True)


    def get_num_sentences(self) -> int:
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])


    def get_num_syllables(self) -> int:
        vowels = "aeiouy"
        text = self.text.lower()
        syllable_count = 0

        for word in text.split():
            word = word.strip(".:;?!")
            if len(word) > 0 and word[0] in vowels:
                syllable_count += 1
            for index in range(1, len(word)):
                if word[index] in vowels and word[index - 1] not in vowels:
                    syllable_count += 1

            if word.endswith("e"):
                syllable_count -= 1

            if syllable_count == 0:
                syllable_count += 1

        return syllable_count


    def get_flesch_kincaid_score(self) -> float:
        sentence_count = self.get_num_sentences()
        syllable_count = self.get_num_syllables()
        if sentence_count == 0:
            return 0.0
        return 206.835 - 1.015 * (self.word_count / sentence_count) - 84.6 * (syllable_count / self.word_count)


    def format_report(self) -> str:
        report = "--- Begin report ---\n"

        report += f"Number of words: {self.word_count}\n"
        report += f"Number of unique words: {self.unique_word_count}\n"
        report += f"Number of sentences: {self.sentence_count}\n"
        report += f"Number of syllables: {self.syllable_count}\n"
        report += f"Flesch-Kincaid readability score: {self.readability_score:.2f}\n"
        report += f"Average word length: {self.average_word_length:.2f}\n"
        report += "\n"

        report += "Letter frequency:\n"
        for letter, count in self.letter_frequency:
            report += f"'{letter}' : {count}\n"
        report += "\n"

        report += "Word frequency:\n"
        for word, count in self.word_frequency:
            report += f"'{word}' : {count}\n"
        report += "\n"

        report += "Punctuation frequency:\n"
        for punctuation, count in self.punctuation_frequency:
            report += f"'{punctuation}' : {count}\n"
        report += "\n"

        report += "--- End report ---\n"
        return report
