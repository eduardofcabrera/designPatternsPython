from urllib.parse import _NetlocResultMixinStr


from abc import ABCMeta, abstractmethod

class You:
    def __init__(self):
        print('You: Lets buy')
        self.debitCard = DebitCard()
        self.isPurchased = None
    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    
    def __del__(self):
        if self.isPurchased:
            print('Yes')
        else: print('No')

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    
    def __getAccount(self):
        self.account = self.card
        return self.account
    
    def __hasFunds(self):
        print('Bank: Checking account:', self.__getAccount(), 'has enough funds')
        return True
    
    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print('Bank: Paying')
            return True
        else:
            print('Bank: Sorry')
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Proxy: Card Number: ')
        self.bank.setCard(card)
        return self.bank.do_pay()

you = You()
you.make_payment()