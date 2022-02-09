from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print('Defining the Algo')
        self.operation2()
        self.operation1()

class ConcreteClass(AbstractClass):

    def operation1(self):
        print('OP1')

    def operation2(self):
        print('OP2')

class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()

client = Client()
client.main()