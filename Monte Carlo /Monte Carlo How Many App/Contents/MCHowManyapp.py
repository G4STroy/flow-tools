import tkinter as tk
from tkinter import filedialog, messagebox
from monte_carlo_ui import MonteCarloUI
from monte_carlo_file_manager import MonteCarloFileManager
from monte_carlo_template_processor import MonteCarloTemplateProcessor

class MonteCarloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monte Carlo How Many")

        self.resources_dir = "/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources"  # Update this with your actual resources directory

        self.ui = MonteCarloUI(self.root)
        self.file_manager = MonteCarloFileManager(self.resources_dir)  # Pass resources_dir here
        self.template_processor = MonteCarloTemplateProcessor(self.resources_dir)

        self.setup_ui()

    def setup_ui(self):
        button_frame = self.ui.create_button_frame()
        self.ui.load_buttons(button_frame, {
            "Download Template": self.download_template,
            "Upload Modified Template": self.upload_template,
            "Instructions": self.download_instructions
        })

    def download_template(self):
        destination_path = self.file_manager.select_destination_directory(self.root)  # Pass root argument here
        if destination_path:
            try:
                self.file_manager.download_template(destination_path)
                messagebox.showinfo("Success", "Template downloaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download the template: {e}")


    def upload_template(self):
        file_path = self.file_manager.select_template_file(self.root)  # Pass root argument here
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


