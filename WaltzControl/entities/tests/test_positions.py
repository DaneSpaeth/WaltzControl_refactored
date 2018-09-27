from entities.positions import  HorizontalPosition

class TestHorizontalPosition():
    """Test Class for HorizontalPosition."""
    def setup_method(self):
        """Execute before every test. Create HorizontalPosition instance."""
        self.hor_pos = HorizontalPosition(0.0, 50.0)
        
    def test_init(self):
        """Test __init__."""
        self.hor_pos2 = HorizontalPosition(5.0, 10.0)
        
        assert self.hor_pos2.ra == 5.0
        assert self.hor_pos2.dec == 10.0
        
    def test_change_ra(self):
        """Test change_ra."""
        self.hor_pos.change_ra(12.0)
        
        assert self.hor_pos.ra == 12.0
        
    def test_change_dec(self):
        """Test change_dec."""
        self.hor_pos.change_dec(-30.0)
        
        assert self.hor_pos.dec == -30.0
        
    def test_change_position(self):
        """Test change_position."""
        self.hor_pos.change_position(20.0,70.0)
        
        assert self.hor_pos.ra == 20.0
        assert self.hor_pos.dec == 70.0
        
    