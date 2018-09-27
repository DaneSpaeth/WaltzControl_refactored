import tkinter as tk

from interface_adapters.view_models import PositionViewModel

class PositionView(tk.Frame):
    """View for Positions"""

    def __init__(self, pos_view_model, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.pos_view_model = pos_view_model
        
        self.ra = tk.StringVar()
        self.dec = tk.StringVar()
        self.ra.set(self.pos_view_model.ra)
        self.dec.set(self.pos_view_model.dec)
        
        self.RA_label= tk.Label(font=('arial', 15, 'bold'),
                                text= "RA")
        self.RA_label.grid(row=1, column =0)
        
        self.RA_display= tk.Label(font=('arial', 20, 'bold'), 
                                  bg='light green',
                                  textvariable = self.ra)
        self.RA_display.grid(row=1, column =1)
        
        self.DEC_label= tk.Label(font=('arial', 15, 'bold'),
                                 text= "DEC")
        self.DEC_label.grid(row=1, column =3)
        
        self.DEC_display= tk.Label(font=('arial', 20, 'bold'),
                                   bg='light green',
                                   textvariable = self.dec)
        self.DEC_display.grid(row=1, column =4)
        
        self.refresh_coordinates()
        
    def refresh_ra(self):
        """Refreshes ra StringVar"""
        self.ra.set(self.pos_view_model.ra)
        
    def refresh_dec(self):
        """Refreshes dec StringVar"""
        self.dec.set(self.pos_view_model.dec)
        
    def refresh_coordinates(self):
        """Refreshes coordinates and calls itself."""
        self.refresh_ra()
        self.refresh_dec()
        print('Refreshing coordinates')
        self.after(500, self.refresh_coordinates)
