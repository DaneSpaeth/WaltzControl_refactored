from use_cases.position_update import PositionUpdater
from use_cases.tel_controller_boundarys import (TelescopeControllerInputBoundary,
                                         TelescopeControllerOutputBoundary)
from entities.positions import HorizontalPosition
from interface_adapters.tel_controller import (TelescopeControllerAPI,
	TelescopeConnectionInterface)
from external_interfaces.tel_connection import (Lx200TelConnection,
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



