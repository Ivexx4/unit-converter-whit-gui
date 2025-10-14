# Unit Converter

A flexible and extensible unit conversion library with a graphical user interface. This project provides a framework for converting between different units of measurement, with current support for temperature conversions.

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
from Converters import Temperature

# Convert from Celsius to Fahrenheit
result = Temperature.convert(25, "ºC", "°F")
print(f"25 ºC = {result:.2f} °F")  # Output: 25 ºC = 77.00 °F

# Convert from Kelvin to Celsius
result = Temperature.convert(300, "K", "ºC")
print(f"300 K = {result:.2f} ºC")  # Output: 300 K = 26.85 ºC
```

### Graphical User Interface

To launch the GUI application:

```python
python gui.py
```

This will open a tabbed interface with the Temperature converter. The GUI allows you to:
1. Enter a value to convert
2. Select the source unit
3. Select the target unit
4. View the converted result
5. Toggle between absolute and interval (delta) conversions
6. Swap units with a single button click

## Extending the Converter

### Adding New Unit Types

To add a new unit type (e.g., Length), create a new converter in `Converters.py`:

```python
from base_class import Converter

# Define a Length converter
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

The converter takes a dictionary where:
- Keys are unit symbols
- Values are tuples of (scale_factor, offset)
  - For simple units like length, offset is typically 0
  - For units like temperature, offset is used for zero point differences

## Project Structure

- `base_class.py`: Contains the base `Converter` class
- `Converters.py`: Implements specific converters (currently Temperature)
- `gui.py`: Provides the graphical user interface
- `LICENCE`: License information

## License

See the [LICENCE](LICENCE) file for details.