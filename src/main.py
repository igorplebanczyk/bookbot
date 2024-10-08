import sys
from .file import read_file
from .text_analyzer import TextAnalyzer

def main() -> None:
  # Check if a file path was provided as a command-line argument
  if len(sys.argv) != 2:
    print("Usage: python -m bookbot <path_to_txt_file>")
    sys.exit(1)

  filepath = sys.argv[1].strip()

  try:
    text = read_file(filepath)
    analyzer = TextAnalyzer(text)
    report = analyzer.format_report()
    print(report)
  except Exception as e:
    print(f"Error: {e}")
