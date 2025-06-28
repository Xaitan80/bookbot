from stats import count_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)

    print (f"{word_count} words found in the document")
    #print (book_content)
    
main()