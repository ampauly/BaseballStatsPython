class Player():
    """Represents a player"""
    def __init__(self, firstName, lastName, year, baDiff, slgDiff, avgEv):
        self.firstName = firstName
        self.lastName = lastName
        self.year = year
        self.baDiff = baDiff
        self.slgDiff = slgDiff
        self.avgEv = avgEv

    def return_year(self):
        """Returns the player's year"""
        return self.year

    def return_baDiff(self):
        """Returns batting average ae"""
        return self.baDiff

    def return_baSLG(self):
        """Returns slg ae"""
        return self.slgDiff

    def return_avgEv(self):
        """Returns average exit velocity"""
        return self.avgEv

    def toString(self):
        """Prints out a player object"""
        return self.firstName + self.lastName + self.baDiff + self.slgDiff + self.avgEv
    