from stats import get_num_words, get_num_char
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    # print(get_book_text("books/frankenstein.txt"))
    
    words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {words} total words")
    print(get_num_char(get_book_text("books/frankenstein.txt")))
main()
