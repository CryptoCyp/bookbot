from stats import char_count
from stats import summary_function
import sys

def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    content = get_book_test(book_path)
    letter_count = char_count(content)
    summary_function(letter_count, content)


main()
