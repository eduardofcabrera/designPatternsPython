class EventManager(object):
    def __init__(self):
        print('Event Manager:; Let me talk to the folks\n')
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowersRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()

class Hotelier(object):
    def __init__(self):
        print('Arranging the Hotel for Marriage? --')
    
    def _isAvaible(self):
        print('Is the Hotel free for the event on given day?')
        return True
    
    def bookHotel(self):
        if self._isAvaible:
            print('Registered the Booking\n\n')
    
class Florist(object):
    def __init__(self):
        print("Flower decorations for the event? --")
    
    def setFlowersRequirements(self):
        print('Carnations, Roses and Lilies would be used for Decorations\n\n')

class Caterer(object):
    def __init__(self):
        print('Food arrangements for the event --')
    
    def setCuisine(self):
        print('Chinese and Continental Cuisine to be served\n\n')

class Musician(object):
    def __init__(self):
        print('Musical arrangements for the marriage --')
    
    def setMusicType(self):
        print('Jazz and Classical will be played\n\n')

class You(object):
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements??!!!')
    
    def askEventManager(self):
        print('You:: Lets contact the event manager\n\n')
        em = EventManager()
        em.arrange()
    
    def __del__(self):
        print('You:: Thanks!')

you = You()
you.askEventManager()