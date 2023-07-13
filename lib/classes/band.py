from classes.concert import Concert

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise Exception
        
    def get_hometown(self):
        return self._hometown
    
    def set_hometown(self, hometown):
        if type(hometown) == str and len(hometown) > 0:
            self._hometown = hometown
        else:
            raise Exception
        
    name = property(get_name, set_name)
    hometown = property(get_hometown, set_hometown)
    concerts = Concert.all

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        return new_concert
    
    def all_introductions(self):
        return [concert.introduction() for concert in Concert.all if concert.band == self]