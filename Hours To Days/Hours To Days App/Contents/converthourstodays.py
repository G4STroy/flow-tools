import tkinter as tk
from timestamp_converter_app import TimestampConverterApp

def main():
    root = tk.Tk()
    template_path = "/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/HoursConvertTemplate.xlsx"
    instructions_path = "/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/AA Hours To Days Converter Instructions.docx"
    app = TimestampConverterApp(root, template_path, instructions_path)
    root.mainloop()

if __name__ == "__main__":
    main()
