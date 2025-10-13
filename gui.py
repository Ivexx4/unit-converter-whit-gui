import tkinter as tk
from tkinter import ttk
# Base class for unit converter GUI
class ConverterApp(tk.Frame):
    def __init__(self, parent, converter, title, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.converter = converter
        self.title = title
        self.create_widgets()

    def configure_rows(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
    def create_widgets(self):
        # Set up the UI elements
        self.create_title_frame()
        self.create_converter_frame()
        self.create_utils_frame()
        self.create_error_label()

    def create_title_frame(self):
            self.title_fr = tk.Frame(self)
            self.title_fr.grid(row=0, column=0, pady=10)
            title_label = tk.Label(self.title_fr, text=self.title, font=("Helvetica", 16))
            title_label.place(relx=0.5, rely=0.3, anchor="center")
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.title_fr.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def create_converter_frame(self):
        converter_frame = tk.Frame(self)
        self.validate_cmd = self.register(self.validate_input)
        self.value_entry = tk.Entry(converter_frame, validate="key", validatecommand=(self.validate_cmd, "%P"))
        self.value_entry.grid(row=0, column=1, padx=5, sticky="ew")
        self.value_entry.bind("<KeyRelease>", self.convert)
        self.grid_columnconfigure(1, weight=1)
        self.origin_unit_combobox = ttk.Combobox(converter_frame, values=self.converter.units)
        self.origin_unit_combobox.grid(row=0, column=2, padx=5, sticky="ew")
        self.origin_unit_combobox.set(self.converter.units[0])
        self.final_unit_combobox = ttk.Combobox(converter_frame, values=self.converter.units)
        equals_label = tk.Label(converter_frame, text="=")
        equals_label.grid(row=0, column=3)
        self.result_label = tk.Label(converter_frame, text=" ")
        self.result_label.grid(row=0, column=4, padx=5)
        self.final_unit_combobox.grid(row=0, column=5, padx=5, sticky="ew")
        self.final_unit_combobox.set(self.converter.units[1])
        converter_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.origin_unit_combobox.bind("<<ComboboxSelected>>", self.convert)
        self.final_unit_combobox.bind("<<ComboboxSelected>>", self.convert)

    def create_utils_frame(self):
        utils_frame = tk.Frame(self)
        if any(valor != 0 for valor in self.converter.offsets):
            self.is_interval_var = tk.BooleanVar()
            self.is_interval_checkbox = tk.Checkbutton(utils_frame, text="Interval (delta)", variable=self.is_interval_var)
            self.is_interval_checkbox.grid(column=0, pady=5)
            self.is_interval_checkbox.bind("<ButtonRelease-1>", self.convert)
        else :
            self.is_interval_var = tk.BooleanVar(value=True)

        self.swap_button = tk.Button(self, text="Swap Units", command=self.swap_units)
        self.swap_button.grid(column=2, padx=10, pady=5)
        utils_frame.grid(row=2, sticky="nsew")
    def create_error_label(self):
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


# Derived class for Temperature Conversion (inherits from ConverterApp)
class TemperatureConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Temperature Converter")


# Derived class for Length Conversion (inherits from ConverterApp)
class LengthConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Length Converter")


# Derived class for Weight Conversion (inherits from ConverterApp)
class WeightConverterApp(ConverterApp):
    def __init__(self, parent, converter):
        super().__init__(parent, converter, "Weight Converter")


# Main Application that manages the tabbed interface
class UnitConverterApp(tk.Tk):
    def __init__(self, converters):
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
