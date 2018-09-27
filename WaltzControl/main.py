from entities.positions import HorizontalPosition
from use_cases.position_update import PositionUpdater
from use_cases.tel_controller_boundarys import TelescopeControllerResponseBoundary
from interface_adapters.tel_controller import TelescopeControllerAPI
from interface_adapters.presenter import PositionPresenter
from interface_adapters.view_models import PositionViewModel
from external_interfaces.tel_communication import TelescopeCommunicator
from external_interfaces.pointing_main_view import WaltzPointing

import threading
import time



hor_pos = HorizontalPosition(0,30)


tel_communicator = TelescopeCommunicator()
tel_response = TelescopeControllerResponseBoundary()
tel_command = TelescopeControllerAPI(tel_response,tel_communicator)
pos_view_model = PositionViewModel()
pos_presenter = PositionPresenter(hor_pos, pos_view_model)
pos_updater = PositionUpdater(hor_pos,
                              tel_command,
                              tel_response,
                              pos_presenter)

def refresh_position(Stop=False):
    """Infinite Loop to update and present position.
    """
    while not Stop:
        pos_updater.request_update_present_position()
        print(pos_view_model.ra, pos_view_model.dec)
        time.sleep(0.5)

threading.Thread(target=refresh_position).start()

if __name__ == '__main__':
    WP = WaltzPointing(pos_view_model)
    WP.mainloop()


