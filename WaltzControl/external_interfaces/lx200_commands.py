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
