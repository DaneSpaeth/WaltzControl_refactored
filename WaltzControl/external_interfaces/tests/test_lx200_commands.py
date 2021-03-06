import external_interfaces.lx200_commands as lx

def test_get_telescope_ra():
    """Test get_telescope_ra."""
    command = lx.get_telescope_ra()
    assert command == b'#:GR#'
    
def test_get_telescope_dec():
    """Test get_telescope_dec."""
    command = lx.get_telescope_dec()
    assert command == b'#:GD#'
    
def test_move_telescope_west():
    """Test test_move_telescope_west."""
    command = lx.move_telescope_west()
    assert command == b'#:Mw#'
    
def test_move_telescope_east():
    """Test move_telescope_east."""
    command = lx.move_telescope_east()
    assert command == b'#:Me#'
    
def test_move_telescope_north():
    """Test move_telescope_north."""
    command = lx.move_telescope_north()
    assert command == b'#:Mn#'
    
def test_move_telescope_south():
    """Test move_telescope_south."""
    command = lx.move_telescope_south()
    assert command == b'#:Ms#'
    
def test_stop_telescope_west():
    """Test stop_telescope_west."""
    command = lx.stop_telescope_west()
    assert command == b'#:Qw#'
    
def test_stop_telescope_east():
    """Test stop_telescope_east."""
    command = lx.stop_telescope_east()
    assert command == b'#:Qe#'
    
def test_stop_telescope_north():
    """Test stop_telescope_north."""
    command = lx.stop_telescope_north()
    assert command == b'#:Qn#'
    
def test_stop_telescope_south():
    """Test stop_telescope_south."""
    command = lx.stop_telescope_south()
    assert command == b'#:Qs#'
    
def test_set_telecope_speed_guide():
    """Test set_telecope_speed_guide."""
    command = lx.set_telescope_speed_guide()
    assert command == b'#:RG#'
    
def test_set_telecope_speed_center():
    """Test set_telecope_speed_center."""
    command = lx.set_telescope_speed_center()
    assert command == b'#:RC#'
    
def test_set_telecope_speed_find():
    """Test set_telecope_speed_find."""
    command = lx.set_telescope_speed_find()
    assert command == b'#:RM#'
    
def test_set_telecope_speed_slew():
    """Test set_telecope_speed_slew."""
    command = lx.set_telescope_speed_slew()
    assert command == b'#:RS#'
    

    

