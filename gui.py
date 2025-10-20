"""
Unit Converter GUI Module

This module provides a graphical user interface for the unit converter application
using Tkinter. It implements a base converter GUI class and specialized subclasses
for different converter types.

The module includes the following classes:
    - ConverterApp: Base class for all converter GUIs
    - TemperatureConverterApp: Specialized converter for temperature units
    - LengthConverterApp: Specialized converter for length units
    - WeightConverterApp: Specialized converter for weight units
    - UnitConverterApp: Main application class that creates a tabbed interface

The GUI allows users to:
    - Enter a value to convert
    - Select source and target units
    - View the converted result
    - Toggle between absolute and interval (delta) conversions
    - Swap units with a single button click
"""

import tkinter as tk
from tkinter import ttk
class ConverterApp(tk.Frame):
    """
    Base class for all converter GUI components.
    
    This class provides the common UI elements and functionality for all converter types.
    It inherits from tk.Frame and creates a complete converter interface with input field,
    unit selection dropdowns, result display, and utility controls.
    
    Attributes:
        converter: The converter instance to use for conversions
        title: The title to display in the converter frame
        value_entry: Entry widget for the value to convert
        origin_unit_combobox: Dropdown for selecting the source unit
        final_unit_combobox: Dropdown for selecting the target unit
        result_label: Label for displaying the conversion result
        is_interval_var: Boolean variable for the interval/delta checkbox
        error_label: Label for displaying error messages
    """
    
    def __init__(self, parent, converter, title, *args, **kwargs):
        """
        Initialize a ConverterApp with a parent widget, converter instance, and title.
        
        Args:
            parent: The parent widget (typically a Notebook for the tabbed interface)
            converter: The converter instance to use for conversions
            title: The title to display in the converter frame
            *args, **kwargs: Additional arguments passed to the parent Frame constructor
        """
        super().__init__(parent, *args, **kwargs)
        self.converter = converter
        self.title = title
        self.create_widgets()

    def configure_rows(self):
        """
        Configure the row weights for the frame layout.
        
        This method sets up the relative weights of the rows in the frame,
        determining how they expand when the window is resized.
        """
        self.rowconfigure(0, weight=0)  # Title row (fixed height)
        self.rowconfigure(1, weight=1)  # Converter row (expands)
        self.rowconfigure(2, weight=1)  # Utils row (expands)
        
    def create_widgets(self):
        """
        Create all the UI elements for the converter.
        
        This method calls other methods to create the different sections of the UI:
        - Title frame with the converter title
        - Converter frame with input, unit selection, and result display
        - Utilities frame with additional options
        - Error label for displaying error messages
        """
        self.create_title_frame()
        self.create_converter_frame()
        self.create_utils_frame()
        self.create_error_label()

    def create_title_frame(self):
        """
        Create the title section of the converter UI.
        
        This method creates a frame with a centered title label using the title
        provided during initialization. The title is displayed with a larger font.
        """
        self.title_fr = tk.Frame(self)
        self.title_fr.grid(row=0, column=0, pady=10)
        title_label = tk.Label(self.title_fr, text=self.title, font=("Helvetica", 16))
        title_label.place(relx=0.5, rely=0.3, anchor="center")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title_fr.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def create_converter_frame(self):
        """
        Create the main conversion interface.
        
        This method creates the central part of the UI with:
        - Input field for the value to convert (with validation)
        - Dropdown for selecting the source unit
        - Equals sign label
        - Result display label
        - Dropdown for selecting the target unit
        
        The method also sets up event bindings to trigger conversion when:
        - The user types in the input field
        - The user selects a different unit from either dropdown
        """
        converter_frame = tk.Frame(self)
        
        # Set up input validation
        self.validate_cmd = self.register(self.validate_input)
        
        # Create and position the input field
        self.value_entry = tk.Entry(converter_frame, validate="key", validatecommand=(self.validate_cmd, "%P"))
        self.value_entry.grid(row=0, column=1, padx=5, sticky="ew")
        self.value_entry.bind("<KeyRelease>", self.convert)
        self.grid_columnconfigure(1, weight=1)
        
        # Create and position the source unit dropdown
        self.origin_unit_combobox = ttk.Combobox(converter_frame, values=self.converter.units)
        self.origin_unit_combobox.grid(row=0, column=2, padx=5, sticky="ew")
        self.origin_unit_combobox.set(self.converter.units[0])
        
        # Create and position the target unit dropdown
        self.final_unit_combobox = ttk.Combobox(converter_frame, values=self.converter.units)
        
        # Create and position the equals sign
        equals_label = tk.Label(converter_frame, text="=")
        equals_label.grid(row=0, column=3)
        
        # Create and position the result label
        self.result_label = tk.Label(converter_frame, text=" ")
        self.result_label.grid(row=0, column=4, padx=5)
        
        # Position the target unit dropdown
        self.final_unit_combobox.grid(row=0, column=5, padx=5, sticky="ew")
        self.final_unit_combobox.set(self.converter.units[1])
        
        # Position the entire converter frame
        converter_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        
        # Set up event bindings for the dropdowns
        self.origin_unit_combobox.bind("<<ComboboxSelected>>", self.convert)
        self.final_unit_combobox.bind("<<ComboboxSelected>>", self.convert)

    def create_utils_frame(self):
        """
        Create utility controls for the converter.
        
        This method creates:
        - Checkbox for interval/delta conversion (only shown for converters with offsets)
        - Swap units button
        
        The interval checkbox is only displayed for converters that have non-zero offsets
        (like temperature), where absolute and delta conversions differ.
        """
        utils_frame = tk.Frame(self)
        
        # Check if any unit has a non-zero offset
        # Fix: Access the units dictionary and check the second element (offset) of each tuple
        if any(unit_info[1] != 0 for unit_info in self.converter.units.values()):
            # Create checkbox for interval/delta conversion
            self.is_interval_var = tk.BooleanVar()
            self.is_interval_checkbox = tk.Checkbutton(utils_frame, text="Interval (delta)", variable=self.is_interval_var)
            self.is_interval_checkbox.grid(column=0, pady=5)
            self.is_interval_checkbox.bind("<ButtonRelease-1>", self.convert)
        else:
            # For converters without offsets, delta and absolute conversions are the same
            self.is_interval_var = tk.BooleanVar(value=True)

        # Create swap units button
        self.swap_button = tk.Button(self, text="Swap Units", command=self.swap_units)
        self.swap_button.grid(column=2, padx=10, pady=5)
        utils_frame.grid(row=2, sticky="nsew")
    def create_error_label(self):
        """
        Create a label for displaying error messages.
        
        This method creates a label at the bottom of the converter frame
        that is used to display error messages when conversion fails.
        The label is initially empty.
        """
        self.error_label = tk.Label(self, text="")
        self.error_label.grid(row=3)
    def swap_units(self):
        """Swaps the selected units between origin and final."""
        origin_unit = self.origin_unit_combobox.get()
        final_unit = self.final_unit_combobox.get()

        # Swap the selections
        self.origin_unit_combobox.set(final_unit)
        self.final_unit_combobox.set(origin_unit)
        self.convert()

    def validate_input(self, input_value):
        """
        This method checks if the input is a valid number.
        It allows digits, one decimal point, and an optional negative sign at the beginning.
        """
        if input_value == "":  # Empty input is allowed (clearing the entry)
            return True
        try:
            # Attempt to convert input to a float
            float(input_value)
            return True
        except ValueError:
            return False

    def convert(self, event=None):
        """
        Perform the conversion based on the current input and selected units.
        
        This method is called automatically when:
        - The user types in the input field
        - The user selects a different unit from either dropdown
        - The user toggles the interval/delta checkbox
        - The user clicks the swap units button
        
        It retrieves the input value and selected units, performs the conversion
        using the converter instance, and updates the result display. If the
        conversion fails (e.g., due to invalid input or units), it displays an
        error message.
        
        Args:
            event: The event that triggered the conversion (optional, can be None)
        """
        value = self.value_entry.get()
        if not value.strip():  # If the input is empty
            self.result_label.config(text=" ")
            self.error_label.config(text="")  # Clear any error message
            return

        try:
            # Get the input values
            value = value.replace(" ", "")
            value = float(value)
            origin_unit = self.origin_unit_combobox.get()
            final_unit = self.final_unit_combobox.get()
            is_interval = self.is_interval_var.get()

            # Call the convert method from the Converter class
            result = self.converter.convert(value, origin_unit, final_unit, delta=is_interval)
            self.result_label.config(text=f"{result:.2f}")
            self.error_label.config(text="")  # Clear error message if conversion is successful

        except ValueError:
            # If there is an error, reset the result and show an error message
            self.result_label.config(text=" ")
            self.error_label.config(text="Error: Invalid input!")


