class Singleton(object):
    def __new__(cls): # method to create new objects
        if not hasattr(cls, 'instance'): # check if an object already exists
            cls.instance = super(Singleton, cls).__new__(cls) # create if no exist
        return cls.instance # return the created or the exist object

s = Singleton()

print(s)

s1 = Singleton()

print(s1)

print(s == s1)


