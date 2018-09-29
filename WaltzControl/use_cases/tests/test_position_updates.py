from entities.positions import HorizontalPosition
from use_cases.position_update import PositionUpdater
from use_cases.tel_controller_boundarys import TelescopeControllerResponseBoundary
from interface_adapters.tel_controller import TelescopeControllerAPI
from interface_adapters.presenter import PositionPresenter
from interface_adapters.view_models import PositionViewModel
from external_interfaces.tel_communication import TelescopeCommunicator
from external_interfaces.pointing_main_view import WaltzPointing

class TestPositionUpdater:
    """Test Class for PositionUpdater."""
    def setup_method(self):
        """Execute before every test. Create instances."""
        self.hor_pos = HorizontalPosition(0,30)
        self.tel_communicator = TelescopeCommunicator()
        self.tel_response = TelescopeControllerResponseBoundary()
        self.tel_command = TelescopeControllerAPI(
            self.tel_response,
            self.tel_communicator)
        self.pos_view_model = PositionViewModel()
        self.pos_presenter = PositionPresenter(
            self.hor_pos, 
            self.pos_view_model)
        self.pos_updater = PositionUpdater(
            self.hor_pos,
            self.tel_command,
            self.tel_response,
            self.pos_presenter)

    def test_init(self):
        """Test PositionUpdater's __init__ method."""
        pos_updater2 = PositionUpdater(
            self.hor_pos,
            self.tel_command,
            self.tel_response,
            self.pos_presenter)

        assert pos_updater2.hor_position == self.hor_pos
        assert pos_updater2.tel_controller_output == self.tel_command
        assert pos_updater2.tel_controller_input == self.tel_response 
        assert pos_updater2.position_presenter == self.pos_presenter

    def test_update_position(self):
        """Test PositionUpater's update_position method."""
        self.pos_updater.update_position(20, 50)
        assert self.hor_pos.ra == 20
        assert self.hor_pos.dec == 50

    def test_call_presenter(self):
        """Test call_presenter method."""
        self.pos_updater.call_presenter()
        assert self.pos_view_model.ra == "00h00m00s"
        assert self.pos_view_model.dec == '''+30°00'00"'''

    def test_request_update_present_position(self):
        """Test request_update_present_position.

        Not complete right now. Maybe we should mock input/output."""
        self.pos_updater.request_update_present_position()
        assert self.hor_pos.ra == 15.25
        assert self.hor_pos.dec == 25.0


        assert self.pos_view_model.ra == "15h15m00s"
        assert self.pos_view_model.dec == '''+25°00'00"'''

