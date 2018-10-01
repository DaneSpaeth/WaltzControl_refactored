from unittest.mock import patch
from entities.local_sidereal_time import LocalSiderealTime

class TestLocalSiderealTime:
    """Test Class fot LocalSiderealTime."""
    def setup_method(self):
        """Initialize LocalSiderealTime instance."""
        self.LST = LocalSiderealTime()
        
    def test_init(self):
        """Test __init__."""
        LST2 = LocalSiderealTime(LST_string = '12:00:00', LST_float = 12.0)
        assert LST2.as_string == '12:00:00'
        assert LST2.as_float == 12.0
        
    def test__retrieve(self):
        """Test _retrieve.
           Not complete yet"""
        pass
    
    def test__format(self):
        LST_test = '03h00m00.000s'
        as_string, as_float = self.LST._format(LST_test)
        assert as_string == '03:00:00'
        assert as_float == 3.0
        
        LST_test = '03h00m59.999s'
        as_string, as_float = self.LST._format(LST_test)
        assert as_string == '03:01:00'
        
        LST_test = '03h59m59.999s'
        as_string, as_float = self.LST._format(LST_test)
        assert as_string == '04:00:00'
        
        LST_test = '23h59m59.999s'
        as_string, as_float = self.LST._format(LST_test)
        assert as_string == '00:00:00'
        
        LST_test = '03h30m00.0s'
        as_string, as_float = self.LST._format(LST_test)
        assert as_float == 3.5
        
    def test_refresh(self):
        """Test refresh."""
        fake_LST_now = '03h00m00.000s'
        with patch('entities.local_sidereal_time.LocalSiderealTime._retrieve') \
            as retr:
            retr.return_value = fake_LST_now
            self.LST.refresh()
        assert self.LST.as_string == '03:00:00'
        assert self.LST.as_float == 3.0
        
        
        
        
        