"""Translate Use_Case data into View_Model.
"""
from use_cases.user_boundarys import UserPresenterBoundary
from interface_adapters.float_to_string_trafo import (ra_float_to_high_prec,
                                                      dec_float_to_high_prec)

class PositionPresenter(UserPresenterBoundary):
    """Handles changes of internal data structures and translates them into 
       simple data structures in the View_Model.
    """
    def __init__(self, position, pos_view_model):
        self.position = position
        self.pos_view_model = pos_view_model
        
    def present_position(self):
        """Format position and send to view model.
        """
        self.pos_view_model.ra = ra_float_to_high_prec(self.position.ra)
        self.pos_view_model.dec = dec_float_to_high_prec(self.position.dec)