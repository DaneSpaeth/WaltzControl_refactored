"""Sontains simple data structures for displaying data.
"""

class PositionViewModel:
    """Contains positions as strings.
    """
    def __init__(self):
        self.ra  = ''
        self.dec = ''
        self.ha = ''
        
class TimeViewModel:
    """Contains times as strings.
    """
    def __init__(self):
        self.LST = ''
        self.LT = ''
        self.UTC = ''
        
