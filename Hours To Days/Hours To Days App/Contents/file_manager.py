from tkinter import filedialog

class FileManager:
    @staticmethod
    def save_file_dialog(title, default_extension, initial_file):
        return filedialog.asksaveasfilename(title=title, defaultextension=default_extension, initialfile=initial_file)

    @staticmethod
    def open_file_dialog(title, file_types):
        return filedialog.askopenfilename(title=title, filetypes=file_types)
