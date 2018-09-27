import tkinter as tk

from external_interfaces.position_view import PositionView 

class WaltzPointing(tk.Tk):
    """Main Window."""
    def __init__(self, pos_view_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("WaltzControl")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        
        self.position_view = PositionView(pos_view_model, self)
        self.position_view.grid(row=0,columnspan=3)

if __name__ == '__main__':
    WP = WaltzPointing()
    WP.mainloop()