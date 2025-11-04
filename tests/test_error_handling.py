import pytest

def test_invalid_unit_raises_value_error(converter):
    with pytest.raises(ValueError):
        converter.convert(1, "m", "unknown")

@pytest.mark.parametrize("bad_value", ["abc", object(), None])
def test_convert_invalid_input_raises(converter, bad_value):
    with pytest.raises(TypeError):
        converter.convert(bad_value, "m", "km")
