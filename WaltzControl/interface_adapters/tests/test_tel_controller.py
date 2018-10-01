from use_cases.tel_controller_boundarys import (
    TelescopeControllerResponseBoundary)
from interface_adapters.tel_controller import TelescopeControllerAPI


class MockTelCommunicator:
    """Mock class for Telescope Connection."""
    def get_ra(self):
        """Mocked method."""
        return "15:30:00#"
    def get_dec(self):
        """Mocked method."""
        return "+25*00'00#"
    
class TestTelescopeControllerAPI:
    """Test Class for TelescopeControllerAPI."""
    
    def setup_method(self):
        """Execute before every test  function."""
        self.tel_communiator = MockTelCommunicator()
        self.tel_response = TelescopeControllerResponseBoundary()
        self.tel_controller = TelescopeControllerAPI(self.tel_response,
                                                     self.tel_communiator)
    
    def test_send_ra_response(self):
        """Test send_ra_response."""
        ra = 15.5
        self.tel_controller.send_ra_response(ra)
        assert self.tel_response.ra_response == 15.5
        
    def test_send_dec_response(self):
        """Test send_dec_response."""
        dec = 25.0 
        self.tel_controller.send_dec_response(dec)
        assert self.tel_response.dec_response == 25.0
        
    def test_request_position(self):
        """Test request_position."""
        self.tel_controller.request_position()
        
        assert self.tel_response.ra_response == 15.5
        assert self.tel_response.dec_response == 25.0
        

    

