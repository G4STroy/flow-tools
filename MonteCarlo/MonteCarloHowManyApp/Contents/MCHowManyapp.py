import shutil
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from monte_carlo_ui import MonteCarloUI
from monte_carlo_file_manager import MonteCarloFileManager
from monte_carlo_template_processor import MonteCarloTemplateProcessor

class MonteCarloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monte Carlo How Many")

        self.ui = MonteCarloUI(self.root)
        self.file_manager = MonteCarloFileManager()

        # Pass the file_manager instance to MonteCarloTemplateProcessor
        self.template_processor = MonteCarloTemplateProcessor(self.file_manager)

        self.setup_ui()

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
            # Use file_manager's method to get the resource path
            resource_file = self.file_manager.get_resource_path('Resources/MonteCarloHowMany.xlsx')
            shutil.copy(resource_file, destination_path)
            messagebox.showinfo("Success", "Template downloaded successfully.")

    def upload_template(self):
        file_path = self.file_manager.select_template_file(self.root)
        if file_path:
            # Directly process the template file without adjusting its path
            self.template_processor.process_template(file_path)

    def download_instructions(self):
        destination_path = self.file_manager.select_destination_directory(self.root)
        if destination_path:
            # Use file_manager's method to get the resource path
            resource_file = self.file_manager.get_resource_path('Resources/MonteCarloHowManyUserGuide.docx')
            shutil.copy(resource_file, destination_path)
            messagebox.showinfo("Success", "Instructions downloaded successfully.")

def main():
    root = tk.Tk()
    app = MonteCarloApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
