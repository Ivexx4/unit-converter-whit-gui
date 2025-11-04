import pytest
base_class = pytest.importorskip("base_class")
Converter = base_class.Converter

@pytest.fixture
def converter():
    return Converter({
        "m": (1, 0),
        "km": (0.001, 0),
        "cm": (100, 0),
        "°C": (1, 0),
        "°F": (1.8, 32),
        "K": (1, 273.15)
    })
