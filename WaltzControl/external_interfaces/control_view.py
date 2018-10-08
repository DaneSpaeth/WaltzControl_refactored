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
        
        self.south_button = tk.Button(self,
                                      text="S",
                                   font=('arial', 20, 'bold'),
                                   bg='LightGrey',
                                   height = 1, 
                                   width = 2)
        self.south_button.grid(row=0,column=1)
        
        
        self.west_button = tk.Button(self,
                                     text="W",
                                  font=('arial', 20, 'bold'),
                                  bg='LightGrey',
                                  height = 1,
                                  width = 2)
        self.west_button.grid(row=1,column=0)
        
        self.east_button = tk.Button(self,
                                     text="E",
                                  font=('arial', 20, 'bold'),
                                  bg='LightGrey',
                                  height = 1,
                                  width = 2)
        self.east_button.grid(row=1,column=2)
        
        
        self.north_button = tk.Button(self,
                                      text="N",
                                   font=('arial', 20, 'bold'),
                                   bg='LightGrey',
                                   height = 1,
                                   width = 2)
        self.north_button.grid(row=2,column=1)
        
        self.stop_button = tk.Button(self,
                                     text="STOP",
                                  font=('arial',20, 'bold'),
                                  fg='White',
                                  bg='Red',
                                  activeforeground='Red',
                                  activebackground='White')
        self.stop_button.grid(row=3,column=0, columnspan=3, pady=10)
        
        #Add Bindings
        self.enable_all_buttons()
        
    def enable_all_buttons(self):
        """Enables and binds all buttons."""
        for child in self.winfo_children():
            child.config(state='normal')
        
        self.north_button.bind("<ButtonPress-1>",
                               self.start_move_north_buttonclick)
        self.north_button.bind("<ButtonRelease-1>",
                               self.stop_move_north_buttonclick)
        self.west_button.bind("<ButtonPress-1>",
                              self.start_move_west_buttonclick)
        self.west_button.bind("<ButtonRelease-1>",
                              self.stop_move_west_buttonclick)
        self.south_button.bind("<ButtonPress-1>",
                               self.start_move_south_buttonclick)
        self.south_button.bind("<ButtonRelease-1>",
                               self.stop_move_south_buttonclick)
        self.east_button.bind("<ButtonPress-1>",
                              self.start_move_east_buttonclick)
        self.east_button.bind("<ButtonRelease-1>",
                              self.stop_move_east_buttonclick)
        
    def start_move_west_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.move_west()
        
    def stop_move_west_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.stop_west()
        
    def start_move_north_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.move_north()
        
    def stop_move_north_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.stop_north()
        
    def start_move_south_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.move_south()
        
    def stop_move_south_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.stop_south()
        
    def start_move_east_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.move_east()
        
    def stop_move_east_buttonclick(self, event):
        """ Calls corresponding method of user_control.
        """
        self.user_control.stop_east()
