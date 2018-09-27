"""Boundarys for Input and Output from the User.
   Data entry and exit point into use_cases layer.
"""
class UserPresenterBoundary():
    """Interface to Presenter."""
    def __init__(self, position):
        self.position = position
    def present_position(self):
        pass
    
        
     