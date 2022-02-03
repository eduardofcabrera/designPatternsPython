class Borg:
    __shared_state = {'1': '2'}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

class Borg_2(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg_2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

b = Borg()
b1 = Borg()

b.x = 4

print('b', b)
print('b1', b1)
print('bState', b.__dict__)
print('b1State', b1.__dict__)