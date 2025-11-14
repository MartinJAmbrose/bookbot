#  Read Frankenstein.txt file and print output
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
    return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
        print(text)

    if __name__ == "__main__"
        main()
