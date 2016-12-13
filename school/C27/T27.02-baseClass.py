import datetime
class LibItem():
    def __init__(self, t, a, i):
        super(LibItem, self).__init__()
        self.__title = t
        self.__author = a
        self.__itemID = i
        self.__onLoan = False
        self.__dueDate = datetime.date.today()

    def getTitle(self):
        return self.__title

    def borrow(self):
        self.__onLoan = True
        self.__dueDate = self.__dueDate + datetime.timedelta(weeks=3)

    def returnback(self):
        self.__onLoan = False

    def printInfo(self):
        print("%s; %s;", end="" % (self.__title, self.__author))
        print("%s; %s; %s" % (self.__itemID, self.__onLoan, self.__dueDate))

class Book(LibItem):
    def __init__(self, t, a, i):
        super(Book, self).__init__(t, a, i)
        self.__reqState = False
        self.__reqBy = 0

    def getReqState(self):
        return self.__reqState

    def setReqState(self):
        self.__reqState = True

class CD(LibItem):
    def __init__(self, t, a, i):
        super(CD, self).__init__(t, a, i)
        self.__genre = ""

    def getGenre(self):
        return self.__genre

    def setGenre(self, g):
        self.__genre = g

Title, Author, ItemID = input("Title: "), input("Author: "), input("ItemID: ")
thisBook = Book(Title, Author, ItemID)
Title, Artist, ItemID = input("Title: "), input("Artist: "), input("ItemID: ")
thisCD = CD(Title, Artist, ItemID)
