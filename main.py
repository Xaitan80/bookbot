import sys
from stats import count_words, count_characters, sort

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    #book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    c = count_characters(book_content)
    sorted_list = sort(c)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item_dict in sorted_list:
       print(f"{item_dict['char']}: {item_dict['num']}")
        



    

    #print (f"{word_count} words found in the document")
    #print (book_content)
    #print (c)
    #print (sorted_list)
    
    
main()