import pytest

from interface_adapters.view_models import PositionViewModel

class TestPositionViewModel():
    """Test PositionViewModel class."""
    def setup_method(self):
        """Execute before every test. Create PositionViewModel instance."""
        self.pos_view = PositionViewModel()
    
    def test_set_ra(self):
        """ Test setting ra attribute of PositionViewModel instance."""
        self.pos_view.ra = '12h00m00s'
        assert self.pos_view.ra == '12h00m00s'
        
    def test_set_dec(self):
        """ Test setting dec attribute of PositionViewModel instance."""
        self.pos_view.dec = '''12°00'00"'''
        assert self.pos_view.dec == '''12°00'00"'''
