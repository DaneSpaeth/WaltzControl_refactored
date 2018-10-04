"""Contains class for Telescope Movements."""

class Mover:
    """Use Case for Telescope Movements."""
    def __init__(self, tel_controller):
        """Construct Instance.
        
           Input: Injection of TelescopeControllerAPI instance.
        """
        self.tel_controller = tel_controller
        
    def move_west(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.move_west()
        
    def move_east(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.move_east()
        
    def move_north(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.move_north()
        
    def move_south(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.move_south()
        
    def stop_west(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.stop_west()
        
    def stop_east(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.stop_east()
        
    def stop_north(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.stop_north()
        
    def stop_south(self):
        """Send command to TelescopeControllerAPI instance."""
        self.tel_controller.stop_south()
        
    
        
