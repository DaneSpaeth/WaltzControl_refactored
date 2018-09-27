"""Float to string conversions.
"""
def float_to_hms(pos_float):
    """Calculate hours, minutes, seconds of arbitrary positive float.
       
       Input: pos_float: positive input float
       
       Output: hours, minutes, seconds
    """
    hours = int(pos_float)
    rest = (pos_float-hours)*60
    minutes = int(rest)
    rest = (rest-minutes)*60
    seconds=round(rest)
    
    #But we have to take care of rounding up to 60. 
    #Increase minutes by one in that case.
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
        
    return (hours, minutes, seconds)
    

def ra_float_to_high_prec(ra_float):
    """Transforms float to high precision ra string in hours.
    
       Input: float in hours 
                                     
       Output: High precision ra string (HHhMMmSSs)
    """
    #Check if float is in range [0,24)
    if ra_float < 0 or ra_float >= 24:
        raise ValueError
    #ra do not contain signs
    #Calculate hours, minutes, seconds
    hours, minutes, seconds = float_to_hms(ra_float)
    #24hours should be converted to 0hours
    if hours == 24:
        hours = 0
    ra_float='{:02}h{:02}m{:02}s'.format(hours,minutes,seconds)
    
    return ra_float

def dec_float_to_high_prec(dec_float):
    """Transforms float to high precision dec string in degrees.
    
       Input: float in hours 
                                     
       Output: High precision ra string (HHhMMmSSs)
    """
    #Check if float is in range [-90,90]
    if dec_float < -90 or dec_float > 90:
        raise ValueError
    #dec contain signs
    if dec_float >= 0:
        sign='+'
    if dec_float < 0:
        sign='-'
    #Calculate degrees, minutes, seconds with the absolute of the dec_float
    degrees, minutes, seconds = float_to_hms(abs(dec_float))
    
    ra_float='''{}{:02}°{:02}'{:02}"'''.format(sign, degrees, minutes, seconds)
    
    return ra_float


    
