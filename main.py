def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)

  letter_count = get_letters_count(text)
  report = format_report(dict_to_sorted_list(letter_count), text)

  print(report)


def get_num_words(text):
  words = text.split()
  return len(words)


def get_book_text(path):
  with open(path) as f:
    return f.read()


def get_letters_count(text):
  letter_count = {}

  for word in text:
    for letter in word.lower():
      if letter.isalpha():
        letter_count[letter] = letter_count.get(letter, 0) + 1

  return letter_count


def dict_to_sorted_list(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)


def format_report(list_of_dicts, text):
  report = "--- Begin report of books/frankenstein.txt ---\n"
  report += f"{get_num_words(text)} words found in the document\n\n"

  for key, value in list_of_dicts:
    report += f"The '{key}' character was found {value} times\n"

  report += "--- End report ---\n"
  return report

main()
