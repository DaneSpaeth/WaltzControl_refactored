class PositionUpdater:
    """Update Position Object.
    """
    def __init__(self, hor_position,
                 tel_controller_output,
                 tel_controller_input):
        """Create PositionUpdater instance.
           
           Input: Existing Horizontal Position instance.
                  Existing Telescope Controller instance
        """
        self.tel_controller_output = tel_controller_output
        self.tel_controller_input = tel_controller_input
        self.hor_position = hor_position
        
    def update_position(self, ra, dec):
        """Update HorizontalPosition instance.
        
           Input: RA in hours as float
                  Dec in degrees as float
        """
        self.hor_position.change_position(ra, dec)
        
    def request_and_update_position(self):
        """Request update from Telescope Controller Interface.
        """
        self.tel_controller_output.request_position()
        (ra, dec) = self.tel_controller_input.retrieve_position()
        self.update_position(ra, dec)
        

        
    
        
        