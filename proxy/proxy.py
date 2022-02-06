class Actor(object):
    def __init__(self):
        self.isBusy = False
    
    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, 'is occupied with current movie')

    def avaible(self):
        self.isBusy = False
        print(type(self).__name__, 'is free for the current movie')

    def getStatus(self):
        return self.isBusy

class Agent(object):
    def __init__(self):
        self.principal = None
        self.actor = None

    def work(self):
        if not self.actor:
            self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.avaible()

if __name__ == '__main__':
    r = Agent()
    r.work()