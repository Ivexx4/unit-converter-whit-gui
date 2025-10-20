# Converters Documentation

The `Converters.py` module implements specific converter instances using the base `Converter` class. It provides four converter types:

1. **Temperature** - Convert between various temperature scales
2. **Length** - Convert between different units of length/distance
3. **Weight** - Convert between different units of weight/mass
4. **Volume** - Convert between different units of volume

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

## Length Converter

### Overview

The Length converter allows conversion between various units of length or distance, including metric units (meters, kilometers, etc.) and imperial units (feet, inches, miles, etc.).

### Implementation

```python
from base_class import Converter

Length = Converter({
    "m": (1, 0),      # meters (base unit)
    "km": (0.001, 0),  # kilometers (1 km = 1000 m, so scale factor is 0.001)
    "cm": (100, 0),   # centimeters (1 m = 100 cm, so scale factor is 100)
    "mm": (1000, 0),  # millimeters (1 m = 1000 mm, so scale factor is 1000)
    "in": (39.3701, 0), # inches (1 m = 39.3701 in, so scale factor is 39.3701)
    "ft": (3.28084, 0), # feet (1 m = 3.28084 ft, so scale factor is 3.28084)
    "yd": (1.09361, 0), # yards (1 m = 1.09361 yd, so scale factor is 1.09361)
    "mi": (0.000621371, 0) # miles (1 m = 0.000621371 mi, so scale factor is 0.000621371)
})
```

### Supported Length Units

| Unit | Symbol | Conversion from meters | Conversion to meters |
|------|--------|------------------------|----------------------|
| Meter | m | - | - |
| Kilometer | km | km = m / 1000 | m = km * 1000 |
| Centimeter | cm | cm = m * 100 | m = cm / 100 |
| Millimeter | mm | mm = m * 1000 | m = mm / 1000 |
| Inch | in | in = m * 39.3701 | m = in / 39.3701 |
| Foot | ft | ft = m * 3.28084 | m = ft / 3.28084 |
| Yard | yd | yd = m * 1.09361 | m = yd / 1.09361 |
| Mile | mi | mi = m * 0.000621371 | m = mi / 0.000621371 |

### Usage Examples

```python
from Converters import Length

# Basic conversions
meters_to_feet = Length.convert(1, "m", "ft")
print(f"1 m = {meters_to_feet:.2f} ft")  # Output: 1 m = 3.28 ft

miles_to_kilometers = Length.convert(1, "mi", "km")
print(f"1 mi = {miles_to_kilometers:.2f} km")  # Output: 1 mi = 1.61 km

inches_to_centimeters = Length.convert(10, "in", "cm")
print(f"10 in = {inches_to_centimeters:.2f} cm")  # Output: 10 in = 25.40 cm
```

## Weight Converter

### Overview

The Weight converter allows conversion between various units of weight or mass, including metric units (kilograms, grams, etc.) and imperial units (pounds, ounces, etc.).

### Implementation

```python
from base_class import Converter

Weight = Converter({
    "kg": (1, 0),      # kilograms (base unit)
    "g": (1000, 0),    # grams (1 kg = 1000 g, so scale factor is 1000)
    "mg": (1000000, 0), # milligrams (1 kg = 1,000,000 mg, so scale factor is 1,000,000)
    "lb": (2.20462, 0), # pounds (1 kg = 2.20462 lb, so scale factor is 2.20462)
    "oz": (35.274, 0),  # ounces (1 kg = 35.274 oz, so scale factor is 35.274)
    "st": (0.157473, 0), # stone (1 kg = 0.157473 st, so scale factor is 0.157473)
    "ton": (0.001, 0),   # metric ton (1 kg = 0.001 ton, so scale factor is 0.001)
    "uston": (0.00110231, 0) # US ton (1 kg = 0.00110231 US ton, so scale factor is 0.00110231)
})
```

### Supported Weight Units

