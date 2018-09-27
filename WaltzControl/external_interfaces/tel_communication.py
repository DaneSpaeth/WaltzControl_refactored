"""Defines Object managing communication with the telescope Controller.
   Also defines SerialConnection.
"""

import time

from interface_adapters.tel_controller import (
    TelescopeCommunicatorInterface)
import external_interfaces.lx200_commands as lx 

try:
    import serial
    print('Importing serial')
except ImportError:
    print('Importing fakeSerial')
    import external_interfaces.fakeSerial as serial        

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
    
class TelescopeCommunicator(TelescopeCommunicatorInterface):
    """Defines communication with Meade Telescope Controller.
    
       Uses Serial Connection and Lx200 commands.
    """
    def __init__(self):
        self.ser = SerialConnection()
        
    def get_ra(self):
        """Get Telescope Right Ascension.
        
           Output: RA as raw telescope output string.
        """
        self.ser.write(lx.get_telescope_ra())
        ra = self.ser.get_response()
        return ra
    
    def get_dec(self):
        """Get Telescope Declination.
        
           Output: DEC as raw telescope output string.
        """
        self.ser.write(lx.get_telescope_dec())
        dec = self.ser.get_response()
        return dec
    
    
    
        
        