class TemperatureConverterApp(ConverterApp):
    """
    Specialized converter app for temperature conversions.
    
    This class inherits from ConverterApp and provides a GUI for converting
    between different temperature scales (Celsius, Fahrenheit, Kelvin, etc.).
    """
    def __init__(self, parent, converter):
        """
        Initialize a TemperatureConverterApp with a parent widget and converter instance.
        
        Args:
            parent: The parent widget (typically a Notebook for the tabbed interface)
            converter: The Temperature converter instance to use for conversions
        """
        super().__init__(parent, converter, "Temperature Converter")


class LengthConverterApp(ConverterApp):
    """
    Specialized converter app for length conversions.
    
    This class inherits from ConverterApp and provides a GUI for converting
    between different length units (meters, feet, inches, etc.).
    """
    def __init__(self, parent, converter):
        """
        Initialize a LengthConverterApp with a parent widget and converter instance.
        
        Args:
            parent: The parent widget (typically a Notebook for the tabbed interface)
            converter: The Length converter instance to use for conversions
        """
        super().__init__(parent, converter, "Length Converter")


class WeightConverterApp(ConverterApp):
    """
    Specialized converter app for weight conversions.
    
    This class inherits from ConverterApp and provides a GUI for converting
    between different weight units (kilograms, pounds, ounces, etc.).
    """
    def __init__(self, parent, converter):
        """
        Initialize a WeightConverterApp with a parent widget and converter instance.
        
        Args:
            parent: The parent widget (typically a Notebook for the tabbed interface)
            converter: The Weight converter instance to use for conversions
        """
        super().__init__(parent, converter, "Weight Converter")


