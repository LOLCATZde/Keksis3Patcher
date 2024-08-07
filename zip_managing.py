import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os
import sys

def select_zip_file():
    from main_window import zip_var
    from main import print_log
    print_log("Selecting zip file...")
    zip_path = filedialog.askopenfilename(filetypes=[("Keksis Patch files", "*.k3p"), ("Zip files", "*.zip"), ("All files", "*")])
    print_log(f"Selected zip file: {zip_path}")
    zip_var.set(zip_path)
    print_log("Zip file selection completed.")

def select_folder():
    from main_window import folder_var
    from main import print_log
    print_log("Selecting folder...")
    folder_path = filedialog.askdirectory()
    print_log(f"Selected folder: {folder_path}")
    folder_var.set(folder_path)
    print_log("Folder selection completed.")

def extract_and_delete():
    from main_window import entry_folder, entry_zip
    from main import print_log
    zip_path = entry_zip.get()
    folder_path = entry_folder.get()

    if not zip_path or not folder_path:
        messagebox.showerror("Error", "Please select both patch file and folder!")
        return

    try:
        if "-intentional-exception" in sys.argv:
            raise ValueError("Raised an intentional exception.")

        print_log(f"------------------------------------------------")
        print_log("Extracting and deleting...")

        print_log(f"Zip path: {zip_path}")
        print_log(f"Folder path: {folder_path}")

        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            print_log("Extracting zip file...")
            zip_file.extractall(folder_path)
            print_log("Zip file extraction completed.")

        for root, dirs, files in os.walk(folder_path):
            print_log(f"Checking folder: {root}")
            for file_name in files:
                print_log(f"Checking file: {file_name}")
                if file_name.endswith('.2bdeleted'):
                    file_path = os.path.join(root, file_name)
                    try:
                        os.remove(file_path.replace('.2bdeleted', ''))
                        print_log(f"Deleted file: {file_path.replace('.2bdeleted', '')}")
                    except FileNotFoundError:
                        print_log(f"File not found: {file_path.replace('.2bdeleted', '')}")
                    os.remove(file_path)
                    print_log(f"Deleted file: {file_path}")
        print_log("Extraction and deletion completed.")
        messagebox.showinfo("Patch successful", "Successfully patched the modpack!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during patching. Please run the file with -debug argument and check the log file for more information.\n\nError message: {str(e)}")
