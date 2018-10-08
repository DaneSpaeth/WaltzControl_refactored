"""View for Speed Radiobuttons.

   Not fully complete yet. Look at comments in code"""
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
        
        radiobutton_parameters=[('Slew', 0, self.user_control.set_speed_slew),
                                ('Find', 1, self.user_control.set_speed_find),
                                ('Center', 2,
                                 self.user_control.set_speed_center),
                                ('Guide', 3, self.user_control.set_speed_guide)]
        #right now I do not check whether Output is up to date with view_model
        #because I do not want to have another rather unnecessary background loop
        #we could change that later but maybe not necessary since we dont really
        #have a possibility to check setting of speeds anyway. So Maybe just
        #leave it like that. Wait for experience with using program
        self.speed = tk.StringVar()
        #Initialize speed to guiding speed
        self.speed.set(self.speed_view_model.speed)
        
        for keyword, position, execute in radiobutton_parameters:
            self.speed_radiobutton= tk.Radiobutton(self,
                                                text=keyword,
                                                variable=self.speed,
                                                value=keyword,
                                                command=execute,
                                                font=('arial', 10, 'bold'))
            self.speed_radiobutton.grid(row=position,column=0,sticky=tk.W)
