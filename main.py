def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    print(get_book_test("books/frankenstein.txt"))


main()