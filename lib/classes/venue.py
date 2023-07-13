from classes.concert import Concert

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    def get_title(self):
        return self._title

    def set_title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception
        
    def get_city(self):
        return self._city
    
    def set_city(self, city):
        if type(city) == str and len(city) > 0:
            self._city = city
        else:
            raise Exception
        
    title = property(get_title, set_title)
    city = property(get_city, set_city)

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        return [concert.band for concert in Concert.all if concert.venue == self]
    
    def concert_on(self, date):
        for concert in Concert.all:
            if concert.date == date:
                return concert
            
        return None
    
