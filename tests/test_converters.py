# python
# File: tests/test_converters.py
import pytest

Converters = pytest.importorskip("Converters")
Temperature = Converters.Temperature
Length = Converters.Length
Weight = Converters.Weight
Volume = Converters.Volume

def test_temperature_celsius_to_fahrenheit():
    assert Temperature.convert(25, "ºC", "°F") == pytest.approx(77.0, rel=1e-6)

def test_temperature_kelvin_to_celsius():
    assert Temperature.convert(300, "K", "ºC") == pytest.approx(26.85, rel=1e-6)

def test_temperature_delisle_to_reaumur():
    # example: 50 ºD -> ? ºRe (uses factors from docs)
    res = Temperature.convert(50, "ºD", "ºRe")
    assert isinstance(res, float)

def test_temperature_delta_conversion():
    # 10 ºC delta -> 18 °F delta
    assert Temperature.convert(10, "ºC", "°F", delta=True) == pytest.approx(18.0, rel=1e-9)

def test_length_meter_to_feet_and_mile_to_km():
    assert Length.convert(1, "m", "ft") == pytest.approx(3.28084, rel=1e-6)
    assert Length.convert(1, "mi", "km") == pytest.approx(1.60934, rel=1e-5)

def test_weight_kg_to_lb_and_lb_to_g():
    assert Weight.convert(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-6)
    assert Weight.convert(1, "lb", "g") == pytest.approx(453.59237, rel=1e-5)

def test_volume_liter_to_gallon_and_cubic_meter_to_liter():
    assert Volume.convert(1, "L", "gal") == pytest.approx(0.264172, rel=1e-6)
    assert Volume.convert(1, "m³", "L") == pytest.approx(1000.0, rel=1e-9)

def test_identity_conversion():
    assert Temperature.convert(10, "ºC", "ºC") == pytest.approx(10)
    assert Length.convert(5, "m", "m") == pytest.approx(5)
    assert Weight.convert(2, "kg", "kg") == pytest.approx(2)
    assert Volume.convert(3, "L", "L") == pytest.approx(3)

def test_invalid_unit_raises_value_error():
    with pytest.raises(ValueError):
        Temperature.convert(1, "invalid_unit", "ºC")

