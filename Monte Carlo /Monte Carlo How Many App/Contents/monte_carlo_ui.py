# monte_carlo_ui.py
import tkinter as tk

class MonteCarloUI:
    def __init__(self, root):
        self.root = root

    def create_button_frame(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill='x', expand=False)
        return button_frame

    def load_buttons(self, button_frame, actions):
        for text, command in actions.items():
            button = tk.Button(button_frame, text=text, command=command)
            button.pack(side=tk.LEFT, padx=5, pady=5)
