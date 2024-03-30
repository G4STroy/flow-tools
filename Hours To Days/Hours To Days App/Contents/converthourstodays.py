import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

class TimestampConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hours To Days Converter")  # Updated app title here

        # Define the paths for the template and output files
        self.template_path = "/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/HoursConvertTemplate.xlsx"
        self.instructions_path = "/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/AA Hours To Days Converter Instructions.docx"

        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        # Create a frame for the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill='x', expand=True)

        # Add buttons for the various functionalities
        tk.Button(button_frame, text="Download Template", command=self.download_template).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Upload Updated Template", command=self.upload_and_process_template).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Download Instructions", command=self.download_instructions).pack(side=tk.LEFT, padx=5, pady=5)

    def download_template(self):
        """Allow the user to download the Excel template."""
        destination_path = filedialog.asksaveasfilename(title="Save Template As", defaultextension=".xlsx", initialfile="HoursConvertTemplate.xlsx")
        if destination_path:
            try:
                shutil.copy(self.template_path, destination_path)
                messagebox.showinfo("Success", "Template downloaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download the template: {e}")

    def upload_and_process_template(self):
        """Upload the updated template and process it."""
        file_path = filedialog.askopenfilename(title="Select Updated Template File", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            output_path = filedialog.asksaveasfilename(title="Save Converted File As", defaultextension=".xlsx", initialfile="ConvertedHours.xlsx")
            if output_path:  # Proceed only if the user selects a save location
                self.convert_timestamps(file_path, output_path)
            else:
                messagebox.showwarning("Warning", "You didn't select a location to save the converted file. Operation cancelled.")

    def download_instructions(self):
        """Allow the user to download the instructions document."""
        destination_path = filedialog.asksaveasfilename(title="Save Instructions As", defaultextension=".docx", initialfile="AA Hours To Days Converter Instructions.docx")
        if destination_path:
            try:
                shutil.copy(self.instructions_path, destination_path)
                messagebox.showinfo("Success", "Instructions downloaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download the instructions: {e}")

    def convert_timestamps(self, excel_path, output_path):
        """Convert timestamps in the Excel file."""
        try:
            df = pd.read_excel(excel_path)
            base_date = datetime(2010, 1, 1)
            timestamp_columns = df.columns[2:]
            earliest_time = df[timestamp_columns].apply(pd.to_datetime, errors='coerce').min().min()

            def hours_to_days(timestamp, earliest_time, base_date):
                if pd.isnull(timestamp):
                    return timestamp
                hour_difference = int((timestamp - earliest_time).total_seconds() / 3600)
                return base_date + timedelta(days=hour_difference)

            for col in timestamp_columns:
                df[col] = df[col].apply(pd.to_datetime, errors='coerce')
                df[col] = df[col].apply(lambda x: hours_to_days(x, earliest_time, base_date))

            df.to_excel(output_path, index=False)
            messagebox.showinfo("Success", f"The file has been processed and saved as: {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the file: {e}")

def main():
    root = tk.Tk()
    app = TimestampConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
