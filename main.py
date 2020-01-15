from book import Book
from library import Library

nss_library = Library("NSS Library")
print(nss_library.name)

# creating an instance (which is an object) of the Book class so they will all have the same attributes and methods. To create an instance of the class, you type the name of the class and put parenthesis after it. You should always store the object instance in a variable.
book_one = Book("J. K. Rowling", "Harry Potter and the Philosopher's Stone")
# book_one.title = "Harry Potter and the Philosopher's Stone"
# book_one.author = "J. K. Rowling"
book_one.current_page = 1

print(f"I am reading {book_one.title} by {book_one. author}")

# book_two = dict()

book_one.start_reading()

# book_two = Book()
# book_two.title = "Harry Potter and the Chamber of Secrets"
# book_two.author = "J. K. Rowling"
# book_two.current_page = 197

# book_two.start_reading()
# Each instance is an object

nss_library.add_book(book_one)


nss_library.set_address("301 Plus Park Blvd.")
print(nss_library.address)