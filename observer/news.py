from abc import ABC, ABCMeta, abstractmethod
from hashlib import new

class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass

class NewsPublisher():
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    
    def attach(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubcribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addNews(self, news):
        self.__latestNews = news
    
    def getNews(self):
        return self.__latestNews
    
class SMSSubscriber:
    def __init__(self, publisher: NewsPublisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber:
    def __init__(self, publisher: NewsPublisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class AnotherSubscriber:
    def __init__(self, publisher: NewsPublisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

if __name__ == '__main__':
    np = NewsPublisher()

    sms = SMSSubscriber(np)
    email = EmailSubscriber(np)
    another = AnotherSubscriber(np)

    print(np.subscribers())

    np.addNews('Hello World')
    np.notifySubcribers()

    np.detach()
    np.subscribers()

    np.addNews('second news')
    np.notifySubcribers()