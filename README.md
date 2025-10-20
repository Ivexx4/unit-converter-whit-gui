# Unit Converter

A flexible and extensible unit conversion library with a graphical user interface. This project provides a framework for converting between different units of measurement, with support for temperature, length, weight, and volume conversions.

## Features

- **Modular Design**: Base converter class that can be extended for any unit type
- **Temperature Conversion**: Convert between multiple temperature scales:
  - Celsius (ºC)
  - Fahrenheit (°F)
  - Kelvin (K)
  - Rankine (ºR)
  - Delisle (ºD)
  - Réaumur (ºRe)
  - Newton (ºN)
  - Rømer (ºRø)
- **Length Conversion**: Convert between various units of length:
  - Meter (m)
  - Kilometer (km)
  - Centimeter (cm)
  - Millimeter (mm)
  - Inch (in)
  - Foot (ft)
  - Yard (yd)
  - Mile (mi)
- **Weight Conversion**: Convert between various units of weight/mass:
  - Kilogram (kg)
  - Gram (g)
  - Milligram (mg)
  - Pound (lb)
  - Ounce (oz)
  - Stone (st)
  - Metric Ton (ton)
  - US Ton (uston)
- **Volume Conversion**: Convert between various units of volume:
  - Liter (L)
  - Milliliter (mL)
  - Cubic Meter (m³)
  - US Gallon (gal)
  - US Quart (qt)
  - US Pint (pt)
  - US Fluid Ounce (fl_oz)
  - US Cup (cup)
- **User-friendly GUI**: Tkinter-based interface with:
  - Input validation
  - Unit swapping
  - Support for both absolute values and intervals (delta)
  - Error handling
- **Extensible**: Easy to add new unit converters

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

## Usage

### Command Line

You can use the converters directly in your Python code:

```python
# Temperature conversions
from Converters import Temperature

# Convert from Celsius to Fahrenheit
result = Temperature.convert(25, "ºC", "°F")
print(f"25 ºC = {result:.2f} °F")  # Output: 25 ºC = 77.00 °F

# Convert from Kelvin to Celsius
result = Temperature.convert(300, "K", "ºC")
print(f"300 K = {result:.2f} ºC")  # Output: 300 K = 26.85 ºC

# Length conversions
from Converters import Length

# Convert from meters to feet
result = Length.convert(1, "m", "ft")
print(f"1 m = {result:.2f} ft")  # Output: 1 m = 3.28 ft

# Convert from miles to kilometers
result = Length.convert(1, "mi", "km")
print(f"1 mi = {result:.2f} km")  # Output: 1 mi = 1.61 km

# Weight conversions
from Converters import Weight

# Convert from kilograms to pounds
result = Weight.convert(1, "kg", "lb")
print(f"1 kg = {result:.2f} lb")  # Output: 1 kg = 2.20 lb

# Convert from pounds to grams
result = Weight.convert(1, "lb", "g")
print(f"1 lb = {result:.2f} g")  # Output: 1 lb = 453.59 g

# Volume conversions
from Converters import Volume

# Convert from liters to gallons
result = Volume.convert(1, "L", "gal")
print(f"1 L = {result:.2f} gal")  # Output: 1 L = 0.26 gal

# Convert from cubic meters to liters
result = Volume.convert(1, "m³", "L")
print(f"1 m³ = {result:.2f} L")  # Output: 1 m³ = 1000.00 L
```

### Graphical User Interface

To launch the GUI application:

```python
python gui.py
```

This will open a tabbed interface with multiple converters (Temperature, Length, Weight). The GUI allows you to:
1. Enter a value to convert
2. Select the source unit
3. Select the target unit
4. View the converted result
5. Toggle between absolute and interval (delta) conversions
6. Swap units with a single button click

## Extending the Converter

The project already includes converters for Temperature, Length, Weight, and Volume. You can easily add more converters for other unit types.

### Adding New Unit Types

To add a new unit type (e.g., Area), create a new converter in `Converters.py`:

```python
from base_class import Converter

# Define an Area converter
Area = Converter({
    "m²": (1, 0),        # square meters (base unit)
    "km²": (0.000001, 0), # square kilometers (1 km² = 1,000,000 m²)
    "cm²": (10000, 0),    # square centimeters (1 m² = 10,000 cm²)
    "mm²": (1000000, 0),  # square millimeters (1 m² = 1,000,000 mm²)
    "ha": (0.0001, 0),    # hectares (1 ha = 10,000 m²)
    "acre": (0.000247105, 0), # acres (1 m² = 0.000247105 acres)
    "ft²": (10.7639, 0),   # square feet (1 m² = 10.7639 ft²)
    "in²": (1550, 0)       # square inches (1 m² = 1,550 in²)
})
```

The converter takes a dictionary where:
- Keys are unit symbols
- Values are tuples of (scale_factor, offset)
  - For simple units like area, offset is typically 0
  - For units like temperature, offset is used for zero point differences

### Adding Support to the GUI

To add the new converter to the GUI, update the `gui.py` file:

1. Create a new converter app class:
```python
class AreaConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Area Converter")
```

2. Add the converter to the list in the main section:
```python
converters = [
    (Temperature, "Temperature"),
    (Length, "Length"),
    (Weight, "Weight"),
    (Area, "Area")  # Add the new converter
]
```

## Project Structure

- `base_class.py`: Contains the base `Converter` class
- `Converters.py`: Implements specific converters (Temperature, Length, Weight, and Volume)
- `gui.py`: Provides the graphical user interface with support for Temperature, Length, and Weight converters
- `docs/`: Contains detailed documentation for all components
- `LICENCE`: License information

## License

See the [LICENCE](LICENCE) file for details.