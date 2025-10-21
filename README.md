# Unit Converter

A flexible and extensible unit conversion library with a graphical user interface. This project provides a framework for converting between different units of measurement, with support for temperature, length, weight, and volume conversions.

## Features

- **Modular Design**: Base converter class that can be extended for any unit type.
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

### Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python, but may require separate installation on certain Linux distributions)

### Test Environment

The application has been tested in the following environments:

- **Operating System**: Windows 11
- **Python Version**: 3.13.7
- **Python Libraries**:
  - Tkinter (included with Python)
  - pytest (for automatic testing)
  - No additional external libraries were required for testing
- **IDE/Editor**: PyCharm
- **Testing Method**:
  - **Manual Testing**: 
    - Via the GUI and command line interface
  - **Automated Testing**: 
    - Using `pytest` for unit and integration tests to ensure functionality across different modules.
- **Virtual Environment**:
  - Testing was done within a **conda environment**:
    - Environment name: `unit-converter-env`
    - Created with: `conda create --name unit-converter-env python=3.13.7`
    - Dependencies: Standard Python libraries, `pytest`, and `tkinter` (included with Python)

### Installation

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Ivexx4/unit-converter-whit-gui.git
   cd converter

