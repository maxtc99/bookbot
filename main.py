from stats import get_num_words, get_num_char, get_sorted_list
import sys

def get_filepath():
    path_to_file = None
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
    else:      
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return path_to_file

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    filepath = get_filepath()
    words = get_num_words(get_book_text(filepath))
    dict = get_num_char(get_book_text(filepath))
    sorted_list = get_sorted_list(dict)
    


    print(f'''============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------''')
    for i in sorted_list: 
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")



   
main()
