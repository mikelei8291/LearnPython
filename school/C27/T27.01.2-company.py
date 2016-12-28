class company():
    def __init__(self, name, email):
        super(company, self).__init__()
        self.__name = name
        self.__email = email
        self.__contactDate = None

    def setContactDate(self, d):
        self.__contactDate = d

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getContactDate(self):
        return self.__contactDate

thisCompany = company("Thunder Studio", "contact@thunder.studio")
thisCompany.setContactDate("2016.12.12")
print(thisCompany.getName(), thisCompany.getEmail(), thisCompany.getContactDate())
