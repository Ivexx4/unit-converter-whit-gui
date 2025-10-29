"""
Unit Converter GUI

This module implements a graphical user interface for the unit converter library.
It provides a user-friendly interface for converting between different units of measurement,
with support for temperature, length, weight, and volume conversions.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import Converters
class ConverterGUI:
    """
    A graphical user interface for the unit converter library.
    
    This class provides a Tkinter-based interface for converting between different
    units of measurement, with support for temperature, length, weight, and volume conversions.
    
    Attributes:
        root (tk.Tk): The root Tkinter window
        notebook (ttk.Notebook): A notebook widget for tabbed interface
        converters (dict): Dictionary mapping converter names to converter objects
        style (ttk.Style): Style configuration for the application
    """
    
    def __init__(self, root, converters):
        """
        Initialize the ConverterGUI with a root Tkinter window.
        
        Args:
            root (tk.Tk): The root Tkinter window
        """
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("550x450")
        self.root.resizable(True, True)
        
        # Set application icon (if available)
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass  # Icon not found, use default
        
        # Apply a theme
        self.style = ttk.Style()
        try:
            self.style.theme_use('clam')  # Use a more modern theme if available
        except:
            pass  # Use default theme if 'clam' is not available
        
        # Configure styles
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TEntry', font=('Arial', 10))
        self.style.configure('TCombobox', font=('Arial', 10))
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TFrame', background='#f0f0f0')
        
        # Set up the converters dictionary
        self.converters = converters
        
        # Create a menu bar
        self.create_menu()
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs for each converter
        for converter_name, converter in self.converters.items():
            tab = self.create_converter_tab(converter_name, converter)
            self.notebook.add(tab, text=converter_name)
            
        # Set up keyboard shortcuts
        self.setup_keyboard_shortcuts()
    
    def create_converter_tab(self, converter_name, converter):
        """
        Create a tab for a specific converter.
        
        Args:
            converter_name (str): The name of the converter
            converter (Converter): The converter object
            
        Returns:
            ttk.Frame: The frame containing the converter interface
        """
        frame = ttk.Frame(self.notebook, padding=10)
        
        # Get the units for this converter
        units = list(converter.units.keys())
        
        # Create the input section
        input_frame = ttk.LabelFrame(frame, text="Input", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Label(input_frame, text="Value:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        # Use StringVar for the value entry to track changes
        value_var = tk.StringVar()
        value_var.set("0")
        value_entry = ttk.Entry(input_frame, width=15, textvariable=value_var)
        value_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(input_frame, text="From:").grid(row=1, column=0, sticky=tk.W, pady=5)
        from_unit = tk.StringVar()
        from_unit.set(units[0])
        from_dropdown = ttk.Combobox(input_frame, textvariable=from_unit, values=units, state="readonly", width=12)
        from_dropdown.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(input_frame, text="To:").grid(row=2, column=0, sticky=tk.W, pady=5)
        to_unit = tk.StringVar()
        to_unit.set(units[1] if len(units) > 1 else units[0])
        to_dropdown = ttk.Combobox(input_frame, textvariable=to_unit, values=units, state="readonly", width=12)
        to_dropdown.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Bind events to update conversion when units are changed
        def on_unit_change(event):
            self.convert(
                converter,
                value_var.get(),
                from_unit.get(),
                to_unit.get(),
                delta_var.get(),
                result_var
            )
            
        from_dropdown.bind("<<ComboboxSelected>>", on_unit_change)
        to_dropdown.bind("<<ComboboxSelected>>", on_unit_change)
        
        # Add trace callback to update conversion when value changes
        def on_value_change(*args):
            # Get the current value
            value_str = value_var.get()
            
            # Skip conversion if value is empty or not a valid number
            if not value_str.strip():
                return
                
            try:
                # Try to convert to float to validate
                float(value_str)
                
                # If valid, perform the conversion
                self.convert(
                    converter,
                    value_str,
                    from_unit.get(),
                    to_unit.get(),
                    delta_var.get(),
                    result_var
                )
            except ValueError:
                # If not a valid number, don't update the conversion
                pass
                
        # Register the trace callback
        value_var.trace_add("write", on_value_change)
        
        # Add a checkbox for delta conversion (for temperature)
        delta_var = tk.BooleanVar()
        delta_var.set(False)
        delta_check = ttk.Checkbutton(input_frame, text="Delta/Interval Conversion", variable=delta_var)
        delta_check.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Create the output section
        output_frame = ttk.LabelFrame(frame, text="Result", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        result_var = tk.StringVar()
        result_var.set("0")
        result_label = ttk.Label(output_frame, textvariable=result_var, font=("Arial", 12))
        result_label.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create the buttons section
        button_frame = ttk.Frame(frame, padding=10)
        button_frame.pack(fill=tk.X, pady=5)
        
        # Convert button
        convert_button = ttk.Button(
            button_frame, 
            text="Convert", 
            command=lambda: self.convert(
                converter, 
                value_var.get(), 
                from_unit.get(), 
                to_unit.get(), 
                delta_var.get(), 
                result_var
            )
        )
        convert_button.pack(side=tk.LEFT, padx=5)
        
        # Swap button
        swap_button = ttk.Button(
            button_frame, 
            text="Swap Units", 
            command=lambda: self.swap_units(
                converter,
                value_var.get(),
                from_unit,
                to_unit,
                delta_var.get(),
                result_var
            )
        )
        swap_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_button = ttk.Button(
            button_frame, 
            text="Clear", 
            command=lambda: self.clear(value_entry, value_var, result_var)
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        return frame
    
    def convert(self, converter, value_str, from_unit, to_unit, delta, result_var):
        """
        Convert a value from one unit to another.
        
        Args:
            converter (Converter): The converter object
            value_str (str): The value to convert as a string
            from_unit (str): The source unit
            to_unit (str): The target unit
            delta (bool): Flag indicating whether this is a delta/interval conversion
            result_var (tk.StringVar): The StringVar to update with the result
        """
        try:
            # Validate input is not empty
            if not value_str.strip():
                messagebox.showerror("Invalid Input", "Please enter a value to convert.")
                return
                
            # Validate input is a valid number
            try:
                value = float(value_str)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")
                return
            
            # Validate units are not the same
            if from_unit == to_unit:
                # If units are the same, just format the result
                if abs(value) < 0.001 or abs(value) > 1000:
                    result_str = f"{value:.6e}"
                else:
                    result_str = f"{value:.6f}"
                result_var.set(f"{value_str} {from_unit} = {result_str} {to_unit}")
                return
            
            # Perform the conversion
            try:
                result = converter.convert(value, from_unit, to_unit, delta)
                
                # Format the result
                if abs(result) < 0.001 or abs(result) > 1000:
                    result_str = f"{result:.6e}"
                else:
                    result_str = f"{result:.6f}"
                
                # Update the result label
                result_var.set(f"{value_str} {from_unit} = {result_str} {to_unit}")
                
            except ValueError as ve:
                messagebox.showerror("Conversion Error", f"Invalid units: {from_unit}, {to_unit}")
            except Exception as e:
                messagebox.showerror("Conversion Error", f"An error occurred during conversion: {str(e)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    def swap_units(self, converter, value_str, from_unit, to_unit, delta, result_var):
        """
        Swap the from and to units and automatically perform the conversion.
        
        Args:
            converter (Converter): The converter object
            value_str (str): The value to convert as a string
            from_unit (tk.StringVar): The from unit StringVar
            to_unit (tk.StringVar): The to unit StringVar
            delta (bool): Flag indicating whether this is a delta/interval conversion
            result_var (tk.StringVar): The StringVar to update with the result
        """
        # Swap the units
        from_value = from_unit.get()
        to_value = to_unit.get()
        from_unit.set(to_value)
        to_unit.set(from_value)
        
        # Automatically perform the conversion with the swapped units
        self.convert(converter, value_str, from_unit.get(), to_unit.get(), delta, result_var)
    
    def clear(self, value_entry, value_var, result_var):
        """
        Clear the input and result.
        
        Args:
            value_entry (ttk.Entry): The value entry widget
            value_var (tk.StringVar): The value StringVar
            result_var (tk.StringVar): The result StringVar
        """
        # Clear and reset the value StringVar
        value_var.set("0")
        # Clear the result
        result_var.set("0")
        
    def create_menu(self):
        """
        Create the application menu bar.
        """
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit, accelerator="Ctrl+Q")
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy Result", command=self.copy_result, accelerator="Ctrl+C")
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        
        # Create a submenu for themes
        theme_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="Themes", menu=theme_menu)
        
        # Add available themes
        available_themes = self.style.theme_names()
        for theme in available_themes:
            theme_menu.add_command(label=theme, command=lambda t=theme: self.change_theme(t))
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Help", command=self.show_help, accelerator="F1")
    
    def copy_result(self):
        """
        Copy the current result to the clipboard.
        """
        # Get the current tab
        current_tab = self.notebook.select()
        if current_tab:
            # Find the result label in the current tab
            tab_frame = self.notebook.nametowidget(current_tab)
            for child in tab_frame.winfo_children():
                if isinstance(child, ttk.LabelFrame) and child.cget("text") == "Result":
                    for result_label in child.winfo_children():
                        if isinstance(result_label, ttk.Label):
                            # Copy the result text to clipboard
                            self.root.clipboard_clear()
                            self.root.clipboard_append(result_label.cget("text"))
                            messagebox.showinfo("Copy", "Result copied to clipboard!")
                            return
        
        messagebox.showinfo("Copy", "No result to copy!")
    
    def change_theme(self, theme_name):
        """
        Change the application theme.
        
        Args:
            theme_name (str): The name of the theme to apply
        """
        try:
            self.style.theme_use(theme_name)
            messagebox.showinfo("Theme Changed", f"Theme changed to {theme_name}")
        except tk.TclError:
            messagebox.showerror("Theme Error", f"Could not apply theme: {theme_name}")
    
    def show_about(self):
        """
        Show the about dialog.
        """
        about_text = """Unit Converter

