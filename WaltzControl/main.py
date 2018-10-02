from entities.positions import HorizontalPosition
from entities.local_sidereal_time import LocalSiderealTime
from use_cases.position_update import PositionUpdater
from use_cases.tel_controller_boundarys import TelescopeControllerResponseBoundary
from interface_adapters.tel_controller import TelescopeControllerAPI
from interface_adapters.presenter import PositionPresenter, TimePresenter
from interface_adapters.view_models import PositionViewModel, TimeViewModel
from interface_adapters.times  import LocalTime, CoordinatedUniversalTime
from external_interfaces.tel_communication import TelescopeCommunicator
from external_interfaces.pointing_main_view import WaltzPointing

import threading
import time





def create_instances():
    """Creates all necessary instances."""
    
    hor_pos = HorizontalPosition(0,30)
    LST = LocalSiderealTime()
    LT = LocalTime()
    UTC = CoordinatedUniversalTime()
    
    tel_communicator = TelescopeCommunicator()
    tel_response = TelescopeControllerResponseBoundary()
    tel_command = TelescopeControllerAPI(tel_response,tel_communicator)
    pos_view_model = PositionViewModel()
    time_view_model = TimeViewModel()
    pos_presenter = PositionPresenter(hor_pos, pos_view_model)
    time_presenter = TimePresenter(LST, LT, UTC, time_view_model)
    pos_updater = PositionUpdater(hor_pos,
                                  tel_command,
                                  tel_response,
                                  pos_presenter)
    return (hor_pos,
            LST,
            LT,
            UTC,
            pos_view_model,
            time_view_model,
            pos_updater,
            time_presenter,)

def refresh_position(Stop=False):
    """Infinite Loop to update and present position.
    """
    while not Stop:
        pos_updater.request_update_present_position()
        time.sleep(0.5)
        
def refresh_times(Stop = False):
    """Infinite Loop to update and present times.
    """
    while not Stop:
        LST.refresh()
        LT.refresh()
        UTC.refresh()
        time_presenter.present_times()
        time.sleep(0.2)





if __name__ == '__main__':
    (hor_pos,
     LST,
     LT,
     UTC,
     pos_view_model,
     time_view_model,
     pos_updater,
     time_presenter) = create_instances()
    threading.Thread(target = refresh_position).start()
    threading.Thread(target = refresh_times).start()
    WP = WaltzPointing(pos_view_model, time_view_model)
    WP.mainloop()


