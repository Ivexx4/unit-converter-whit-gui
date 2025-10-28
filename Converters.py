# -*- coding: utf-8 -*-
"""
Unit Converters Module

This module implements specific converter instances using the base Converter class.
It provides converters for Temperature, Length, Weight, and Volume units.

Each converter is an instance of the Converter class, initialized with a dictionary
of units and their conversion factors. The conversion factors are specified as
tuples of (scale_factor, offset).

Available Converters:
    - Temperature: Convert between temperature scales (Celsius, Fahrenheit, Kelvin, etc.)
    - Length: Convert between length units (meters, feet, inches, etc.)
    - Weight: Convert between weight/mass units (kilograms, pounds, etc.)
    - Volume: Convert between volume units (liters, gallons, etc.)

Example Usage:
    >>> from Converters import Temperature
    >>> Temperature.convert(25, "ºC", "°F")
    77.0
"""

from base_class import Converter

# Temperature converter - Converts between different temperature scales (Celsius, Fahrenheit, Kelvin, etc.)
# Base unit: Celsius (ºC) with scale factor 1 and offset 0
Temperature = Converter({
    "°F":(1.8,32),
    "ºC":(1,0),
    "K":(1,273.15),
    "ºR":(1.8,491.67),
    "ºD":(-1.5,150),
    "ºRe":(0.8,0),
    "ºN":(0.33,0),
    "ºRø":(21/40,7.5)}# Units
)

# Length converter - Converts between different units of length/distance (meters, feet, inches, etc.)
# Base unit: Meter (m) with scale factor 1 and offset 0
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

# Weight converter - Converts between different units of weight/mass (kilograms, pounds, ounces, etc.)
# Base unit: Kilogram (kg) with scale factor 1 and offset 0
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

# Volume converter - Converts between different units of volume (liters, gallons, cubic meters, etc.)
# Base unit: Liter (L) with scale factor 1 and offset 0
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
if __name__ == "__main__":
    def test():
    # Temperature conversion examples
        print("\nTemperature Conversion Examples:")
        print(f"75 ºD = {Temperature.convert(75, "ºD", "ºC"):.2f}°C.")
        print(f"32 ºF = {Temperature.convert(32, "°F", "ºC"):.2f}°C.")
        print(f"300 K = {Temperature.convert(300, 'K', '°F'):.2f}°F.")
        print(f"25 ºC = {Temperature.convert(25, "ºC", "ºR"):.2f}°R.")
        print(f"10 ºRe = {Temperature.convert(10, "ºRe", "K"):.2f} K.")
        print(f"10 ºD = {Temperature.convert(10, "ºD", 'ºN'):.2f}°N.")
        print(f"10 ºRø = {Temperature.convert(10, 'ºRø', "ºC"):.2f}°C.")
    
    # Length conversion examples
        print("\nLength Conversion Examples:")
        print(f"1 m = {Length.convert(1, 'm', 'ft'):.2f} ft.")
        print(f"1 mi = {Length.convert(1, 'mi', 'km'):.2f} km.")
        print(f"10 in = {Length.convert(10, 'in', 'cm'):.2f} cm.")
        print(f"100 yd = {Length.convert(100, 'yd', 'm'):.2f} m.")

    
    # Weight conversion examples
        print("\nWeight Conversion Examples:")
        print(f"1 kg = {Weight.convert(1, 'kg', 'lb'):.2f} lb.")
        print(f"1 lb = {Weight.convert(1, 'lb', 'g'):.2f} g.")
        print(f"10 oz = {Weight.convert(10, 'oz', 'g'):.2f} g.")
        print(f"1 ton = {Weight.convert(1, 'ton', 'uston'):.2f} US tons.")
    
    # Volume conversion examples
        print("\nVolume Conversion Examples:")
        print(f"1 L = {Volume.convert(1, 'L', 'gal'):.2f} gallons.")
        print(f"1 gal = {Volume.convert(1, 'gal', 'L'):.2f} L.")
        print(f"1 m³ = {Volume.convert(1, 'm³', 'L'):.2f} L.")
        print(f"1 cup = {Volume.convert(1, 'cup', 'mL'):.2f} mL.")

    test()
