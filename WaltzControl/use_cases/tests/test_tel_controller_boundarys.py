from use_cases.tel_controller_boundarys import(
    TelescopeControllerResponseBoundary
    )

class TestTelescopeControllerResponseBoundary():
    """Class to test TelescopeControllerResponseBoundary."""

    def setup_method(self):
        """Execute before every test. 
           Create TelescopeControllerResponseBoundary instance."""

        self.tel_response = TelescopeControllerResponseBoundary()

    def test_init(self):
        """Test __init__."""
        tel_response2 = TelescopeControllerResponseBoundary()
        assert tel_response2.ra_response == None
        assert tel_response2.dec_response == None
        assert tel_response2.validate_response == None

        tel_response2 = TelescopeControllerResponseBoundary(
            10.5,
            30.5,
            True)
        assert tel_response2.ra_response == 10.5
        assert tel_response2.dec_response == 30.5
        assert tel_response2.validate_response == True

    def test_set_ra_response(self):
        """Test set_ra_response."""
        self.tel_response.set_ra_response(12.5)

        assert self.tel_response.ra_response == 12.5

    def test_set_dec_response(self):
        """Test set_dec_response."""
        self.tel_response.set_dec_response(30.5)

        assert self.tel_response.dec_response == 30.5

    def test_set_validate_reponse(self):
        """Test set_validate_response."""
        self.tel_response.set_validate_response(True)

        assert self.tel_response.validate_response == True

    def test_reset_response(self):
        """Test reset_responses."""
        self.tel_response.set_ra_response(12.5)
        self.tel_response.set_dec_response(30.5)
        self.tel_response.set_validate_response(True)
        self.tel_response.reset_responses()

        assert self.tel_response.ra_response == None
        assert self.tel_response.dec_response == None
        assert self.tel_response.validate_response == None

    def test_retrive_position(self):
        """Test retrieve_position."""
        self.tel_response.set_ra_response(12.5)
        self.tel_response.set_dec_response(30.5)

        ra, dec = self.tel_response.retrieve_position()

        assert ra == 12.5
        assert dec == 30.5


