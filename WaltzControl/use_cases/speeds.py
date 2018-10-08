"""Contains Class for setting slew speeds."""

class SpeedChanger:
    """Class for changing speeds."""
    def __init__(self, tel_controller, speed_presenter):
        """Construct instance.
           
           Input: Injection of tel_controller instance
                  Injection of SpeedPresenter instance
        """
        self.tel_controller = tel_controller
        self.speed_presenter = speed_presenter
        #We want to store current speed
        self.current_speed = ''
        #Always start with guide speed
        self.set_speed_guide()
        
        
    def set_speed_guide(self):
        """Calls telescope controller to set guiding speed."""
        self.tel_controller.set_speed_guide()
        #Save current speed. Actually it would be much nicer to set current
        #from feedback of telescope controller. But the controller does not
        #respond to speed changes so we don't have an oportunity to check.
        #So we can also set the current speed here and assume that it has worked
        self.current_speed = 'Guide'
        self.speed_presenter.present_speed(self.current_speed)
        
    def set_speed_center(self):
        """Calls telescope controller to set center speed."""
        self.tel_controller.set_speed_center()
        self.current_speed = 'Center'
        self.speed_presenter.present_speed(self.current_speed)
        
    def set_speed_find(self):
        """Calls telescope controller to set find speed."""
        self.tel_controller.set_speed_find()
        self.current_speed = 'Find'
        self.speed_presenter.present_speed(self.current_speed)
        
    def set_speed_slew(self):
        """Calls telescope controller to set slew speed."""
        self.tel_controller.set_speed_slew()
        self.current_speed = 'Slew'
        self.speed_presenter.present_speed(self.current_speed)