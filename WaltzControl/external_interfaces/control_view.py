import tkinter as tk

class ControlView(tk.Frame):
    """View for Movement Controls."""
    def __init__(self, user_control, parent, *args, **kwargs):
        """Contruct instance.
        
           Input: Injection of UserController instance
                  Parent window instance.
        """
        super().__init__(parent, *args, **kwargs)
        
        self.user_control = user_control
        
        self.south_button = tk.Button(text="S",
                                   font=('arial', 20, 'bold'),
                                   bg='LightGrey',
                                   height = 1, 
                                   width = 2)
        self.south_button.grid(row=0,column=1)
        
        self.west_button = tk.Button(text="W",
                                  font=('arial', 20, 'bold'),
                                  bg='LightGrey',
                                  height = 1,
                                  width = 2)
        self.west_button.grid(row=1,column=0)
        
        self.east_button = tk.Button(text="E",
                                  font=('arial', 20, 'bold'),
                                  bg='LightGrey',
                                  height = 1,
                                  width = 2)
        self.east_button.grid(row=1,column=2)
        
        
        self.north_button = tk.Button(text="N",
                                   font=('arial', 20, 'bold'),
                                   bg='LightGrey',
                                   height = 1,
                                   width = 2)
        self.north_button.grid(row=2,column=1)
        
        self.stop_button = tk.Button(text="STOP",
                                  font=('arial',20, 'bold'),
                                  fg='White',
                                  bg='Red',
                                  activeforeground='Red',
                                  activebackground='White')
        self.stop_button.grid(row=3,column=0, columnspan=3, pady=10)
