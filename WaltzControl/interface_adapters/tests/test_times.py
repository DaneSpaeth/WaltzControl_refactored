from unittest.mock import patch
from interface_adapters.times import (LocalTime, CoordinatedUniversalTime)

class TestLocalTime:
    """Test Class for Local Time."""
    def setup_method(self):
        """Create LocalTime instance."""
        self.LT = LocalTime()
        
    def test_init(self):
        """Test __init__."""
        LT2 = LocalTime(LT_string = '12:00:00')
        assert LT2.as_string == '12:00:00'
        
    def test_refresh(self):
        """Test refresh."""
        fake_local_time = '04:43:00'
        with patch('time.strftime') as strf:
            strf.return_value = fake_local_time
            self.LT.refresh()
        assert self.LT.as_string == '04:43:00'
        
class TestCoordinatedUniversalTime:
    """Test Class for Local Time."""
    def setup_method(self):
        """Create CoordinatedUniversalTime instance."""
        self.UTC = CoordinatedUniversalTime()
        
    def test_init(self):
        """Test __init__."""
        UTC2 = CoordinatedUniversalTime(UTC_string = '12:00:00')
        assert UTC2.as_string == '12:00:00'
        
    def test_refresh(self):
        """Test refresh."""
        fake_uni_time = '04:43:00'
        with patch('datetime.datetime') as dt:
            dt.utcnow().strftime.return_value = fake_uni_time
            self.UTC.refresh()
        assert self.UTC.as_string == '04:43:00'