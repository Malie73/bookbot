from stats import get_num_words, get_num_chars, get_report
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_text = f.read()
    return file_text

def print_report(report, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(book_path))} total words")
    print("--------- Character Count -------")
    for e in report:
        if e['char'].isalpha():
            print(f"{e['char']}: {e['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    print(f"{get_num_words(book_text)} words found in the document")
    print_report(get_report(get_num_chars(book_text)), book_path)

if __name__ == "__main__":
    main()
