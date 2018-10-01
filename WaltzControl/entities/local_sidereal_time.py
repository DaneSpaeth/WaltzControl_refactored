"""Conatins various classes for storing times."""
from astropy.time import Time

class LocalSiderealTime:
    """Stores LocalSiderealTime."""
    def __init__(self, LST_string = '', LST_float = 0):
        """Initiliaze LocalSiderealTime.
           
           Input: (Optional) LST.
        """
        self.as_string = LST_string
        self.as_float = LST_float
        
    def _retrieve(self):
        """ Retrieve the current Local Sidereal Time from Astropy.
        """
        #Get current UTC from astropy.Time
        UTC_now=Time.now()
        #Convert to LST
        LST_now=UTC_now.sidereal_time('mean',longitude=8.724700212478638)
        LST_now=str(LST_now)
        return LST_now
    
    def _format(self, LST_now):
        """Format retrieved LST to string and float"""
        (hours,h,rest)=LST_now.partition('h')
        #Add a zero to hours if single number
        hours=int(hours)
        (minutes,m,rest)=rest.partition('m')
        minutes=int(minutes)
        (seconds,s,rest)=rest.partition('s')
        #For different purposes compute LST as a float in hours.
        LST_float=int(hours) + int(minutes)/60. + float(seconds)/3600.
        #Round the seconds (format 12.545 to 13)
        #We want to round to get a more continous refreshing of the seconds
        seconds=round(float(seconds))
        #With rounding we could get 60 for seconds
        #In that case increse minutes by 1 and set seconds to 0
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
        if minutes == 60:
            minutes = 0
            hours = hours + 1
        if hours == 24:
            hours = 0
        LST_string='{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
        
        return LST_string, LST_float
    
    def refresh(self):
        """Update LST."""
        LST_now = self._retrieve()
        LST_string, self.as_float = self._format(LST_now)
        
        #Only update string if string has changed."""
        if self.as_string != LST_string:
            self.as_string = LST_string


        
        
        


