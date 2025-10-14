# GUI Documentation

The `gui.py` module provides a graphical user interface for the unit converter application using Tkinter. It implements a base converter GUI class and specialized subclasses for different converter types.

## Class Hierarchy

The GUI module implements the following class hierarchy:

1. `ConverterApp` - Base class for all converter GUIs
2. Specialized converter classes:
   - `TemperatureConverterApp`
   - `LengthConverterApp`
   - `WeightConverterApp`
3. `UnitConverterApp` - Main application class that creates a tabbed interface

## Base Class: `ConverterApp`

### Overview

The `ConverterApp` class is a base frame that provides the common UI elements and functionality for all converter types. It inherits from `tk.Frame`.

### Constructor

```python
def __init__(self, parent, converter, title, *args, **kwargs)
```

#### Parameters

- `parent`: The parent widget (typically a Notebook for the tabbed interface)
- `converter`: The converter instance to use for conversions
- `title`: The title to display in the converter frame
- `*args`, `**kwargs`: Additional arguments passed to the parent Frame constructor

### Methods

#### `create_widgets`

```python
def create_widgets(self)
```

Creates all the UI elements for the converter, including:
- Title frame
- Converter frame with input, unit selection, and result display
- Utilities frame with additional options
- Error label for displaying error messages

#### `create_title_frame`

```python
def create_title_frame(self)
```

Creates the title section of the converter UI.

#### `create_converter_frame`

```python
def create_converter_frame(self)
```

Creates the main conversion interface with:
- Input field for the value to convert
- Dropdown for selecting the source unit
- Equals sign label
- Result display label
- Dropdown for selecting the target unit

#### `create_utils_frame`

```python
def create_utils_frame(self)
```

Creates utility controls:
- Checkbox for interval/delta conversion (only shown for converters with offsets)
- Swap units button

#### `create_error_label`

```python
def create_error_label(self)
```

Creates a label for displaying error messages.

#### `swap_units`

```python
def swap_units(self)
```

Swaps the selected source and target units and updates the conversion.

#### `validate_input`

```python
def validate_input(self, input_value)
```

Validates that the input is a valid number. Allows:
- Digits
- One decimal point
- Optional negative sign at the beginning
- Empty input (for clearing)

#### `convert`

```python
def convert(self, event=None)
```

Performs the conversion based on the current input and selected units. Updates the result display or shows an error message if the input is invalid.

## Specialized Converter Classes

### `TemperatureConverterApp`

```python
class TemperatureConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Temperature Converter")
```

A specialized converter app for temperature conversions.

### `LengthConverterApp`

```python
class LengthConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Length Converter")
```

A specialized converter app for length conversions.

### `WeightConverterApp`

```python
class WeightConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Weight Converter")
```

A specialized converter app for weight conversions.

## Main Application: `UnitConverterApp`

### Overview

The `UnitConverterApp` class creates the main application window with a tabbed interface for different converter types.

### Constructor

```python
def __init__(self, converters)
```

#### Parameters

- `converters`: A list of tuples, each containing a converter instance and its title

### Implementation Details

The constructor:
1. Creates the main application window
2. Sets up a Notebook (tabbed interface)
3. Creates appropriate converter tabs based on the provided converters
4. Adds each converter to the notebook as a tab

## Usage Example

```python
from Converters import Temperature, Length, Weight
from gui import UnitConverterApp

# Create a list of converters with their titles
converters = [
    (Temperature, "Temperature"),
    (Length, "Length"),
    (Weight, "Weight")
]

# Create and run the application
app = UnitConverterApp(converters)
app.mainloop()
```

## GUI Features

### Input Validation

The GUI validates input in real-time as the user types, ensuring that only valid numeric input is accepted.

### Real-time Conversion

Conversions are performed automatically as the user:
- Types in the input field
- Selects different units from the dropdowns
- Toggles the interval/delta checkbox

### Error Handling

The GUI displays error messages when:
- The input is invalid
- The conversion fails for any reason

### Interval/Delta Conversion

For converters with offsets (like temperature), the GUI provides a checkbox to toggle between:
- Regular conversion (considering both scale and offset)
- Interval/delta conversion (considering only scale)

### Unit Swapping

The "Swap Units" button allows users to quickly swap the source and target units.

## Extending the GUI

To add a new converter type to the GUI:

1. Create a new converter class in `Converters.py`
2. Create a specialized converter app class in `gui.py` (if needed)
3. Add the new converter to the `converters` list when creating the `UnitConverterApp`

Example for adding a new Volume converter:

```python
# In Converters.py
Volume = Converter({
    "L": (1, 0),
    "mL": (0.001, 0),
    # ... other volume units
})

# In gui.py
class VolumeConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Volume Converter")

# When creating the application
converters = [
    (Temperature, "Temperature"),
    (Length, "Length"),
    (Weight, "Weight"),
    (Volume, "Volume")  # Add the new converter
]

app = UnitConverterApp(converters)
app.mainloop()
```