import datetime
class LibItem():
    def __init__(self, t, a, i):
        super(LibItem, self).__init__()
        self.__title = t
        self.__author = a
        self.__itemID = i
        self.__onLoan = False
        self.__dueDate = datetime.date.today()
        self.__borrowerID = None

    def getTitle(self):
        return self.__title

    def borrow(self):
        print("Borrowing Item Now...")
        self.__onLoan = True
        self.__borrowerID = input("BorrowerID: ")
        self.__dueDate = self.__dueDate + datetime.timedelta(weeks=3)

    def returnback(self):
        print("Returning Item Now..")
        self.__onLoan = False
        self.__borrowerID = input("BorrowerID: ")

    def printInfo(self):
        print("{0}; {1};".format(self.__title, self.__author), end=" ")
        print("{0}; {1}; {2}; Borrowed by: {3}\
            ".format(self.__itemID, self.__onLoan, self.__dueDate, self.__borrowerID))

    def showMenu():
        print("Welcome to the library management system!\
            \n1 - Add a new borrower\n2 - Add a new book\n3 - Add a new CD\
            \n4 - Borrow a book\n5 - Return a book\n6 - Borrow a CD\
            \n7 - Return a CD\n8 - Request book\n9 - Show all infomation\
            \n0 - Exit")
        choice = input("Enter your choice: ")
        print(choice)

class Book(LibItem):
    def __init__(self, t, a, i):
        super(Book, self).__init__(t, a, i)
        self.__reqState = False
        self.__reqBy = 0

    def getReqState(self):
        return self.__reqState

    def setReqState(self):
        self.__reqState = True
        self.__reqBy = input("RequestorID: ")

    def getInfo(self):
        print("Book Info:")
        LibItem.printInfo(self)
        print(self.__reqState)

class CD(LibItem):
    def __init__(self, t, a, i):
        super(CD, self).__init__(t, a, i)
        self.__genre = ""

    def getGenre(self):
        return self.__genre

    def setGenre(self, g):
        self.__genre = g

    def getInfo(self):
        print("CD Info:")
        LibItem.printInfo(self)

Title, Author, ItemID = input("Title: "), input("Author: "), input("ItemID: ")
thisBook = Book(Title, Author, ItemID)
Title, Artist, ItemID = input("Title: "), input("Artist: "), input("ItemID: ")
thisCD = CD(Title, Artist, ItemID)

thisBook.getInfo()
thisCD.getInfo()
thisBook.borrow()
thisBook.getInfo()
thisBook.returnback()
thisBook.getInfo()
