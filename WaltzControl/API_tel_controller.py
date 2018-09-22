from API_string_to_float_trafo import high_prec_to_float
from UC_tel_controller_boundarys import TelescopeControllerOutputBoundary

class TelescopeControllerAPI(TelescopeControllerOutputBoundary):
    """API to define interaction with serial connection.
    """
    def __init__(self, UC_input, tel_connection):
        self.UC_input = UC_input
        self.tel_connection = tel_connection
    
    def send_ra_response(self, ra):
        """Sends ra response to Input boundary in Use Cases.
        
           Input: ra in hours as float.
        """
        self.UC_input.set_ra_response(ra)
        
    def send_dec_response(self, dec):
        """Sends dec response to Input boundary in Use Cases.
        
           Input: dec in degrees as float.
        """
        self.UC_input.set_dec_response(dec)
        
    def request_position(self):
        """Request position from serial connection, 
           transform to floats and send to UC input.
        """
        string_ra = self.tel_connection.get_ra()
        string_dec = self.tel_connection.get_dec()
        
        ra_float=high_prec_to_float(string_ra)
        dec_float=high_prec_to_float(string_dec)
        
        self.send_ra_response(ra_float)
        self.send_dec_response(dec_float)
        
class TelescopeConnectionInterface:
    """Interface for Telescope Connection.
    """
    def __init__(self):
        pass
    def get_ra(self):
        raise NotImplementedError
    def get_dec(self):
        raise NotImplementedError
        
        
    
    
