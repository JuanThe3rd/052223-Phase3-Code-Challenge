class Concert:
    all = []
    
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        self.add_concert(self)

    @classmethod
    def add_concert(cls, concert):
        cls.all.append(concert)

    def get_date(self):
        return self._date
    
    def set_date(self, date):
        if type(date) == str and len(date) > 0:
            self._date = date
        else:
            raise Exception
        
    def get_band(self):
        return self._band
    
    def set_band(self, band):
        from classes.band import Band

        if isinstance(band, Band):
            self._band = band
        else:
            raise Exception
        
    def get_venue(self):
        return self._venue
    
    def set_venue(self, venue):
        from classes.venue import Venue

        if isinstance(venue, Venue):
            self._venue = venue
        else:
            raise Exception
        
    date = property(get_date, set_date)
    band = property(get_band, set_band)
    venue =  property(get_venue, set_venue)

    def hometown_show(self):   
        return self.venue.city == self.band.hometown

    def introduction(self):
        city = self.venue.city

        return (f'Hello {city}!!!!!, we are {self.band.name} and we\'re from {self.band.hometown}')
    
    '''
        It seems that the units tests have conflicting prompts when it comes to 
        whether the venue city input 'Sac' should output as 'Sac' or 'SAC'.
        The unit test for Concert.introduction() tells us that the intro should
        read 'Hello Sac!!!!!...' whereas the Band.all_introductions() tells us 
        that the intro should read 'Hello SAC!!!!!...
    '''