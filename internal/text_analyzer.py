class TextAnalyzer:
    def __init__(self, text):
        self.text: str = text
        self.word_count: int = self.get_num_words()
        self.letter_count: list = self.get_letters_count()
        self.common_words: list = self.get_most_common_words(25)

    def get_num_words(self) -> int:
        return len(self.text.split())

    def get_letters_count(self) -> list:
        letter_count_dict = {}
        for letter in self.text.lower():
            if letter.isalpha():
                letter_count_dict[letter] = letter_count_dict.get(letter, 0) + 1

        return sorted(letter_count_dict.items(), key=lambda item: item[1], reverse=True)

    def get_most_common_words(self, n: int) -> list:
        words = self.text.split()
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        return sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:n]

    def format_report(self) -> str:
        report = "--- Begin report ---\n"
        report += f"{self.word_count} words found in the document\n\n"

        report += "Letter frequency:\n"
        for letter, count in self.letter_count:
            report += f"'{letter}' : {count}\n"
        report += "\n"

        report += "Word frequency:\n"
        for word, count in self.common_words:
            report += f"'{word}' : {count}\n"
        report += "\n"

        report += "--- End report ---\n"
        return report