class UnitConverterApp(tk.Tk):
    """
    Main application class that creates a tabbed interface for multiple converters.
    
    This class inherits from tk.Tk and creates a window with a tabbed interface,
    where each tab contains a different converter (Temperature, Length, Weight, etc.).
    It dynamically creates the appropriate converter app for each converter type.
    
    Attributes:
        title: The title of the application window
        geometry: The size of the application window
    """
    def __init__(self, converters):
        """
        Initialize a UnitConverterApp with a list of converters.
        
        Args:
            converters: A list of tuples, each containing a converter instance and its title
                Example: [(Temperature, "Temperature"), (Length, "Length"), ...]
        """
        super().__init__()

        self.title("Unit Converter")
        self.geometry("600x400")

        # Create the Notebook (tab container)
        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True, fill="both")

        # Create tabs for different converters
        for converter, title in converters:
            if title == "Temperature":
                tab = TemperatureConverterApp(notebook, converter)
            elif title == "Length":
                tab = LengthConverterApp(notebook, converter)
            elif title == "Weight":
                tab = WeightConverterApp(notebook, converter)
            else:
                continue  # Handle other converters here if needed

            # Add tabs to the notebook
            notebook.add(tab, text=title)


if __name__ == "__main__":
    # Example converter (assuming the Converter class and its instances are already defined)
    from Converters import Temperature, Length, Weight  # Adjust import accordingly

    converters = [
        (Temperature, "Temperature"),
        (Length, "Length"),
        (Weight, "Weight")
    ]

    # Create the main application window and pass the converters to it
    app = UnitConverterApp(converters)
    app.mainloop()
