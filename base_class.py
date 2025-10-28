# -*- coding: utf-8 -*-
from numbers import Number
from typing import Union, Tuple, Dict, List


class Converter:
    """
    A flexible unit conversion class that can handle various unit types.
    
    This class provides a framework for converting between different units of measurement.
    It can handle both simple scaling conversions (like length) and conversions with 
    offsets (like temperature).
    
    Attributes:
        units (Dict[str, Tuple[Number, Number]]): Dictionary of unit symbols mapped to 
            their conversion factors as (scale_factor, offset) tuples.
    """
    
    def __init__(self, units: Dict[str, Union[Number, Tuple[Number, Number], List[Number]]]):
        """
        Initialize a Converter with a dictionary of units and their conversion factors.
        
        Args:
            units: A dictionary where:
                - Keys are unit symbols (strings)
                - Values can be:
                    - A single number (scale factor)
                    - A tuple of two numbers (scale factor, offset)
                    - A list of two numbers [scale factor, offset]
                    
        Raises:
            ValueError: If a list or tuple value doesn't contain exactly two numbers
            TypeError: If a value is not a number, list of two numbers, or tuple of two numbers
            
        Note:
            The constructor normalizes all unit values to tuples of (scale_factor, offset).
            For simple unit types (length, weight, etc.), offset is typically 0.
            For units with different zero points (like temperature), offset is non-zero.
        """
        self.units = units

        # Iterate over the keys and values in the `self.units` dictionary
        for unit, value in self.units.items():
            # Check if the value is a single number
            if isinstance(value, Number):
                # If it's a number, convert it to a tuple (value, 1)
                self.units[unit] = (value, 1)
            # Check if the value is a list with exactly two numbers
            elif isinstance(value, list):
                if len(value) == 2 and all(isinstance(i, Number) for i in value):
                    # Convert the list to a tuple
                    self.units[unit] = tuple(value)
                else:
                    raise ValueError(f"The value for '{unit}' must be a list with exactly two numbers.")
            # Check if the value is already a tuple with exactly two numbers
            elif isinstance(value, tuple):
                if len(value) == 2 and all(isinstance(i, Number) for i in value):
                    continue  # Valid tuple, leave as is
                else:
                    raise ValueError(f"The value for '{unit}' must be a tuple with exactly two numbers.")
            else:
                raise TypeError(f"The value for '{unit}' must be a valid number, list of two numbers, or a tuple of two numbers.")


    def convert(self, value, origin_unit, final_unit, delta=False):
        """
        Convert a value from one unit to another.
        
        This method converts a value from the origin unit to the final unit.
        It can handle both absolute conversions and delta/interval conversions.
        
        Args:
            value (Number): The numeric value to convert
            origin_unit (str): The source unit (must be a key in the units dictionary)
            final_unit (str): The target unit (must be a key in the units dictionary)
            delta (bool, optional): Flag indicating whether this is a delta/interval conversion.
                When True, only the scale factor is used (offsets are ignored).
                When False (default), both scale factor and offset are applied.
                
        Returns:
            float: The converted value
            
        Raises:
            ValueError: If either the origin or final unit is not in the units dictionary
            
        Examples:
            >>> temp_converter = Converter({"°C": (1, 0), "°F": (1.8, 32)})
            >>> temp_converter.convert(25, "°C", "°F")
            77.0
            >>> temp_converter.convert(10, "°C", "°F", delta=True)
            18.0
        """
        # Check if both units are valid
        if origin_unit not in self.units.keys() or final_unit not in self.units.keys():
            raise ValueError(f"Invalid units: {origin_unit}, {final_unit}")

        if delta:
            # For delta conversions, only apply scale factors (ignore offsets)
            base_value = value / self.units[origin_unit][0]

            # Now, convert to the final unit
            final_value = base_value * self.units[final_unit][0]
        else:
            # For absolute conversions, apply both scale factors and offsets
            # First, adjust the value for the origin unit offset (if any)
            base_value = (value - self.units[origin_unit][1]) / self.units[origin_unit][0]
            # Now, convert to the final unit
            final_value = base_value * self.units[final_unit][0] + self.units[final_unit][1]

        return final_value
