# store book name in a dictionary if available or not
# # create a class book, library and user

# catalogue = {
#     "Treasure Island" : "Available",
#     "Pride and Prejudice" : "Available",
#     "The Adventures of Tom Sawyer" : "Borrowed",
#     "Alice's Adventures in Wonderland" : "Available",
#     "The Adventures of Huckleberry Finn" : "Borrowed",
#     "Harry Potter" : "Available"
# }

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def checkout(self):
        if not self.is_checked_out :
            self.is_checked_out = True
            return True
        return False
    
    def return_books(self):
        if self.is_checked_out : 
            self.is_checked_out = False
            return True
        return False
    
    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Library():
    def __init__(self):
        self.books = []

    def add_books(self,title, author):
        new_book = Book(title,author)
        self.books.append(new_book)
        print(f"Added",{new_book})

    def check_out(self,title):
        for book in self.books:
            if book.title == title:
                if book.checkout():
                    print(f"The book,{title} has been checkedout by you")
                    return 
                else:
                    print(f"The book,'{title}' has been checkedout already")
        print(f"The book '{title}' does not exist")       

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.return_books():
                    print(f"The book {title} has been returned by you")
                else:
                    print(f"The book,'{title}' has not been checked out")
        print(f"The book,{title} does not exist")


    def view_books(self):
        if not self.books:
            print("This book does not exist")
            return
        for book in self.books:
            print(book)

class user():
    def __init__(self):
        self.books = []

    def borrow_book(self,library,title):
        library.check_out(title)
        self.books.append(title)

    def return_book(self,library,title):
        library.return_book(title)
        self.books.remove(title)

    def view_books(self):
        if not self.books:
            print("You have not borrowed any book")
            return
        for book in self.books:
            print(book)

def main():
    library = Library()
    library.add_books("Treasure Island","Robert Louis Stevenson")
    library.add_books("Pride and Prejudice","Jane Austen")
    library.add_books("The Adventures of Tom Sawyer","Mark Twain")
    library.add_books("Alice's Adventures in Wonderland","Lewis Carroll")
    library.add_books("The Adventures of Huckleberry Finn","Mark Twain")
    library.add_books("Harry Potter","J.K. Rowling")
    print("Welcome to the Library")
    while True:
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            library.view_books()
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            user1.borrow_book(library,title)
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            user1.return_book(library,title)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

user1 = user()
main()          




         