| Unit | Symbol | Conversion from kilograms | Conversion to kilograms |
|------|--------|---------------------------|-------------------------|
| Kilogram | kg | - | - |
| Gram | g | g = kg * 1000 | kg = g / 1000 |
| Milligram | mg | mg = kg * 1,000,000 | kg = mg / 1,000,000 |
| Pound | lb | lb = kg * 2.20462 | kg = lb / 2.20462 |
| Ounce | oz | oz = kg * 35.274 | kg = oz / 35.274 |
| Stone | st | st = kg * 0.157473 | kg = st / 0.157473 |
| Metric Ton | ton | ton = kg * 0.001 | kg = ton / 0.001 |
| US Ton | uston | uston = kg * 0.00110231 | kg = uston / 0.00110231 |

### Usage Examples

```python
from Converters import Weight

# Basic conversions
kilograms_to_pounds = Weight.convert(1, "kg", "lb")
print(f"1 kg = {kilograms_to_pounds:.2f} lb")  # Output: 1 kg = 2.20 lb

pounds_to_grams = Weight.convert(1, "lb", "g")
print(f"1 lb = {pounds_to_grams:.2f} g")  # Output: 1 lb = 453.59 g

ounces_to_grams = Weight.convert(10, "oz", "g")
print(f"10 oz = {ounces_to_grams:.2f} g")  # Output: 10 oz = 283.50 g
```

## Volume Converter

### Overview

The Volume converter allows conversion between various units of volume, including metric units (liters, milliliters, etc.) and imperial/US units (gallons, quarts, etc.).

### Implementation

```python
from base_class import Converter

Volume = Converter({
    "L": (1, 0),        # liters (base unit)
    "mL": (1000, 0),    # milliliters (1 L = 1000 mL, so scale factor is 1000)
    "m³": (0.001, 0),   # cubic meters (1 L = 0.001 m³, so scale factor is 0.001)
    "gal": (0.264172, 0), # US gallons (1 L = 0.264172 gal, so scale factor is 0.264172)
    "qt": (1.05669, 0),  # US quarts (1 L = 1.05669 qt, so scale factor is 1.05669)
    "pt": (2.11338, 0),  # US pints (1 L = 2.11338 pt, so scale factor is 2.11338)
    "fl_oz": (33.814, 0), # US fluid ounces (1 L = 33.814 fl_oz, so scale factor is 33.814)
    "cup": (4.16667, 0)  # US cups (1 L = 4.16667 cups, so scale factor is 4.16667)
})
```

### Supported Volume Units

| Unit | Symbol | Conversion from liters | Conversion to liters |
|------|--------|------------------------|----------------------|
| Liter | L | - | - |
| Milliliter | mL | mL = L * 1000 | L = mL / 1000 |
| Cubic Meter | m³ | m³ = L * 0.001 | L = m³ / 0.001 |
| US Gallon | gal | gal = L * 0.264172 | L = gal / 0.264172 |
| US Quart | qt | qt = L * 1.05669 | L = qt / 1.05669 |
| US Pint | pt | pt = L * 2.11338 | L = pt / 2.11338 |
| US Fluid Ounce | fl_oz | fl_oz = L * 33.814 | L = fl_oz / 33.814 |
| US Cup | cup | cup = L * 4.16667 | L = cup / 4.16667 |

### Usage Examples

```python
from Converters import Volume

# Basic conversions
liters_to_gallons = Volume.convert(1, "L", "gal")
print(f"1 L = {liters_to_gallons:.2f} gallons")  # Output: 1 L = 0.26 gallons

gallons_to_liters = Volume.convert(1, "gal", "L")
print(f"1 gal = {gallons_to_liters:.2f} L")  # Output: 1 gal = 3.79 L

cubic_meters_to_liters = Volume.convert(1, "m³", "L")
print(f"1 m³ = {cubic_meters_to_liters:.2f} L")  # Output: 1 m³ = 1000.00 L
```

## Best Practices for Creating Converters

1. **Choose a Base Unit**: Select one unit as the base (usually the SI unit) and define it with a scale factor of 1 and an offset of 0.

2. **Use Consistent Formats**: For simple unit types (length, weight, etc.), use an offset of 0. Only use non-zero offsets for units with different zero points (like temperature).

3. **Include Unit Symbols**: Use standard symbols for units when possible.

4. **Document Conversion Factors**: Include comments explaining the conversion factors, especially for less common units.

5. **Test Conversions**: Verify your conversion factors with known values before using them in production.