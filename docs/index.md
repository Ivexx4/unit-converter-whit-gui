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

Currently, the project supports temperature conversions between multiple scales, including Celsius, Fahrenheit, Kelvin, Rankine, Delisle, Réaumur, Newton, and Rømer.

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

The project consists of three main modules:

- [Base Class](base_class.md) - Documentation for the core `Converter` class
- [Converters](converters.md) - Documentation for specific converter implementations
- [GUI](gui.md) - Documentation for the graphical user interface

## Usage Examples

### Command Line Usage

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

### GUI Usage

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

The Unit Converter is designed to be easily extended with new unit types. See the following documentation for details:

- [Adding New Converters](converters.md#creating-additional-converters)
- [Extending the GUI](gui.md#extending-the-gui)

## License

This project is licensed under the terms specified in the [LICENCE](../LICENCE) file.