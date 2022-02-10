from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):

    @abstractmethod
    def Handle(self):
        pass

class ConcreteStateA(State):
    def Handle(self):
        print("A")

class ConcreteStateB(State):
    def Handle(self):
        print("B")

class Context(State):

    def __init__(self):
        self.state: State = None

    def getState(self):
        return self.state

    def setState(self, state: State):
        self.state = state
    
    def Handle(self):
        self.state.Handle()

context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()

context.setState(stateA)
context.Handle()