import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from Converter_Logic.Converter import Converter


class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Converter")
        self.root.geometry("450x400")
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.custom_font = ("Roboto", 18)

        # configure input field
        self.input_label = ctk.CTkLabel(self.frame, text="Enter a number: NUMBERxBASE(e.g., 1C8x16):",
                                        font=self.custom_font)
        self.input_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.input_entry = ctk.CTkEntry(self.frame, font=self.custom_font, placeholder_text="Number")
        self.input_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # configure target base combobox
        self.target_base_label = ctk.CTkLabel(self.frame, text="Select target base:", font=self.custom_font)
        self.target_base_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.target_base_var = ctk.StringVar()
        self.target_base_combo = ctk.CTkComboBox(self.frame, variable=self.target_base_var,
                                                 values=[str(i) for i in range(2, 17)], font=self.custom_font)
        self.target_base_combo.grid(row=3, column=0, columnspan=3, padx=10, pady=10, )

        # configure "Convert" button
        self.convert_button = ctk.CTkButton(self.frame, text="Convert", command=self.convert, font=self.custom_font)
        self.convert_button.grid(row=4, column=0, columnspan=3, padx=10, pady=15, sticky="nsew")

        # configure output field
        self.output_label = ctk.CTkLabel(self.frame, text="Result:", font=self.custom_font)
        self.output_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.output_var = ctk.StringVar()
        self.output_entry = ctk.CTkEntry(self.frame, textvariable=self.output_var, state='readonly',
                                         font=self.custom_font, justify="center")
        self.output_entry.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Configure column and row weights for centering and resizing
        for i in range(3):
            self.frame.columnconfigure(i, weight=1)  # Center elements horizontally
        for i in range(7):
            self.frame.rowconfigure(i, weight=1)

    def convert(self):
        try:
            input_string = self.input_entry.get().strip()
            target_base = self.target_base_var.get()

            if (input_string.count('x') != 1 or len(input_string[(input_string.index('x') + 1):]) == 0
                    or len(input_string[:input_string.index('x')]) == 0):
                ConverterApp.show_warning_message("Please specify the source number and base. Format (NUMBERxBASE)")
                return
            source_base = int(input_string[(input_string.index('x') + 1):]);
            input_string = input_string[:-len("x" + str(source_base))]

            if not target_base:
                ConverterApp.show_warning_message("Please select a target base.")
                return
            target_base = int(target_base)

            status, result = Converter.convert(input_string, source_base, target_base)

            if status:
                self.output_var.set(result)
            else:
                self.output_var.set("Error")
                ConverterApp.show_error_message("Conversion error: " + result)
        except Exception as e:
            ConverterApp.show_error_message("An error occurred: " + str(e))

    @staticmethod
    def show_error_message(message):
        messagebox.showerror("Error", message)

    @staticmethod
    def show_warning_message(message):
        messagebox.showwarning("Warning", message);


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
app = ConverterApp(root)
root.mainloop()
