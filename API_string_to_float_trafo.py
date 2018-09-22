"""String to float conversions.
"""
def high_prec_to_float(string):
    """Transforms high precision string to float.
    
       Input: High precision string 
       (e.g HH:MM:SS, HHhMMmSSs, sDD:MM:SS, sDD°MM°SS)
                                     
       Output: Value as float
    """
    #Check if high precision string by looking at the length
    if len(string) < 8 or len(string) > 10:
        raise ValueError
    #ra do not contain signs, dec does. Retrieve sign from dec and remove it 
    #from string
    if string[0] == '+' or string[0] == '-':
        sign = int(string[0]+'1')
        string = string[1:]
    else:
        sign = +1
    #Perform the actual transformation
    float_value = sign*(int(string[0:2])+
                        int(string[3:5])/60.+
                        int(string[6:8])/3600.)
    
    return float_value


    
