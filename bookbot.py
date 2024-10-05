import sys

from internal.file import read_file
from internal.text_analyzer import TextAnalyzer


def main():
  # Check if a file path was provided as a command-line argument
  if len(sys.argv) != 2:
    print("Usage: python text_analysis.py <path_to_text_file>")
    sys.exit(1)

  filepath = sys.argv[1].strip()

  try:
    text = read_file(filepath)
    analyzer = TextAnalyzer(text)
    report = analyzer.format_report()
    print(report)
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
