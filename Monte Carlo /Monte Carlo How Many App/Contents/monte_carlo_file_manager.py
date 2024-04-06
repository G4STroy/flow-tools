# monte_carlo_file_manager.py
import os
import shutil
from tkinter import filedialog

class MonteCarloFileManager:
    def __init__(self, resources_dir):
        self.resources_dir = resources_dir

    def select_destination_directory(self, root):
        destination_path = filedialog.askdirectory(title="Select Destination Directory")
        return destination_path

    def download_template(self, destination_path):
        template_file_path = os.path.join(self.resources_dir, 'Monte Carlo How Many.xlsx')
        shutil.copy(template_file_path, os.path.join(destination_path, os.path.basename(template_file_path)))

    def select_template_file(self, root):
        file_path = filedialog.askopenfilename(title="Select Template File", filetypes=[("Excel files", "*.xlsx")])
        return file_path

    def download_instructions(self, destination_path):
        instructions_file_path = os.path.join(self.resources_dir, 'Monte Carlo How Many User Guide.docx')
        shutil.copy(instructions_file_path, os.path.join(destination_path, os.path.basename(instructions_file_path)))
