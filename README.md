# BookBot

BookBot is a simple text analysis and sentiment analysis script built in Python. It can analyze the text, calculate various metrics, and determine the emotional tone of the text.

## Features

- **Text Analysis**: Analyze various aspects of the text, including:
    - Total word count
    - Unique word count
    - Sentence count
    - Syllable count
    - Average word length
    - Reading time estimation

- **Sentiment Analysis**: Assess the emotional tone of the text using a comprehensive word list. Determine if the sentiment is positive, negative, or neutral.

- **Frequency Analysis**: Get detailed insights on:
    - Letter frequency
    - Word frequency
    - Punctuation frequency
    - N-gram frequency (bigrams and trigrams)

- **Readability Metrics**: Calculate the Flesch-Kincaid readability score and grade level to assess the text's complexity.

## Installation

Clone the repository:
```bash
git clone https://github.com/igorplebanczyk/bookbot.git
```

## Usage

```bash
python -m bookbot <path_to_txt_file>
```

## Notes
* Recommended Python version: `3.10` or higher
* Requires no external dependencies
* Originally designed as a guided project on [boot.dev](https://www.boot.dev/courses/build-bookbot), but has since been heavily expanded
* It was primarily designed for learning purposes