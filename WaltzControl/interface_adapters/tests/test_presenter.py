import pytest

from interface_adapters.presenter import PositionPresenter
from entities.positions import  HorizontalPosition
from interface_adapters.view_models import PositionViewModel



class TestPositionPresenter():
    """Test PositionPresenter class."""
    def setup_method(self):
        """Execute before every test. Create PositionPresenter instance."""
        self.hor_pos = HorizontalPosition(0.0, 50.0)
        self.pos_view_model = PositionViewModel()
        self.pos_pres = PositionPresenter(self.hor_pos,self.pos_view_model)
        
        self.hor_pos.ra = 12.5
        self.hor_pos.dec = 45
        
    def test_present_position(self):
        """Test present position method."""
        self.pos_pres.present_position()
        assert self.pos_view_model.ra == '12h30m00s'
        assert self.pos_view_model.dec == '''+45°00'00"'''
