import tkinter as tk
from tkinter import filedialog, messagebox
from monte_carlo_ui import MonteCarloUI
from monte_carlo_file_manager import MonteCarloFileManager
from monte_carlo_template_processor import MonteCarloTemplateProcessor
import os

class MonteCarloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monte Carlo How Many")

        self.ui = MonteCarloUI(self.root)
        self._file_manager = None
        self._template_processor = None

        self.setup_ui()

    @property
    def file_manager(self):
        if self._file_manager is None:
            self._file_manager = MonteCarloFileManager(resources_dir=os.path.abspath('MonteCarlo/MonteCarloHowManyApp/Contents/Resources/'))
        return self._file_manager

    @property
    def template_processor(self):
        if self._template_processor is None:
            self._template_processor = MonteCarloTemplateProcessor(resources_dir=os.path.abspath('MonteCarlo/MonteCarloHowManyApp/Contents/Resources/'))
        return self._template_processor

    def setup_ui(self):
        button_frame = self.ui.create_button_frame()
        self.ui.load_buttons(button_frame, {
            "Download Template": self.download_template,
            "Upload Modified Template": self.upload_template,
            "Instructions": self.download_instructions
        })

    def download_template(self):
        destination_path = self.file_manager.select_destination_directory(self.root)
        if destination_path:
            try:
                self.file_manager.download_template(destination_path)
                messagebox.showinfo("Success", "Template downloaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download the template: {e}")

    def upload_template(self):
        file_path = self.file_manager.select_template_file(self.root)
        if file_path:
            self.template_processor.process_template(file_path)

    def download_instructions(self):
        destination_path = self.file_manager.select_destination_directory(self.root)
        if destination_path:
            try:
                self.file_manager.download_instructions(destination_path)
                messagebox.showinfo("Success", "Instructions downloaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download the instructions: {e}")

def main():
    root = tk.Tk()
    app = MonteCarloApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
