import os
import shutil
import sys
from tkinter import filedialog

class MonteCarloFileManager:
    def __init__(self):
        # The path is relative to the root of the PyInstaller _MEIPASS directory or the current file
        resources_relative_path = os.path.join('MonteCarlo', 'MonteCarloHowManyApp', 'Contents', 'Resources')

        if getattr(sys, 'frozen', False):
            # Running in a PyInstaller bundle
            base_path = sys._MEIPASS
        else:
            # Running in a normal Python environment
            # Assumes the script is alongside the 'Resources' directory
            base_path = os.path.dirname(os.path.abspath(__file__))

        self.resources_dir = os.path.join(base_path, resources_relative_path)

    def select_destination_directory(self, root):
        destination_path = filedialog.askdirectory(title="Select Destination Directory")
        return destination_path

    def download_template(self, destination_path):
        template_file_path = os.path.join(self.resources_dir, 'MonteCarloHowMany.xlsx')
        shutil.copy(template_file_path, os.path.join(destination_path, os.path.basename(template_file_path)))

    def select_template_file(self, root):
        file_path = filedialog.askopenfilename(title="Select Template File", filetypes=[("Excel files", "*.xlsx")])
        return file_path

    def download_instructions(self, destination_path):
        instructions_file_path = os.path.join(self.resources_dir, 'MonteCarloHowManyUserGuide.docx')
        shutil.copy(instructions_file_path, os.path.join(destination_path, os.path.basename(instructions_file_path)))