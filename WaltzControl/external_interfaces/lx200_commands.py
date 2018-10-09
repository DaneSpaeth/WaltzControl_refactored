"""Translate Meade Telescope Serial Command Protocol into commands."""

def get_telescope_ra():
    """Return Lx200 protocol command for "Get Telescope Right Ascension".
    """
    command = b'#:GR#'
    return command
    
def get_telescope_dec():
    """Return Lx200 protocol command for "Get Telescope Declination".
    """
    command = b'#:GD#'
    return command

def move_telescope_west():
    """Return Lx200 protocol command for "move_telescope_west".
    """
    command = b'#:Mw#'
    return command

def move_telescope_east():
    """Return Lx200 protocol command for "move_telescope_east".
    """
    command = b'#:Me#'
    return command

def move_telescope_north():
    """Return Lx200 protocol command for "move_telescope_north".
    """
    command = b'#:Mn#'
    return command

def move_telescope_south():
    """Return Lx200 protocol command for "move_telescope_south".
    """
    command = b'#:Ms#'
    return command

def stop_telescope_west():
    """Return Lx200 protocol command for "halt westward slew".
    """
    command = b'#:Qw#'
    return command

def stop_telescope_east():
    """Return Lx200 protocol command for "halt eastward slew".
    """
    command = b'#:Qe#'
    return command

def stop_telescope_north():
    """Return Lx200 protocol command for "halt northward slew".
    """
    command = b'#:Qn#'
    return command

def stop_telescope_south():
    """Return Lx200 protocol command for "halt southward slew".
    """
    command = b'#:Qs#'
    return command

def set_telescope_speed_guide():
    """Return Lx200 protocol command for "Set Slew Rate to Guiding Rate".
    """
    command = b'#:RG#'
    return command

def set_telescope_speed_center():
    """Return Lx200 protocol command for "Set Slew Rate to Centering Rate".
    """
    command = b'#:RC#'
    return command

def set_telescope_speed_find():
    """Return Lx200 protocol command for "Set Slew Rate to Find Rate".
    """
    command = b'#:RM#'
    return command

def set_telescope_speed_slew():
    """Return Lx200 protocol command for "Set Slew Rate to Max Rate".
    """
    command = b'#:RS#'
    return command

def toggle_telescope_precision():
    """Return Lx200 command for "Toggle Precision"."""
    command = b'#:U#'
    return command

