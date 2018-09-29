import pytest

from interface_adapters.string_to_float_trafo import high_prec_to_float

def test_high_prec_to_float():
    """Test high_prec_to_float."""
    assert high_prec_to_float('12h30m00s') == 12.5
    assert high_prec_to_float('''+12°30'00"''') == 12.5
    assert high_prec_to_float('''-45°30'00"''') == -45.5
    assert high_prec_to_float('''-00°30'00"''') == -0.5
    assert high_prec_to_float('12:30:00') == 12.5
    assert high_prec_to_float('''+12:30:00"''') == 12.5
    assert high_prec_to_float('''-45:30:00"''') == -45.5
    assert high_prec_to_float('''-00:30:00"''') == -0.5
    
    with pytest.raises(ValueError):
        high_prec_to_float(''''#+12°30'00"''')
    with pytest.raises(ValueError):
        high_prec_to_float("""+12°30'""")
    with pytest.raises(ValueError):
        high_prec_to_float('abcdefgh')
    with pytest.raises(ValueError):
        high_prec_to_float('1h123m45s')
        
    