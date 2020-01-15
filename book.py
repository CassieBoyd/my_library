# classes are instructions for how to make a thing, this is a blueprint for making a book. Define attributes and behaviors of a thing but it isn't the thing itself. Class names always start with a capital letter.
class Book:
    # self is not taco, self is always self. When called you don't need to pass an argument for self. You do need arguments for any additional positional arguments
    # double underscore indicates that the method is never called directly, also overrides built-in init method
    # def is definition
    def __init__(self, author, title):
        # Establish the properties of each book
        # with a default value
        # Attributes
        self.title = title
        self.publisher = ""
        self.author = author
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page


