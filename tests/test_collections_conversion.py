def test_convert_dict_copy(converter):
    data = {"a": 1000, "b": 2000}
    result = converter.convert(data, "m", "km")
    assert result == {"a": 1, "b": 2}
    assert result is not data

def test_convert_list_inplace(converter):
    values = [1, 2, 3]
    converter.convert(values, "m", "cm", inplace=True)
    assert values == [100, 200, 300]

def test_convert_tuple_returns_iterable(converter):
    result = converter.convert((1, 2), "m", "cm")
    assert list(result) == [100, 200]
