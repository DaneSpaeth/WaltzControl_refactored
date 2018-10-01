import external_interfaces.lx200_commands as lx

def test_get_telescope_ra():
    """Test get_telescope_ra."""
    command = lx.get_telescope_ra()
    assert command == b'#:GR#'
    
def test_get_telescope_dec():
    """Test get_telescope_dec."""
    command = lx.get_telescope_dec()
    assert command == b'#:GD#'
