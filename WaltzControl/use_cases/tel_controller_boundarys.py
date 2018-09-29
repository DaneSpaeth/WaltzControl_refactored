"""Boundarys for Responses from TelescopeController (TC) and Requests to TC.
   Data entry and exit point into use_cases layer.
"""

class TelescopeControllerResponseBoundary:
    """Contains Responses from TelescopeController Device.
    """
    def __init__(
        self,
        ra_response = None,
        dec_response = None,
        validate_response = None):
        """Store Responses of Telescope Controller as floats.
        """
        self.ra_response = ra_response
        self.dec_response = dec_response
        self.validate_response = validate_response
        
    def set_ra_response(self, ra):
        """Set ra response.
           
           Input: ra as float in hours
        """
        self.ra_response = ra
        
    def set_dec_response(self, dec):
        """Set dec response.
           
           Input: dec as float in degrees
        """
        self.dec_response = dec
        
    def set_validate_response(self, valid):
        """Set validate response.
           
           Input: valid as boolean (accounts for Returns of Telesope Controllere
                                    to set_target etc)
                                    
        """
        self.validate_response = valid
        
    def reset_responses(self):
        """Reset all responses to None.
        """
        self.ra_response = None
        self.dec_response = None
        self.validate_response = None
        
    def retrieve_position(self):
        """Returns ra and dec_responses.
        """
        return (self.ra_response, self.dec_response)
    
class TelescopeControllerRequestBoundary:
    """Interface for commands to TelescopeController Device.
    """
    def __init__(self):
        pass
        
    def request_position(self):
        pass
