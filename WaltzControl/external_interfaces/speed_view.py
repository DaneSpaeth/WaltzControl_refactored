"""View for Speed Radiobuttons."""
import tkinter as tk

class SpeedView(tk.Frame):
    """View for Speed Radiobuttons."""
    def __init__(self, speed_view_model, user_control, parent, *args, **kwargs):
        """Contruct instance.
        
           Input: Injection of speed_view_model instance
                  Injection of UserController instance
                  Parent window instance.
        """
        super().__init__()
        
        self.speed_view_model = speed_view_model
        self.user_control = user_control
        
        radiobutton_parameters=[('Slew', 0, self.set_speed_slew_click),
                                ('Find', 1, self.set_speed_find_click),
                                ('Center', 2,
                                 self.set_speed_center_click),
                                ('Guide', 3, self.set_speed_guide_click)]
        self.speed = tk.StringVar()
        #Initialize speed to guiding speed
        #Link StringVar to View Model. This is done after every click.
        #This aims to keep the View and View Model synchronized.
        #However we do not check in a background loop if speed is still accurate
        #But not really useful since we dont get replies of telescope controller
        #when seting speeds
        self.speed.set(self.speed_view_model.speed)
        
        for keyword, position, execute in radiobutton_parameters:
            self.speed_radiobutton= tk.Radiobutton(self,
                                                text=keyword,
                                                variable=self.speed,
                                                value=keyword,
                                                command=execute,
                                                font=('arial', 10, 'bold'))
            self.speed_radiobutton.grid(row=position,column=0,sticky=tk.W)
            
    def set_speed_slew_click(self):
        """Sends command to user_control instance and checks variable 
           of speed_view_model."""
        self.user_control.set_speed_slew()
        self.speed.set(self.speed_view_model.speed)
        
    def set_speed_find_click(self):
        """Sends command to user_control instance and checks variable 
           of speed_view_model."""
        self.user_control.set_speed_find()
        self.speed.set(self.speed_view_model.speed)
        
    def set_speed_center_click(self):
        """Sends command to user_control instance and checks variable 
           of speed_view_model."""
        self.user_control.set_speed_center()
        self.speed.set(self.speed_view_model.speed)
        
    def set_speed_guide_click(self):
        """Sends command to user_control instance and checks variable 
           of speed_view_model."""
        self.user_control.set_speed_guide()
        self.speed.set(self.speed_view_model.speed)
        