# python
import unittest
import tkinter as tk
from tkinter import ttk
from unittest.mock import patch
import gui

class MockConverter:
    def __init__(self):
        # unidades de exemplo
        self.units = {"A": 1, "B": 2}
    def convert(self, value, from_unit, to_unit, delta):
        # comportamento simples para testes
        if from_unit == to_unit:
            return float(value)
        if from_unit == "A" and to_unit == "B":
            return float(value) * 10.0
        raise ValueError("Invalid units")

class TestConverterGUI(unittest.TestCase):
    def setUp(self):
        # tenta criar root Tkinter; se não houver Tcl/Tk disponível, pula os testes GUI
        self.root = None
        try:
            self.root = tk.Tk()
            self.root.withdraw()
        except tk.TclError as e:
            raise unittest.SkipTest(f"Tk not available: {e}")

        # Instancia GUI com o conversor mock
        self.mock_conv = MockConverter()
        self.gui = gui.ConverterGUI(self.root, {"Mock": self.mock_conv})

    def tearDown(self):
        if self.root:
            try:
                self.root.update_idletasks()
                self.root.destroy()
            except Exception:
                pass

    def test_convert_success(self):
        result_var = tk.StringVar(self.root)
        # 2 A -> B => 20.000000
        self.gui.convert(self.mock_conv, "2", "A", "B", False, result_var)
        self.assertEqual(result_var.get(), "2 A = 20.000000 B")

    def test_convert_invalid_number_shows_error(self):
        result_var = tk.StringVar(self.root)
        with patch("gui.messagebox.showerror") as mock_err:
            self.gui.convert(self.mock_conv, "abc", "A", "B", False, result_var)
            mock_err.assert_called_with("Invalid Input", "Please enter a valid number.")

    def test_convert_empty_input_shows_error(self):
        result_var = tk.StringVar(self.root)
        with patch("gui.messagebox.showerror") as mock_err:
            self.gui.convert(self.mock_conv, "   ", "A", "B", False, result_var)
            mock_err.assert_called_with("Invalid Input", "Please enter a value to convert.")

    def test_same_unit_formatting_scientific(self):
        result_var = tk.StringVar(self.root)
        # valor pequeno que deve aparecer em notação científica
        self.gui.convert(self.mock_conv, "0.0005", "A", "A", False, result_var)
        self.assertEqual(result_var.get(), "0.0005 A = 5.000000e-04 A")

    def test_swap_units_calls_convert(self):
        # prepara StringVars como na GUI
        from_var = tk.StringVar(self.root)
        to_var = tk.StringVar(self.root)
        from_var.set("A")
        to_var.set("B")
        orig_from = from_var.get()
        orig_to = to_var.get()
        with patch.object(self.gui, "convert") as mock_convert:
            self.gui.swap_units(self.mock_conv, "1", from_var, to_var, False, tk.StringVar(self.root))
            # após swap, convert deve ser chamado com unidades trocadas
            mock_convert.assert_called()
            called_args = mock_convert.call_args[0]
            # garantir que as unidades passadas para convert são as invertidas em relação ao original
            self.assertEqual(called_args[2], orig_to)
            self.assertEqual(called_args[3], orig_from)

    def test_clear_resets_values(self):
        # prepara valores
        value_var = tk.StringVar(self.root)
        result_var = tk.StringVar(self.root)
        value_var.set("123")
        result_var.set("abc")
        # value_entry não é usado internamente além de ser reset por StringVar, passa None
        self.gui.clear(None, value_var, result_var)
        self.assertEqual(value_var.get(), "0")
        self.assertEqual(result_var.get(), "0")

    def test_copy_result_copies_label_text_to_clipboard(self):
        # encontra o label de resultado no tab atual e configura texto direto
        current_tab = self.gui.notebook.select()
        tab_frame = self.gui.notebook.nametowidget(current_tab)
        target_text = "1 A = 10 B"
        # localiza Label dentro do LabelFrame "Result" e seta text explicitamente
        for child in tab_frame.winfo_children():
            if isinstance(child, ttk.LabelFrame) and child.cget("text") == "Result":
                for lbl in child.winfo_children():
                    if isinstance(lbl, ttk.Label):
                        # atualiza texto direto e também a textvariable se existir
                        lbl.config(text=target_text)
                        varname = lbl.cget("textvariable")
                        if varname:
                            try:
                                self.root.setvar(varname, target_text)
                            except Exception:
                                pass
                        break
                break

        with patch("gui.messagebox.showinfo") as mock_info:
            self.gui.copy_result()
            # clipboard_get deve retornar o texto copiado
            clip = self.root.clipboard_get()
            self.assertEqual(clip, target_text)
            mock_info.assert_called_with("Copy", "Result copied to clipboard!")

    def test_change_theme_invalid_shows_error(self):
        # força theme_use a levantar TclError para simular tema inválido
        with patch.object(self.gui.style, "theme_use", side_effect=tk.TclError()), \
             patch("gui.messagebox.showerror") as mock_err:
            self.gui.change_theme("invalid_theme")
            mock_err.assert_called_with("Theme Error", "Could not apply theme: invalid_theme")

if __name__ == "__main__":
    unittest.main()
