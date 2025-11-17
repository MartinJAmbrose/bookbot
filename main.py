# New Main with import
from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath_name):
    with open(filepath_name) as f:
#       file_contents = f.read()
        return f.read()

def main():
 
    if len(sys.argv) != 2:
        usage = "'Usage: python3 main.py <path_to_book>'"
        print(usage)
        return {usage, exit(1)}
        sys.exit(1)

    text = get_book_text(sys.argv[1])
#    text = get_book_text("/Users/martinambrose/workspace/github.com/martinjambrose/bookbot/books/frankenstein.txt")
    
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    print(f"Found {num_words} total words")

 #   sorted_chars = count_characters(text)
    print("--------- Character Count --------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("------------- END ------------")

#    char_counts = count_characters(text)
#    print("Character counts:")
#    print(char_counts)

if __name__ == "__main__":
    main()