# Read the Frankenstein text file
# filepath_name = input("Enter Filepath to Frankenstein: ")

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Return sorted dictionary
def sort_characters(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    def sort_by_num(item):
        return item["num"]
    char_list.sort(key=sort_by_num, reverse=True)
    return char_list

#def get_book_text(filepath_name):
#    with open(filepath_name) as f:
#        file_contents = f.read()
#        return file_contents


#def main():
#    text = get_book_text("/Users/martinambrose/workspace/github.com/martinjambrose/bookbot/books/frankenstein.txt")

#    num_words = len(text.split())
    
#    print(f"Found {num_words} total words")

#    return num_words

#if __name__ == "__main__":
#    main()
