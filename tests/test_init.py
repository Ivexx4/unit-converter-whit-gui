import pytest
from base_class import Converter

def test_init_normalizes_various_formats():
    units = {"num": 2, "lst": [3, 4], "tpl": (5, 6)}
    conv = Converter(units)
    assert conv.units["num"] == (2, 1)
    assert conv.units["lst"] == (3, 4)
    assert conv.units["tpl"] == (5, 6)

@pytest.mark.parametrize("bad_value", [
    {"bad_list": [1, 2, 3]},
    {"bad_tuple": (1, 2, 3)},
])
def test_init_invalid_length_raises_value_error(bad_value):
    with pytest.raises(ValueError):
        Converter(bad_value)

def test_init_invalid_type_raises_type_error():
    with pytest.raises(TypeError):
        Converter({"bad_type": "invalid"})
