"""Translate Use_Case data into View_Model.
"""
from use_cases.user_boundarys import UserPresenterBoundary
from interface_adapters.float_to_string_trafo import (ra_float_to_high_prec,
                                                      dec_float_to_high_prec,
                                                      ha_float_to_high_prec)

class PositionPresenter(UserPresenterBoundary):
    """Present Position in View Model.
       
       Handles changes of internal data structures and translates them into 
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
        
class PositionPresenterHA(PositionPresenter):
    """Present Position (including RA, DEC, HA) in View Model.
    
       Handles changes of internal data structures and translates them into 
       simple data structures in the View_Model.
    """
    def present_position(self):
        """For,at position and send to view model.
        """
        super().present_position()
        self.pos_view_model.ha = ha_float_to_high_prec(self.position.ha)
        
class TimePresenter:
    """Present Times in View Model.
       
       Handles changes of internal data structures and translates them into 
       simple data structures in the View_Model.
    """
    def __init__(self, LST, LT, UTC, time_view_model):
        """Inject existing time instances."""
        self.LST = LST
        self.LT = LT
        self.UTC = UTC
        self.time_view_model = time_view_model
        
    def present_times(self):
        """Send formated times to view model."""
        self.time_view_model.LST = self.LST.as_string
        self.time_view_model.LT = self.LT.as_string
        self.time_view_model.UTC = self.UTC.as_string
