from numbers import Number
from typing import Union, Tuple, Dict, List


class Converter:
    def __init__(self, units: Dict[str, Union[Number, Tuple[Number, Number], List[Number]]]):
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


    def convert(self, value, origin_unit, final_unit,delta=False):
        # Check if both units are valid
        if origin_unit not in self.units.keys() or final_unit not in self.units.keys():
            raise ValueError(f"Invalid units: {origin_unit}, {final_unit}")

        if delta:
            base_value = value/ self.units[origin_unit][0]

            # Now, convert to the final unit
            final_value = base_value * self.units[final_unit][0]
        else:
        # First, adjust the value for the origin unit offset (if any)
            base_value = (value - self.units[origin_unit][1])/self.units[origin_unit][0]
        # Now, convert to the final unit
            final_value = base_value * self.units[final_unit][0] + self.units[final_unit][1]

        return final_value
