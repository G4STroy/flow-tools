import os
import shutil
import sys
from tkinter import filedialog

class MonteCarloFileManager:
    def __init__(self):
        # Initialization remains simplified
        pass

    def get_resource_path(self, relative_path):
        """Resolve the absolute path to a resource in a way that works both for development and when bundled by PyInstaller."""
        # Dynamically adjust the base path whether the app is frozen (packaged by PyInstaller) or in development
        if getattr(sys, 'frozen', False):
            # If the application is running in a bundle, use the _MEIPASS directory
            base_path = sys._MEIPASS
        else:
            # Development environment: Adjust based on your project's structure
            # This assumes the script is at the root of the project, adjust the path traversal as necessary
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to the resource
        full_path = os.path.join(base_path, relative_path)
        print(f"Resource path resolved to: {full_path}")  # Debugging: Print the resolved path
        return full_path

    def select_destination_directory(self, root):
        """Ask the user to select a destination directory."""
        destination_path = filedialog.askdirectory(title="Select Destination Directory")
        return destination_path

    def download_template(self, destination_path):
        """Download the template file to a user-selected destination."""
        template_file_path = self.get_resource_path('Resources/MonteCarloHowMany.xlsx')
        shutil.copy(template_file_path, os.path.join(destination_path, os.path.basename(template_file_path)))

    def select_template_file(self, root):
        """Allow the user to select a template file."""
        file_path = filedialog.askopenfilename(title="Select Template File", filetypes=[("Excel files", "*.xlsx")])
        return file_path

    def download_instructions(self, destination_path):
        """Download the instructions file to a user-selected destination."""
        instructions_file_path = self.get_resource_path('Resources/MonteCarloHowManyUserGuide.docx')
        shutil.copy(instructions_file_path, os.path.join(destination_path, os.path.basename(instructions_file_path)))
