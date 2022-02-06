class MetaSingleton(type):
    _instances = {}
    count = 0
    def __call__(cls, *args, **kwargs):
        cls.count += 1
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class counterProxy(metaclass=MetaSingleton):

    obj = None
    def do_something(self):
        if not self.obj:
            self.obj = RealObject()
        self.obj.do_something()

class RealObject(object):
    def __init__(self):
        pass
    
    def do_something(self):
        print('SOMETHING')