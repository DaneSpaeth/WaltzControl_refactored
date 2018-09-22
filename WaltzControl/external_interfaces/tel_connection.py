import time

from interface_adapters.tel_controller import (
	TelescopeConnectionInterface)

try:
    import serial
    print('Importing serial')
except ImportError:
    print('Importing fakeSerial')
    import external_interfaces.fakeSerial as serial

class Lx200TelConnection(TelescopeConnectionInterface):
    """Defines commands send to serial port using lx200 protocol.
    """
    def __init__(self,serial_connection):
        super().__init__()
        self.con = serial_connection
        
    def get_ra(self):
        """Send '#:GR#' to serial port.
        
           Output: Response string.
        """
        inp=b'#:GR#'
        self.con.write(inp)
        ra = self.con.get_response()
        return ra 
    
    def get_dec(self):
        """Send '#:GD#' to serial port.
        
           Output: Response string.
        """
        inp=b'#:GD#'
        self.con.write(inp)
        dec = self.con.get_response()
        return dec 
        

class SerialConnection(serial.Serial):
    def __init__(self):
        #Open serial connection
        super().__init__(port='/dev/ttyS0',baudrate = 9600,timeout = 1)
        
    def get_response(self):
        """Reads from the serial connection and returns response as a string"""
        response = b''
        time.sleep(0.1)
        while self.in_waiting > 0:
            response += super().read(1)
        response=response.decode()
        return response
    
        
