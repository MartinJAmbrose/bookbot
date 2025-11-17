# Read the Frankenstein text file
# filepath_name = input("Enter Filepath to Frankenstein: ")

def get_book_text(filepath_name):
    with open(filepath_name) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = get_book_text("/Users/martinambrose/workspace/github.com/martinjambrose/bookbot/books/frankenstein.txt")
    print(text)

if __name__ == "__main__":
    main()
