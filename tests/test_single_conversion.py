import pytest

def test_convert_temperature_absolute_and_delta(converter):
    assert converter.convert(25, "°C", "°F") == pytest.approx(77.0, rel=1e-9)
    assert converter.convert(300, "K", "°C") == pytest.approx(26.85, rel=1e-3)
    assert converter.convert(10, "°C", "°F", delta=True) == pytest.approx(18.0, rel=1e-9)

def test_convert_length_scaling(converter):
    assert converter.convert(1, "m", "cm") == pytest.approx(100.0, rel=1e-6)
    assert converter.convert(1, "km", "m") == pytest.approx(1000.0, rel=1e-6)

def test_convert_same_unit_returns_same_value(converter):
    assert converter.convert(123, "m", "m") == 123
