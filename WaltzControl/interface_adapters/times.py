"""Contains Various Classes for storing Times.
   LT and UTC, as those are not needed for any calculations and only have to 
   be displayed.
"""
import time
import datetime

class LocalTime:
    """Store Local Time (LT)."""
    def __init__(self, LT_string = ''):
        """Initialize LocalTime instance.
        
           Input (optional): LT as as_string
        """
        self.as_string = LT_string
        
    def refresh(self):
        """Sets as_string."""
        # get the current local time from the PC
        LT_now = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if LT_now != self.as_string:
            self.as_string = LT_now
            
class CoordinatedUniversalTime:
    """Store Coordinated Universal Time (UTC)."""
    def __init__(self, UTC_string = ''):
        """Initialize CoordinatedUniversalTime Instance.
        
           Input (optional): UTC as string.
        """
        self.as_string = UTC_string
    
    def refresh(self):
        """Sets as_string."""
        #Get current UTC from datetime
        UTC_now = datetime.datetime.utcnow().strftime("%H:%M:%S")
        #Check if UTC has changed since last call
        if UTC_now != self.as_string:
            #Save current UTC in self.UTC
            self.as_string = UTC_now
            

 
