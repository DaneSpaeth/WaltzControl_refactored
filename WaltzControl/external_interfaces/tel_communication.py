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
    
    def move_west(self):
        """Move Telescope West.
        
           Returns nothing.
        """
        self.ser.write(lx.move_telescope_west())
        
    def move_east(self):
        """Move Telescope East.
        
           Returns nothing.
        """
        self.ser.write(lx.move_telescope_east())
        
    def move_north(self):
        """Move Telescope North.
        
           Returns nothing.
        """
        self.ser.write(lx.move_telescope_north())
        
    def move_south(self):
        """Move Telescope South.
        
           Returns nothing.
        """
        self.ser.write(lx.move_telescope_south())
        
    def stop_west(self):
        """Stop Telescope West.
        
           Returns nothing.
        """
        self.ser.write(lx.stop_telescope_west())
        
    def stop_east(self):
        """Stop Telescope East.
        
           Returns nothing.
        """
        self.ser.write(lx.stop_telescope_east())
        
    def stop_north(self):
        """Stop Telescope North.
        
           Returns nothing.
        """
        self.ser.write(lx.stop_telescope_north())
        
    def stop_south(self):
        """Stop Telescope South.
        
           Returns nothing.
        """
        self.ser.write(lx.stop_telescope_south())
        
    def set_speed_guide(self):
        """Set speed to guide speed.
        
           Returns nothing.
        """
        self.ser.write(lx.set_telescope_speed_guide())
        
    def set_speed_center(self):
        """Set speed to center speed.
        
           Returns nothing.
        """
        self.ser.write(lx.set_telescope_speed_center())
    
    def set_speed_find(self):
        """Set speed to find speed.
        
           Returns nothing.
        """
        self.ser.write(lx.set_telescope_speed_find())
        
    
    def set_speed_slew(self):
        """Set speed to slew speed.
        
           Returns nothing.
        """
        self.ser.write(lx.set_telescope_speed_slew())
        
    def toggle_precision(self):
        """Toggle Precision.
        
           Returns nothing.
        """
        self.ser.write(lx.toggle_telescope_precision())
        
           
        
    
    
    
    
        
        
