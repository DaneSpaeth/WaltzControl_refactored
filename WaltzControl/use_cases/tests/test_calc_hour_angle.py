from use_cases.calc_hour_angle import calculate_hour_angle

def test_calculate_hour_angle():
    """Test calc_hour_angle."""
    assert calculate_hour_angle(0, 0) == 0
    assert calculate_hour_angle(3, 5) == 2
    assert calculate_hour_angle(0, 12) == 12
    assert calculate_hour_angle(0, 13) == -11
    assert calculate_hour_angle(0, 24) == 0
    assert calculate_hour_angle(0, 23) == -1
