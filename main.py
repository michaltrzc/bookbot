from stats import count_words
from stats import count_characters
from stats import return_sorted_list_dictionaries
import sys

#book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
        
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    saved_text = get_book_text(book_path)
    counted_words = count_words(saved_text)
    counted_characters = count_characters(saved_text)
    sorted_list_to_print = return_sorted_list_dictionaries(counted_characters)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {counted_words} total words\n")
    print("--------- Character Count -------\n")
    for char_dict in sorted_list_to_print:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()   #to dodawaj na koniec do maina
