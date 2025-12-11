from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) >= 2:
        pass
    else:
        print("Usage: python3 main.py <path_to_book>")
        print(sys.exit(1))
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_chars_dict(text)
    num_chars_sorted_list = chars_dict_to_sorted_list(num_chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_chars_sorted_list:
        if not item["char"].isalpha(): 
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    



main()

#"books/frankenstein.txt"