from UC_position_update import PositionUpdater
from UC_tel_controller_boundarys import (TelescopeControllerInputBoundary,
                                         TelescopeControllerOutputBoundary)
from ENT_positions import HorizontalPosition
from API_tel_controller import (TelescopeControllerAPI,
                                TelescopeConnectionInterface)
from DEV_tel_connection import (Lx200TelConnection,
                                SerialConnection)

hor_pos = HorizontalPosition(0,30)
print(hor_pos.ra, hor_pos.dec)

ser_con = SerialConnection()
tel_connection = Lx200TelConnection(ser_con)
tel_response = TelescopeControllerInputBoundary()
tel_command = TelescopeControllerAPI(tel_response,tel_connection)
pos_updater = PositionUpdater(hor_pos, tel_command, tel_response)
pos_updater.request_and_update_position()

print(hor_pos.ra, hor_pos.dec)



