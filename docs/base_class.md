# Base Converter Class Documentation

The `Converter` class in `base_class.py` provides the foundation for all unit conversions in this project. It implements a flexible conversion system that can handle both simple scaling conversions (like length) and conversions with offsets (like temperature).

## Class: `Converter`

### Overview

The `Converter` class takes a dictionary of units and their conversion factors, then provides methods to convert values between these units. It handles validation of inputs and supports both absolute conversions and delta/interval conversions.

### Constructor

```python
def __init__(self, units: Dict[str, Union[Number, Tuple[Number, Number], List[Number]]])
```

#### Parameters

- `units`: A dictionary where:
  - Keys are unit symbols (strings)
  - Values can be:
    - A single number (scale factor)
    - A tuple of two numbers (scale factor, offset)
    - A list of two numbers [scale factor, offset]

#### Behavior

The constructor normalizes all unit values to tuples of (scale_factor, offset):
- If a single number is provided, it's converted to (number, 1)
- If a list of two numbers is provided, it's converted to a tuple
- If a tuple of two numbers is already provided, it's left as is
- Any other format raises an appropriate error

### Methods

#### `convert`

```python
def convert(self, value, origin_unit, final_unit, delta=False)
```

Converts a value from one unit to another.

#### Parameters

- `value`: The numeric value to convert
- `origin_unit`: The source unit (must be a key in the units dictionary)
- `final_unit`: The target unit (must be a key in the units dictionary)
- `delta`: Boolean flag indicating whether this is a delta/interval conversion
  - When `True`, only the scale factor is used (offsets are ignored)
  - When `False` (default), both scale factor and offset are applied

#### Returns

- The converted value as a float

#### Raises

- `ValueError`: If either the origin or final unit is not in the units dictionary

### Conversion Formula

The conversion process follows these steps:

1. For regular conversions (`delta=False`):
   ```
   base_value = (value - origin_offset) / origin_scale
   final_value = base_value * final_scale + final_offset
   ```

2. For delta/interval conversions (`delta=True`):
   ```
   base_value = value / origin_scale
   final_value = base_value * final_scale
   ```

### Example Usage

```python
# Create a temperature converter
temp_converter = Converter({
    "°C": (1, 0),       # Celsius (base unit)
    "°F": (1.8, 32),    # Fahrenheit
    "K": (1, 273.15)    # Kelvin
})

# Convert 25°C to Fahrenheit
fahrenheit = temp_converter.convert(25, "°C", "°F")
print(f"25°C = {fahrenheit}°F")  # Output: 25°C = 77.0°F

# Convert a temperature difference (delta) of 10°C to Fahrenheit
# Note: a 10°C increase equals an 18°F increase (not 50°F)
fahrenheit_delta = temp_converter.convert(10, "°C", "°F", delta=True)
print(f"Delta of 10°C = Delta of {fahrenheit_delta}°F")  # Output: Delta of 10°C = Delta of 18.0°F
```

## Implementation Details

### Type Checking and Validation

The class performs extensive type checking and validation to ensure that:
1. All unit values are properly formatted
2. Conversion operations use valid units
3. Input values are numeric

### Error Handling

The class raises appropriate exceptions with descriptive error messages when:
- Unit values are not in the expected format
- Conversion is attempted with unknown units
- Input values are not numeric

### Performance Considerations

The conversion formulas are optimized for accuracy and simplicity. The class normalizes all unit definitions during initialization to ensure consistent behavior during conversions.