"""Contains Various Classes for storing telescope positions.
"""
class HorizontalPosition:
    """Contains horizontal on sky position (ra, dec).
    
       ra in hours as float
       dec in degrees as float
    """
    def __init__(self, ra, dec):
        """Construct instance.
        
           Input: instance
                  ra in hours as float
                  dec in degrees as float
        """
        self.ra = ra
        self.dec = dec
        
    def change_ra(self,ra):
        """change ra.
        
           Input: ra in hours as float
        """
        self.ra = ra
        
    def change_dec(self,dec):
        """Update dec.
        
           Input: dec in hours as float
        """
        self.dec = dec
    
    def change_position(self,ra,dec):
        """Update ra and dec.
        
           Input: ra in hours as float
                  dec in degrees as float
        """
        self.change_ra(ra)
        self.change_dec(dec)
        



    
