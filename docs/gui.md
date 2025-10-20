# Unit Converter GUI

The Unit Converter GUI provides a graphical user interface for the unit conversion library. It allows users to easily convert between different units of measurement with a user-friendly interface.

## Features

- **Tabbed Interface**: Separate tabs for Temperature, Length, Weight, and Volume conversions
- **Input Validation**: Ensures valid numeric input and handles errors gracefully
- **Automatic Conversion**: Conversion updates automatically when typing values or changing units
- **Unit Swapping**: Quickly swap between source and target units with automatic conversion
- **Delta/Interval Conversion**: Support for both absolute values and intervals (especially useful for temperature)
- **Themes**: Multiple visual themes available through the View menu
- **Keyboard Shortcuts**: Convenient shortcuts for common actions
- **Copy to Clipboard**: Easily copy conversion results to the clipboard

## Usage

### Starting the GUI

To start the Unit Converter GUI, run the following command from the project directory:

```bash
python gui.py
```

### Basic Conversion

1. Select the appropriate converter tab (Temperature, Length, Weight, or Volume)
2. Enter a value to convert in the "Value" field
   - The conversion updates automatically as you type
3. Select the source unit from the "From" dropdown
   - The conversion updates automatically when you select a unit
4. Select the target unit from the "To" dropdown
   - The conversion updates automatically when you select a unit
5. The result will be displayed in the "Result" section

Note: The "Convert" button is still available but is rarely needed since conversion happens automatically when you type a value or change units.

### Delta/Interval Conversion

For temperature conversions, you can enable delta/interval conversion by checking the "Delta/Interval Conversion" checkbox. This is useful when you want to convert temperature differences rather than absolute temperatures.

For example:
- Without delta conversion: 0°C → 32°F (absolute temperature)
- With delta conversion: 1°C → 1.8°F (temperature difference)

### Keyboard Shortcuts

The GUI supports the following keyboard shortcuts:

- **Ctrl+Q**: Exit the application
- **Ctrl+C**: Copy the current result to clipboard
- **F1**: Show help dialog
- **Alt+1 to Alt+4**: Switch between converter tabs
- **Enter**: Perform conversion (when focus is in the value field)
- **Ctrl+S**: Swap units

### Menu Options

The GUI includes a menu bar with the following options:

#### File Menu
- **Exit**: Close the application

#### Edit Menu
- **Copy Result**: Copy the current conversion result to the clipboard

#### View Menu
- **Themes**: Change the visual theme of the application

#### Help Menu
- **About**: Display information about the application
- **Help**: Show the help dialog with usage instructions

## Examples

### Temperature Conversion

1. Select the "Temperature" tab
2. Enter "25" in the Value field
   - The conversion happens automatically as you type
3. Select "ºC" from the From dropdown
   - The conversion updates automatically
4. Select "°F" from the To dropdown
   - The conversion updates automatically
5. Result: "25 ºC = 77.000000 °F"

### Length Conversion

1. Select the "Length" tab
2. Enter "1" in the Value field
   - The conversion happens automatically as you type
3. Select "mi" from the From dropdown
   - The conversion updates automatically
4. Select "km" from the To dropdown
   - The conversion updates automatically
5. Result: "1 mi = 1.609344 km"

### Weight Conversion

1. Select the "Weight" tab
2. Enter "1" in the Value field
   - The conversion happens automatically as you type
3. Select "kg" from the From dropdown
   - The conversion updates automatically
4. Select "lb" from the To dropdown
   - The conversion updates automatically
5. Result: "1 kg = 2.204620 lb"

### Volume Conversion

1. Select the "Volume" tab
2. Enter "1" in the Value field
   - The conversion happens automatically as you type
3. Select "L" from the From dropdown
   - The conversion updates automatically
4. Select "gal" from the To dropdown
   - The conversion updates automatically
5. Result: "1 L = 0.264172 gal"

## Extending the GUI

The GUI is designed to automatically incorporate any new converters added to the `Converters.py` file. If you add a new converter (e.g., Area), it will appear as a new tab in the GUI without requiring changes to the GUI code.