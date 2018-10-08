import tkinter as tk

#from interface_adapters.view_models import PositionViewModel

class OutputView(tk.Frame):
    """View for Positions"""

    def __init__(self, pos_view_model, time_view_model, parent, *args, **kwargs):
        """Constructor method.
           
           Inject pos_view_model, time_view_model and parent frame.
        """
        super().__init__(parent, *args, **kwargs)

        self.pos_view_model = pos_view_model
        self.time_view_model = time_view_model
        
        #Store Time
        self.LST = tk.StringVar()
        self.LT = tk.StringVar()
        self.UTC = tk.StringVar()
        self.LST.set(self.time_view_model.LST)
        self.LT.set(self.time_view_model.LT)
        self.UTC.set(self.time_view_model.UTC)
        #Store Position
        self.ra = tk.StringVar()
        self.dec = tk.StringVar()
        self.ha = tk.StringVar()
        self.ra.set(self.pos_view_model.ra)
        self.dec.set(self.pos_view_model.dec)
        self.ha.set(self.pos_view_model.ha)
        
        #Display Time
        self.LST_label= tk.Label(self,
                                 font=('arial', 15, 'bold'),
                                text= "LST")
        self.LST_label.grid(row = 0, column = 0)
        
        self.LST_display= tk.Label(self,
                                   font=('arial', 20, 'bold'), 
                                  bg='light green',
                                  textvariable = self.LST)
        self.LST_display.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.LT_label= tk.Label(self,
                                font=('arial', 15, 'bold'),
                                text= "LT")
        self.LT_label.grid(row = 0, column = 2)
        
        self.LT_display= tk.Label(self,
                                  font=('arial', 20, 'bold'), 
                                  bg='light green',
                                  textvariable = self.LT)
        self.LT_display.grid(row = 0, column = 3, padx = 10, pady = 10)
        
        self.UTC_label= tk.Label(self,
                                 font=('arial', 15, 'bold'),
                                text= "UTC")
        self.UTC_label.grid(row = 0, column = 4)
        
        self.UTC_display= tk.Label(self,
                                   font=('arial', 20, 'bold'), 
                                  bg='light green',
                                  textvariable = self.UTC)
        self.UTC_display.grid(row = 0, column = 5, padx = 10, pady = 10)
        
        #Store position
        self.RA_label= tk.Label(self,
                                font=('arial', 15, 'bold'),
                                text= "RA")
        self.RA_label.grid(row = 1, column = 0)
        
        self.RA_display= tk.Label(self,
                                  font=('arial', 20, 'bold'), 
                                  bg='light green',
                                  textvariable = self.ra)
        self.RA_display.grid(row = 1, column = 1)
        
        self.DEC_label= tk.Label(self,
                                 font=('arial', 15, 'bold'),
                                 text= "DEC")
        self.DEC_label.grid(row = 1, column = 2)
        
        self.DEC_display= tk.Label(self,
                                   font=('arial', 20, 'bold'),
                                   bg='light green',
                                   textvariable = self.dec)
        self.DEC_display.grid(row = 1, column = 3)
        
        self.HA_label= tk.Label(self,
                                font=('arial', 15, 'bold'),
                                 text= "HA")
        self.HA_label.grid(row = 1, column = 4)
        
        self.HA_display= tk.Label(self,
                                  font=('arial', 20, 'bold'),
                                   bg='light green',
                                   textvariable = self.ha)
        self.HA_display.grid(row = 1, column = 5)
        
        self.refresh_times()
        self.refresh_coordinates()
        
        
    def refresh_ra(self):
        """Refreshes ra StringVar."""
        self.ra.set(self.pos_view_model.ra)
        
    def refresh_dec(self):
        """Refreshes dec StringVar."""
        self.dec.set(self.pos_view_model.dec)
        
    def refresh_ha(self):
        """Refreshes ha StringVar."""
        self.ha.set(self.pos_view_model.ha)
        
    def refresh_LST(self):
        """Refreshes LST StringVar."""
        self.LST.set(self.time_view_model.LST)
        
    def refresh_LT(self):
        """Refreshes LT StringVar."""
        self.LT.set(self.time_view_model.LT)
        
    def refresh_UTC(self):
        """Refreshes UTC StringVar."""
        self.UTC.set(self.time_view_model.UTC)
        
    def refresh_coordinates(self):
        """Refreshes coordinates and calls itself."""
        self.refresh_ra()
        self.refresh_dec()
        self.after(500, self.refresh_coordinates)
        
    def refresh_times(self):
        """Refreshes times and calls itself."""
        self.refresh_LST()
        self.refresh_LT()
        self.refresh_UTC()
        self.refresh_ha()
        self.after(200, self.refresh_times)
