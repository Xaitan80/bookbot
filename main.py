# Define a function to read the file content
def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Define a main function to use the above
def main():
    # Relative path to the book file (make sure the file is in the same folder as this script)
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

# Call the main function to run the program
main()
