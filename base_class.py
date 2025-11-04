from numbers import Number
from typing import Union, Tuple, Dict, List
from collections.abc import Iterable, MutableMapping,MutableSequence,MutableSet


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

    def convert(self, value, origin_unit, final_unit, delta=False, inplace=False):
        """
            Converts a value or collection (number, string, dict, list, iterable) from one unit to another, optionally as a delta or in place; raises TypeError for unsupported types or invalid strings.
            """
        if isinstance(value,str):
            try:
                value=float(value)
            except ValueError:
                raise TypeError("type not supported")
        if isinstance(value, Number):
            return self._single_convertion(value, origin_unit, final_unit, delta)
        elif isinstance(value, MutableMapping):
            return self._dict_convertion(value, origin_unit, final_unit, delta,inplace)
        elif isinstance(value, MutableSequence):
            return self._mut_sequence_convertion(value, origin_unit, final_unit, delta,inplace)
        elif isinstance(value, Iterable):
            return self._imut_iterable_convertion(value, origin_unit, final_unit, delta)
        else:
            raise TypeError("type not supported")

    def _mut_sequence_convertion(self, value: Iterable, origin_unit: str, final_unit: str, delta,inplace):
        """
        Converts each element in an mutable iterable from the origin unit to the final unit.
        Returns the iterable of the same type as the input.
        """
        converted_values = [self._single_convertion(val, origin_unit, final_unit, delta) for val in value]
        if inplace:
            value[:] = converted_values
            return value
        else:
            return converted_values

    def _dict_convertion(self,value, origin_unit, final_unit, delta,inplace):
        """
                Converts all values in the dictionary from the origin unit to the final unit.
                """
        converted_dict = {key: self._single_convertion(val, origin_unit, final_unit, delta) for key, val in value.items()}
        if inplace:
            value.update(converted_dict)
            return value
        return converted_dict

    def _imut_iterable_convertion(self, value: Iterable, origin_unit: str, final_unit: str, delta):
        """
        Converts each element in an immutable iterable from the origin unit to the final unit.
        Returns the iterable of the same type as the input.
        """
        converted_values = [self._single_convertion(val, origin_unit, final_unit, delta) for val in value]
        return type(value)(converted_values)  # Return the iterable of the same type

    def _single_convertion(self, value, origin_unit, final_unit, delta=False):
        """
        Convert a single value from one unit to another.
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
