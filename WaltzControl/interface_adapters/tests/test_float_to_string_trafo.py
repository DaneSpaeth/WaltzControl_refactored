import pytest

from interface_adapters.float_to_string_trafo import (float_to_hms,
                                   ra_float_to_high_prec,
                                   dec_float_to_high_prec,
                                   ha_float_to_high_prec)

def test_float_to_hms():
    """Test float_to_hms."""
    assert float_to_hms(12) == (12,0,0)
    assert float_to_hms(0) == (0,0,0)
    assert float_to_hms(23.9999999999) == (24,0,0)
    with pytest.raises(TypeError):
        float_to_hms('12')

def test_ra_float_to_high_prec():
    """Test ra_float_to_high_prec."""
    assert ra_float_to_high_prec(12) == '12h00m00s'
    assert ra_float_to_high_prec(0) == '00h00m00s'
    assert ra_float_to_high_prec(23.9999999999) == '00h00m00s'
    assert ra_float_to_high_prec(1.99999999999) == '02h00m00s'
    
    with pytest.raises(TypeError):
        ra_float_to_high_prec('12')
    with pytest.raises(ValueError):
        ra_float_to_high_prec(25)
    with pytest.raises(ValueError):
        ra_float_to_high_prec(-1)
        
def test_dec_float_to_high_prec():
    """Test dec_float_to_high_prec."""
    assert dec_float_to_high_prec(12) == '''+12°00'00"'''
    assert dec_float_to_high_prec(0) == '''+00°00'00"'''
    assert dec_float_to_high_prec(89.9999999999) == '''+90°00'00"'''
    assert dec_float_to_high_prec(1.99999999999) == '''+02°00'00"'''
    assert dec_float_to_high_prec(-45) == '''-45°00'00"'''
    
    with pytest.raises(TypeError):
        dec_float_to_high_prec('12')
    with pytest.raises(ValueError):
        dec_float_to_high_prec(91)
    with pytest.raises(ValueError):
        dec_float_to_high_prec(-91)
        
def test_ha_float_to_high_prec():
    """ Test ha_float_to_high_prec."""
    assert ha_float_to_high_prec(12) == '+12h00m00s'
    assert ha_float_to_high_prec(0) == '+00h00m00s'
    assert ha_float_to_high_prec(-1) == '-01h00m00s'
    assert ha_float_to_high_prec(1.99999999) == '+02h00m00s'
    
    with pytest.raises(ValueError):
        ha_float_to_high_prec(-12)
        



    
        
