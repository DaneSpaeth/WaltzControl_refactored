from entities.positions import HorizontalPositionHA
from entities.local_sidereal_time import LocalSiderealTime
from use_cases.position_update import PositionUpdaterHA
from use_cases.movements import Mover
from use_cases.speeds import SpeedChanger
from use_cases.tel_controller_boundarys import TelescopeControllerResponseBoundary
from interface_adapters.tel_controller import TelescopeControllerAPI
from interface_adapters.presenter import (PositionPresenterHA,
                                          TimePresenter,
                                          SpeedPresenter)
from interface_adapters.view_models import (PositionViewModel,
                                            TimeViewModel,
                                            SpeedViewModel)
from interface_adapters.times  import LocalTime, CoordinatedUniversalTime
from interface_adapters.user_controller import UserController
from external_interfaces.tel_communication import TelescopeCommunicator
from external_interfaces.pointing_main_view import WaltzPointing

import threading
import time





def create_instances():
    """Creates all necessary instances."""
    
    hor_pos = HorizontalPositionHA(0, 30, ha = 0 )
    LST = LocalSiderealTime()
    LT = LocalTime()
    UTC = CoordinatedUniversalTime()
    
    tel_communicator = TelescopeCommunicator()
    tel_response = TelescopeControllerResponseBoundary()
    tel_command = TelescopeControllerAPI(tel_response,tel_communicator)
    pos_view_model = PositionViewModel()
    time_view_model = TimeViewModel()
    speed_view_model = SpeedViewModel()
    pos_presenter = PositionPresenterHA(hor_pos, pos_view_model)
    time_presenter = TimePresenter(LST, LT, UTC, time_view_model)
    speed_presenter = SpeedPresenter(speed_view_model)
    pos_updater = PositionUpdaterHA(hor_pos,
                                    tel_command,
                                    tel_response,
                                    pos_presenter,
                                    LST)
    mover = Mover(tel_command)
    speed_changer = SpeedChanger(tel_command, speed_presenter)
    user_control = UserController(mover, speed_changer)
    
    
    return (hor_pos,
            LST,
            LT,
            UTC,
            pos_view_model,
            time_view_model,
            speed_view_model,
            pos_updater,
            time_presenter,
            mover,
            speed_changer,
            user_control)

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
        LT.refresh()
        UTC.refresh()
        LST.refresh()
        pos_updater.request_update_present_position()
        time_presenter.present_times()
        time.sleep(0.2)

if __name__ == '__main__':
    (hor_pos,
     LST,
     LT,
     UTC,
     pos_view_model,
     time_view_model,
     speed_view_model,
     pos_updater,
     time_presenter,
     mover,
     speed_changer,
     user_control) = create_instances()
    #Create daemon thread. We choose a daemon 
    #so that it will stop automatically if mainloop is stopped
    refresh = threading.Thread(target = refresh_times)
    refresh.daemon = True
    refresh.start()
    
    WP = WaltzPointing(pos_view_model, time_view_model, speed_view_model,
                       user_control)
    WP.mainloop()