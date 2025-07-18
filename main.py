from stats import word_count, character_count
import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string

def main(path_too_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_too_book}...")
    print("----------- Word Count ----------")
    words = word_count(get_book_text(path_too_book))
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    chars = character_count(get_book_text(path_too_book))
    for f,e in chars.items():
        if f.isalpha() == True:
            print(f"{f}: {e}")
    print("============= END ===============")
main(sys.argv[1])


    