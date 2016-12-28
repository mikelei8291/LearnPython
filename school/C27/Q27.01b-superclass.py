class BankAccount():
    def __init__(self, n):
        super(BankAccount, self).__init__()
        self.__holderName = ""
        self.__iban = n

    def setHolderName(self, t):
        self.__holderName = t

    def getHolderName(self):
        return self.__holderName

    def getIban(self):
        return self.__iban
