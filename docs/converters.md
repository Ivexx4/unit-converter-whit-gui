# Converters Documentation

The `Converters.py` module implements specific converter instances using the base `Converter` class. Currently, it provides a Temperature converter with support for multiple temperature scales.

## Temperature Converter

### Overview

The Temperature converter allows conversion between various temperature scales, including common ones like Celsius, Fahrenheit, and Kelvin, as well as less common scales like Delisle, Réaumur, Newton, and Rømer.

### Implementation

```python
Temperature = Converter(
    {"°F":(1.8,32),"ºC":(1,0),"K":(1,273.15),"ºR":(1.8,491.67),"ºD":(-1.5,150),"ºRe":(0.8,0),"ºN":(0.33,0),"ºRø":(21/40,7.5)}
)
```

### Supported Temperature Scales

| Scale | Symbol | Formula (from Celsius) | Formula (to Celsius) |
|-------|--------|------------------------|----------------------|
| Celsius | ºC | - | - |
| Fahrenheit | °F | °F = (ºC × 1.8) + 32 | ºC = (°F - 32) / 1.8 |
| Kelvin | K | K = ºC + 273.15 | ºC = K - 273.15 |
| Rankine | ºR | ºR = (ºC × 1.8) + 491.67 | ºC = (ºR - 491.67) / 1.8 |
| Delisle | ºD | ºD = (100 - ºC) × 1.5 | ºC = 100 - (ºD / 1.5) |
| Réaumur | ºRe | ºRe = ºC × 0.8 | ºC = ºRe / 0.8 |
| Newton | ºN | ºN = ºC × 0.33 | ºC = ºN / 0.33 |
| Rømer | ºRø | ºRø = (ºC × 21/40) + 7.5 | ºC = (ºRø - 7.5) × 40/21 |

### Usage Examples

```python
from Converters import Temperature

# Basic conversions
celsius_to_fahrenheit = Temperature.convert(25, "ºC", "°F")
print(f"25 ºC = {celsius_to_fahrenheit:.2f} °F")  # Output: 25 ºC = 77.00 °F

kelvin_to_celsius = Temperature.convert(300, "K", "ºC")
print(f"300 K = {kelvin_to_celsius:.2f} ºC")  # Output: 300 K = 26.85 ºC

# Converting between less common scales
delisle_to_reaumur = Temperature.convert(50, "ºD", "ºRe")
print(f"50 ºD = {delisle_to_reaumur:.2f} ºRe")

# Delta conversions (temperature differences)
# A 10°C increase equals an 18°F increase
celsius_delta_to_fahrenheit = Temperature.convert(10, "ºC", "°F", delta=True)
print(f"Delta of 10 ºC = Delta of {celsius_delta_to_fahrenheit:.2f} °F")
```

## Creating Additional Converters

You can easily extend the module by adding new converter instances for different unit types. Here are examples of how to implement additional converters:

### Length Converter Example

```python
from base_class import Converter

Length = Converter({
    "m": (1, 0),      # meters (base unit)
    "km": (1000, 0),  # kilometers
    "cm": (0.01, 0),  # centimeters
    "mm": (0.001, 0), # millimeters
    "in": (0.0254, 0), # inches
    "ft": (0.3048, 0), # feet
    "yd": (0.9144, 0), # yards
    "mi": (1609.34, 0) # miles
})
```

### Weight Converter Example

```python
from base_class import Converter

Weight = Converter({
    "kg": (1, 0),      # kilograms (base unit)
    "g": (0.001, 0),   # grams
    "mg": (0.000001, 0), # milligrams
    "lb": (0.453592, 0), # pounds
    "oz": (0.0283495, 0), # ounces
    "st": (6.35029, 0),  # stone
    "ton": (1000, 0),    # metric ton
    "uston": (907.185, 0) # US ton
})
```

### Volume Converter Example

```python
from base_class import Converter

Volume = Converter({
    "L": (1, 0),        # liters (base unit)
    "mL": (0.001, 0),   # milliliters
    "m³": (1000, 0),    # cubic meters
    "gal": (3.78541, 0), # US gallons
    "qt": (0.946353, 0), # US quarts
    "pt": (0.473176, 0), # US pints
    "fl_oz": (0.0295735, 0), # US fluid ounces
    "cup": (0.24, 0)    # US cups
})
```

## Best Practices for Creating Converters

1. **Choose a Base Unit**: Select one unit as the base (usually the SI unit) and define it with a scale factor of 1 and an offset of 0.

2. **Use Consistent Formats**: For simple unit types (length, weight, etc.), use an offset of 0. Only use non-zero offsets for units with different zero points (like temperature).

3. **Include Unit Symbols**: Use standard symbols for units when possible.

4. **Document Conversion Factors**: Include comments explaining the conversion factors, especially for less common units.

5. **Test Conversions**: Verify your conversion factors with known values before using them in production.