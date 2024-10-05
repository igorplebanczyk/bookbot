class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.word_count = self.get_num_words()
        self.letter_count = self.get_letters_count()

    def get_num_words(self):
        return len(self.text.split())

    def get_letters_count(self):
        letter_count = {}
        for letter in self.text.lower():
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1
        return letter_count

    def format_report(self):
        report = "--- Begin report ---\n"
        report += f"{self.word_count} words found in the document\n\n"
        for letter, count in sorted(self.letter_count.items(), key=lambda item: item[1], reverse=True):
            report += f"The '{letter}' character was found {count} times\n"
        report += "--- End report ---\n"
        return report