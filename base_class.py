class Converter:
    def __init__(self, units, factors, offsets):
        self.units = units  # List of unit names (e.g., ['Fahrenheit', 'Celsius'])
        self.factors = factors  # Conversion factors (e.g., Celsius to Fahrenheit = 9/5)
        self.offsets = offsets  # Offsets (Fahrenheit starts at 32, Celsius starts at 0)

    def convert(self, value, origin_unit, final_unit,delta=False):
        # Check if both units are valid
        if origin_unit not in self.units or final_unit not in self.units:
            raise ValueError(f"Invalid units: {origin_unit}, {final_unit}")
        # Get the index for origin and final units
        origin_index = self.units.index(origin_unit)
        final_index = self.units.index(final_unit)
        if delta:
            base_value = value/ self.factors[origin_index]

            # Now, convert to the final unit
            final_value = base_value * self.factors[final_index]
        else:
        # First, adjust the value for the origin unit offset (if any)
            base_value = (value - self.offsets[origin_index])/self.factors[origin_index]

        # Now, convert to the final unit
            final_value = base_value * self.factors[final_index] + self.offsets[final_index]
        return final_value
