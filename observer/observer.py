class Subject:
    def __init__(self):
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f'{type(self).__name__} got {args} from {subject}')

class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f'{type(self).__name__} got {args} from {subject}')

subject = Subject()
ob1 = Observer1(subject)
ob2 = Observer2(subject)
subject.notifyAll('notification')