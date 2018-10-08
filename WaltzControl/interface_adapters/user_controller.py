"""Contains Controller class for controlling Inputs from User."""

class UserController:
    """Control Inputs from User."""
    def __init__(self, mover, speed_changer):
        """Contruct instance.
        
           Input: Injection of Mover instance.
                  Injection of SpeedChanger instance.
        """
        self.mover = mover
        self.speed_changer = speed_changer
    def move_west(self):
        """Trigger move_west use case in Mover instance."""
        self.mover.move_west()
    def move_east(self):
        """Trigger move_east use case in Mover instance."""
        self.mover.move_east()
    def move_north(self):
        """Trigger move_north use case in Mover instance."""
        self.mover.move_north()
    def move_south(self):
        """Trigger move_south use case in Mover instance."""
        self.mover.move_south()
    def stop_west(self):
        """Trigger stop_west use case in Mover instance."""
        self.mover.stop_west()
    def stop_east(self):
        """Trigger stop_east use case in Mover instance."""
        self.mover.stop_east()
    def stop_north(self):
        """Trigger stop_north use case in Mover instance."""
        self.mover.stop_north()
    def stop_south(self):
        """Trigger stop_south use case in Mover instance."""
        self.mover.stop_south()
    def set_speed_guide(self):
        """Trigger set_speed_guide use case in SpeedChanger instance."""
        self.speed_changer.set_speed_guide()
    def set_speed_center(self):
        """Trigger set_speed_center use case in SpeedChanger instance."""
        self.speed_changer.set_speed_center()
    def set_speed_find(self):
        """Trigger set_speed_find use case in SpeedChanger instance."""
        self.speed_changer.set_speed_find()
    def set_speed_slew(self):
        """Trigger set_speed_slew use case in SpeedChanger instance."""
        self.speed_changer.set_speed_slew()
    
