import sys
from stats import get_num_words, get_character_count, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    sorted_character_count = sort_dict(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_character_count:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
