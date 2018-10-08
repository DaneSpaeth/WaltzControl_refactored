"""View for interchanging North/South and East/West.

   Only interaction on View level. Does not need view_model.
   Maybe this is a bad idea and should be changed 
   but I think it should be clearer like this."""
import tkinter as tk

class InterchangeView(tk.Frame):
    """Class for Interchange Frame."""
    def __init__(self, control_view, parent, *args, **kwargs):
        """Construct instance.
           
           Input: Parent window.
        """
        super().__init__(parent, *args, **kwargs)
        
        self.west_button = control_view.west_button
        self.east_button = control_view.east_button
        self.north_button = control_view.north_button
        self.south_button = control_view.south_button
        
        self.inter_WE=tk.IntVar()
        self.inter_NS=tk.IntVar()
        
        self.inter_NS_checkbox=tk.Checkbutton(self,
                                           text='N <> S',
                                           font=('arial', 10, 'bold'),
                                           variable=self.inter_NS,
                                           command=self.interchange_north_south)
        self.inter_NS_checkbox.grid(row=0,column=0,sticky='w',pady=5)
        
        
        self.inter_WE_checkbox=tk.Checkbutton(self,
                                           text='W <> E',
                                           font=('arial', 10, 'bold'), 
                                           variable=self.inter_WE,
                                           command=self.interchange_west_east)
        self.inter_WE_checkbox.grid(row=1,column=0,sticky='w',pady=5)
        
    def interchange_west_east(self):
        """Interchanges West and East Buttons.
        """
        #self.inter_WE.get() will return 1 if box is checked and 0 if not
        if self.inter_WE.get():
            #Grid Positions if checkbutton is checked
            self.west_button.grid(row=1,column=2)
            self.east_button.grid(row=1,column=0)  
        if not self.inter_WE.get():
            #Grid Position in default state
            self.west_button.grid(row=1,column=0)
            self.east_button.grid(row=1,column=2)
            
    def interchange_north_south(self):
        """Interchanges North and South Buttons.
        """
        #self.inter_WE.get() will return 1 if box is checked and 0 if not
        if self.inter_NS.get():
            #Grid Positions if checkbutton is checked
            self.south_button.grid(row=2,column=1)
            self.north_button.grid(row=0,column=1)  
        if not self.inter_NS.get():
            #Grid Position in default state
            self.south_button.grid(row=0,column=1)
            self.north_button.grid(row=2,column=1)
