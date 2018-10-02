def calculate_hour_angle(ra, LST):
        """ Calculate hour angle.
        
            Input: ra as float
                   LST as float
            
            Output: ha as float
        """
        #Compute the hour angle in range [-12,12]
        ha = LST - ra
        #hour angles larger than 12 should be converted to negative numbers
        #e.g. 13 to -11
        if ha > 12:
            ha = ha - 24
        if ha <= -12:
            ha = ha + 24
        
        return ha