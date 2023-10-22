
import tkinter as tk
from tkinter import ttk, messagebox
from Converter_Logic.Converter import Converter


class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Converter")
        self.root.geometry("500x350")

        self.custom_font = ("Helvetica", 12)
        self.custom_bg = "#f2f2f2"
        self.custom_fg = "white"
        self.custom_button_bg = "blue"

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), background=self.custom_button_bg, foreground="black")

        # configure input field
        self.input_label = ttk.Label(root, text="Enter a number (e.g., 1C8x16):", font=self.custom_font, background=self.custom_bg)
        self.input_label.pack(pady=10)
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(root, textvariable=self.input_var, font=self.custom_font)
        self.input_entry.pack(pady=10)

        # configure target base combobox
        self.target_base_label = ttk.Label(root, text="Select target base:", font=self.custom_font,
                                           background=self.custom_bg)
        self.target_base_label.pack(pady=10)
        self.target_base_var = tk.StringVar()
        self.target_base_combo = ttk.Combobox(root, textvariable=self.target_base_var,
                                              values=[str(i) for i in range(2, 17)], font=self.custom_font)
        self.target_base_combo.pack(pady=10)

        # configure "Convert" button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert,
                                         style="TButton")
        self.convert_button.pack(pady=10)

        # configure output field
        self.output_label = ttk.Label(root, text="Result:", font=self.custom_font, background=self.custom_bg)
        self.output_label.pack(pady=10)
        self.output_var = tk.StringVar()
        self.output_entry = ttk.Entry(root, textvariable=self.output_var, state='readonly', font=self.custom_font)
        self.output_entry.pack(pady=10)

    def convert(self):
        try:
            input_string = self.input_var.get().strip()
            target_base = self.target_base_var.get()

            if not target_base:
                self.show_warning_message("Please select a target base.")
                return
            target_base = int(target_base)

            if 'x' not in input_string or len(input_string[(input_string.index('x') + 1):]) == 0:
                self.show_warning_message("Please specify the source base.")
                return

            source_base = int(input_string[(input_string.index('x') + 1):]);
            input_string = input_string[:-len("x" + str(source_base))]

            status, result = Converter.convert(input_string, source_base, target_base)

            if status:
                self.output_var.set(result)
            else:
                self.output_var.set("Error")
                self.show_error_message("Conversion error: " + result)
        except Exception as e:
            self.show_error_message("An error occurred: " + str(e))

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

    def show_warning_message(self, message):
        messagebox.showwarning("Warning", message);


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
