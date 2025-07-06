from stats import word_count
from stats import char_count

# Define a function to read the file content
def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Define a main function to use the above
def main():
    # Relative path to the book file (make sure the file is in the same folder as this script)
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    words = word_count(book_text)
    print(f"{words} words found in the document")

    characters = char_count(book_text)
    print(characters)

# Call the main function to run the program


main()
