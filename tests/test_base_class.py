# python
# -*- coding: utf-8 -*-
import pytest

base_class = pytest.importorskip("base_class")
Converter = base_class.Converter

def test_init_normalizes_various_formats():
    units = {"num": 2, "lst": [3, 4], "tpl": (5, 6)}
    conv = Converter(units)
    assert conv.units["num"] == (2, 1)
    assert conv.units["lst"] == (3, 4)
    assert conv.units["tpl"] == (5, 6)

def test_init_invalid_list_raises_value_error():
    with pytest.raises(ValueError):
        Converter({"bad_list": [1, 2, 3]})

def test_init_invalid_tuple_raises_value_error():
    with pytest.raises(ValueError):
        Converter({"bad_tuple": (1, 2, 3)})

def test_init_invalid_type_raises_type_error():
    with pytest.raises(TypeError):
        Converter({"bad_type": "not_a_number_or_sequence"})

def test_convert_temperature_absolute_and_delta():
    temp = Converter({
        "°C": (1, 0),
        "°F": (1.8, 32),
        "K": (1, 273.15)
    })
    # absolute conversions
    assert temp.convert(25, "°C", "°F") == pytest.approx(77.0, rel=1e-9)
    assert temp.convert(300, "K", "°C") == pytest.approx(26.85, rel=1e-3)
    # delta (interval) conversion: 10°C delta -> 18°F delta
    assert temp.convert(10, "°C", "°F", delta=True) == pytest.approx(18.0, rel=1e-9)

def test_convert_length_scaling():
    length = Converter({
        "m": (1, 0),            # base
        "ft": (3.28084, 0),     # 1 m = 3.28084 ft
        "mi": (0.000621371, 0)  # 1 m = 0.000621371 mi
    })
    assert length.convert(1, "m", "ft") == pytest.approx(3.28084, rel=1e-6)
    # 1 mile -> meters (should be ~1609.344 m)
    assert length.convert(1, "mi", "m") == pytest.approx(1609.344, rel=1e-6)

def test_invalid_unit_raises_value_error():
    conv = Converter({"m": (1, 0)})
    with pytest.raises(ValueError):
        conv.convert(1, "m", "unknown")
