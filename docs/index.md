# Unit Converter Documentation

Welcome to the documentation for the Unit Converter project. This documentation provides comprehensive information about the project's structure, components, and usage.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [API Documentation](#api-documentation)
4. [Usage Examples](#usage-examples)
5. [Extending the Converter](#extending-the-converter)
6. [License](#license)

## Project Overview

The Unit Converter is a flexible and extensible library for converting between different units of measurement. It features a modular design with a base converter class that can be extended for any unit type, and a user-friendly graphical interface built with Tkinter.

The project supports the following conversion types:

1. **Temperature**: Convert between multiple temperature scales:
   - Celsius (ºC)
   - Fahrenheit (°F)
   - Kelvin (K)
   - Rankine (ºR)
   - Delisle (ºD)
   - Réaumur (ºRe)
   - Newton (ºN)
   - Rømer (ºRø)

2. **Length**: Convert between various units of length:
   - Meter (m)
   - Kilometer (km)
   - Centimeter (cm)
   - Millimeter (mm)
   - Inch (in)
   - Foot (ft)
   - Yard (yd)
   - Mile (mi)

3. **Weight**: Convert between various units of weight/mass:
   - Kilogram (kg)
   - Gram (g)
   - Milligram (mg)
   - Pound (lb)
   - Ounce (oz)
   - Stone (st)
   - Metric Ton (ton)
   - US Ton (uston)

4. **Volume**: Convert between various units of volume:
   - Liter (L)
   - Milliliter (mL)
   - Cubic Meter (m³)
   - US Gallon (gal)
   - US Quart (qt)
   - US Pint (pt)
   - US Fluid Ounce (fl_oz)
   - US Cup (cup)

## Installation

### Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/converter.git
   cd converter
   ```

2. No additional dependencies are required beyond Python's standard library.

## API Documentation

The project consists of two main modules:

- [Base Class](base_class.md) - Documentation for the core `Converter` class
- [Converters](converters.md) - Documentation for specific converter implementations


## Usage Examples

### Command Line Usage

#### Temperature Conversion

```python
from Converters import Temperature

# Convert from Celsius to Fahrenheit
result = Temperature.convert(25, "ºC", "°F")
print(f"25 ºC = {result:.2f} °F")  # Output: 25 ºC = 77.00 °F

# Convert from Kelvin to Celsius
result = Temperature.convert(300, "K", "ºC")
print(f"300 K = {result:.2f} ºC")  # Output: 300 K = 26.85 ºC

# Convert with delta (temperature difference)
result = Temperature.convert(10, "ºC", "°F", delta=True)
print(f"Delta of 10 ºC = Delta of {result:.2f} °F")  # Output: Delta of 10 ºC = Delta of 18.00 °F
```

#### Length Conversion

```python
from Converters import Length

# Convert from meters to feet
result = Length.convert(1, "m", "ft")
print(f"1 m = {result:.2f} ft")  # Output: 1 m = 3.28 ft

# Convert from miles to kilometers
result = Length.convert(1, "mi", "km")
print(f"1 mi = {result:.2f} km")  # Output: 1 mi = 1.61 km

# Convert from inches to centimeters
result = Length.convert(10, "in", "cm")
print(f"10 in = {result:.2f} cm")  # Output: 10 in = 25.40 cm
```

#### Weight Conversion

```python
from Converters import Weight

# Convert from kilograms to pounds
result = Weight.convert(1, "kg", "lb")
print(f"1 kg = {result:.2f} lb")  # Output: 1 kg = 2.20 lb

# Convert from pounds to grams
result = Weight.convert(1, "lb", "g")
print(f"1 lb = {result:.2f} g")  # Output: 1 lb = 453.59 g

# Convert from ounces to grams
result = Weight.convert(10, "oz", "g")
print(f"10 oz = {result:.2f} g")  # Output: 10 oz = 283.50 g
```

#### Volume Conversion

```python
from Converters import Volume

# Convert from liters to gallons
result = Volume.convert(1, "L", "gal")
print(f"1 L = {result:.2f} gal")  # Output: 1 L = 0.26 gal

# Convert from gallons to liters
result = Volume.convert(1, "gal", "L")
print(f"1 gal = {result:.2f} L")  # Output: 1 gal = 3.79 L

# Convert from cubic meters to liters
result = Volume.convert(1, "m³", "L")
print(f"1 m³ = {result:.2f} L")  # Output: 1 m³ = 1000.00 L
```

## Extending the Converter

The Unit Converter already includes converters for Temperature, Length, Weight, and Volume. However, it is designed to be easily extended with additional unit types (such as Area, Pressure, Energy, etc.). See the following documentation for details:
[Extending the Converter](converters.md#best-practices-for-creating-converters)


## License

This project is licensed under the terms specified in the [LICENSE](../LICENSE) file.