A flexible and extensible unit conversion application.

Features:
- Temperature, Length, Weight, and Volume conversions
- Support for delta/interval conversions
- Easy unit swapping
- Multiple themes

© 2025 Unit Converter Project
"""
        messagebox.showinfo("About Unit Converter", about_text)
    
    def show_help(self):
        """
        Show the help dialog.
        """
        help_text = """Unit Converter Help

How to use:
1. Select the converter tab (Temperature, Length, Weight, Volume)
2. Enter a value to convert
   - Conversion updates automatically as you type
3. Select the source unit from the "From" dropdown
   - Conversion updates automatically when changing units
4. Select the target unit from the "To" dropdown
   - Conversion updates automatically when changing units
5. For temperature, check "Delta/Interval Conversion" if needed
6. Use "Swap Units" to exchange the source and target units and automatically convert
7. Use "Clear" to reset the input and result

Keyboard shortcuts:
- Ctrl+Q: Exit the application
- Ctrl+C: Copy the current result to clipboard
- F1: Show this help dialog
- Alt+1 to Alt+4: Switch between converter tabs
- Enter: Perform conversion (when focus is in the value field)
- Ctrl+S: Swap units
"""
        messagebox.showinfo("Unit Converter Help", help_text)
        
    def setup_keyboard_shortcuts(self):
        """
        Set up keyboard shortcuts for common actions.
        """
        # Exit application (Ctrl+Q)
        self.root.bind("<Control-q>", lambda event: self.root.quit())
        
        # Show help (F1)
        self.root.bind("<F1>", lambda event: self.show_help())
        
        # Copy result (Ctrl+C) - handled by the copy_result method
        self.root.bind("<Control-c>", lambda event: self.copy_result())
        
        # Tab switching shortcuts (Alt+1 through Alt+4)
        # Use more explicit binding syntax and ensure each lambda gets its own tab_index
        self.root.bind("<Alt-Key-1>", lambda event, idx=0: self.notebook.select(idx))
        self.root.bind("<Alt-Key-2>", lambda event, idx=1: self.notebook.select(idx))
        self.root.bind("<Alt-Key-3>", lambda event, idx=2: self.notebook.select(idx))
        self.root.bind("<Alt-Key-4>", lambda event, idx=3: self.notebook.select(idx))
        
        # Add alternative bindings for platforms where Alt key might be intercepted
        self.root.bind("<Alt-1>", lambda event, idx=0: self.notebook.select(idx))
        self.root.bind("<Alt-2>", lambda event, idx=1: self.notebook.select(idx))
        self.root.bind("<Alt-3>", lambda event, idx=2: self.notebook.select(idx))
        self.root.bind("<Alt-4>", lambda event, idx=3: self.notebook.select(idx))
        
        # Add bindings to each tab's value entry field
        for i, tab_name in enumerate(self.converters.keys()):
            tab = self.notebook.winfo_children()[i]
            
            # Find the value entry and add Enter key binding
            for child in tab.winfo_children():
                if isinstance(child, ttk.LabelFrame) and child.cget("text") == "Input":
                    for widget in child.winfo_children():
                        if isinstance(widget, ttk.Entry):
                            # Bind Enter key to perform conversion
                            widget.bind("<Return>", lambda event, t=tab: self.handle_enter_key(t))
            
            # Find the swap button and add Ctrl+S binding
            for child in tab.winfo_children():
                if isinstance(child, ttk.Frame):  # Button frame
                    for button in child.winfo_children():
                        if isinstance(button, ttk.Button) and button.cget("text") == "Swap Units":
                            tab.bind("<Control-s>", lambda event, b=button: b.invoke())
                            
    def handle_enter_key(self, tab):
        """
        Handle Enter key press in a value entry field.
        
        Args:
            tab (ttk.Frame): The tab containing the value entry field
        """
        # Find the convert button and invoke it
        for child in tab.winfo_children():
            if isinstance(child, ttk.Frame):  # Button frame
                for button in child.winfo_children():
                    if isinstance(button, ttk.Button) and button.cget("text") == "Convert":
                        button.invoke()
                        return

def main():
    """
    Main function to run the GUI application.
    """
    converters = {
        name: obj
        for name, obj in vars(Converters).items()
        if isinstance(obj, Converters.Converter)
    }
    root = tk.Tk()
    app = ConverterGUI(root,converters)
    root.mainloop()

if __name__ == "__main__":
    main()