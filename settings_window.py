import tkinter as tk
import settings

from tkinter import ttk
from algo_enum import AlgorithumEnum


class SettingsWindow:
    def __init__(self, width, heigth) -> None:
        self.width = width
        self.heigth = heigth
        self.win = self.win = tk.Tk()
        
        self.win.geometry(f"{self.width}x{self.heigth}")
        self.win.title("Settings window")
        
        text_var = tk.StringVar()
        self.algo_choice = ttk.Combobox(self.win, textvariable=text_var)
        self.algo_choice['values'] = [algo.value for algo in AlgorithumEnum]
        self.algo_choice['state'] = "readonly"
        self.algo_choice.pack(fill=tk.X, padx=5, pady=5)
        
        validate_button = ttk.Button(self.win, text="Validate", command=self.set_algo)
        validate_button.pack()
        
    def run(self) -> None:
        self.win.mainloop()
        
    def set_algo(self) -> None:
        settings.SELECTED_ALGO = AlgorithumEnum[self.algo_choice.get().upper()]