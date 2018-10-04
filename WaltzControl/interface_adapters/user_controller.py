"""Contains Controller class for controlling Inputs from User."""
from use_cases.movements import Mover


class UserController:
    """Control Inputs from User."""
    def __init__(self, mover):
        """Contruct instance.
        
           Input: Injection of Mover instance.
        """
        self.mover = Mover
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
        """Trigger stop_west use casein Mover instance."""
        self.mover.stop_west()
    def stop_east(self):
        """Trigger stop_east use casein Mover instance."""
        self.mover.stop_east()
    def stop_north(self):
        """Trigger stop_north use casein Mover instance."""
        self.mover.stop_north()
    def stop_south(self):
        """Trigger stop_south use casein Mover instance."""
        self.mover.stop_south()