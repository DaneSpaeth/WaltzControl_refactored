from external_interfaces.tel_communication import TelescopeCommunicator  


class TestTelescopeCommunicator:
    """Test Class for Telescope Communicator."""
    def setup_method(self):
        """Initiliaze TelescopeCommunicator. Run before every test."""
        self.tel_communicator = TelescopeCommunicator()
        
    def test_get_ra(self):
        """ Test get_ra."""
        ra = self.tel_communicator.get_ra()
        assert ra == "15:15:00#"
        
    def test_get_dec(self):
        """Test get_dec"""
        dec = self.tel_communicator.get_dec()
        assert dec == "+25*00'00#"