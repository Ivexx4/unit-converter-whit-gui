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

## 🧪 Testing Environment

### Manual Testing
The project was manually tested in the following environment:

- **Operating System:** Windows 11  
- **Python Version:** 3.13.7  
- **Python Libraries:**  
  - `Tkinter` (included with Python)  
  - `pytest` (for automated testing)  
- **Notes:**  
  No additional external libraries were required for testing.

---

### Automated Testing (GitHub Actions)
Continuous Integration (CI) was configured using **GitHub Workflows** to ensure cross-platform and multi-version compatibility.  
The test matrix used was:

```yaml
matrix:
  os: [ubuntu-latest, windows-latest, macos-latest]
  python-version: ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]
  include:
    # Add Python 3.6 and 3.7 only for Windows
    - os: windows-latest
      python-version: "3.6"
    - os: windows-latest
      python-version: "3.7"

### Installation

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Ivexx4/unit-converter-whit-gui.git
   cd converter

