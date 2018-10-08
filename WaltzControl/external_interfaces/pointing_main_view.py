import tkinter as tk

from external_interfaces.position_view import OutputView
from external_interfaces.control_view import ControlView
from external_interfaces.interchange_view import InterchangeView
from external_interfaces.speed_view import SpeedView

class WaltzPointing(tk.Tk):
    """Main Window."""
    def __init__(self, pos_view_model, time_view_model, speed_view_model, 
                 user_control, *args, **kwargs):
        """Construct main window.
        
           Input: Injection of PositionViewModel instance
                  Injection of TimeViewModel instance
                  Injection of UserController instance
        """
        super().__init__(*args, **kwargs)
        self.title("WaltzControl")
        #self.geometry("800x600")
        self.resizable(width=False, height=False)
        
        self.position_view = OutputView(pos_view_model, time_view_model, self)
        self.control_view = ControlView(user_control, self)
        self.interchange_view = InterchangeView(self.control_view, self)
        self.speed_view = SpeedView(speed_view_model, user_control, self)
        
        self.position_view.grid(row = 0,columnspan = 3)
        
        self.control_view.grid(row = 1, column = 1, pady = 10)
        self.interchange_view.grid(row = 1, column = 0, pady = 10)
        self.speed_view.grid(row = 1, column = 2, pady = 10)

if __name__ == '__main__':
    WP = WaltzPointing()
    WP.mainloop()