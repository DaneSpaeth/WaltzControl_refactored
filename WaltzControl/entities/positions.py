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
        
    def change_ra(self, ra):
        """change ra.
        
           Input: ra in hours as float
        """
        self.ra = ra
        
    def change_dec(self, dec):
        """Change dec.
        
           Input: dec in hours as float
        """
        self.dec = dec
    
    def change_position(self, ra, dec):
        """Update ra and dec.
        
           Input: ra in hours as float
                  dec in degrees as float
        """
        self.change_ra(ra)
        self.change_dec(dec)
        
class HorizontalPositionHA(HorizontalPosition):
    """Contains horizontal on sky position with hour angle (ra, dec, ha).
    
       ra in hours as float
       dec in hours as float
       ha in hours as float.
    """
    def __init__(self, ra, dec, ha = None):
        """Construct instance.
        
           Input: instance
                  ra in hours as float
                  dec in degrees as float
                  ha in hours as float
        """
        super().__init__(ra, dec)
        self.ha = ha
        
    def change_ha(self, ha):
        """Change ha.
        
           Input: ha as float.
        """
        self.ha = ha
        
    def change_position(self, ra, dec, ha = None):
        """Update ra, dec and (optionally) ha.
        """
        super().change_position(ra, dec)
        if ha:
            self.change_ha(ha)
        
           
        



    
