class TextAnalyzer:
    def __init__(self, text):
        self.text: str = text

        self.word_count: int = self.get_num_words()
        self.unique_word_count: int = self.get_unique_word_count()

        self.letter_frequency: list = self.get_letter_frequency()
        self.word_frequency: list = self.get_word_frequency(25)
        self.punctuation_frequency: list = self.get_punctuation_frequency()

        self.average_word_length: float = self.get_average_word_length()

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

    def format_report(self) -> str:
        report = "--- Begin report ---\n"

        report += f"Number of words: {self.word_count}\n"
        report += f"Number of unique words: {self.unique_word_count}\n"
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
