import tkinter as tk
from tkinter import ttk
from main import resource_path, GuideWindow
from zip_managing import select_folder, select_zip_file, extract_and_delete
import tkinterDnD
import os

root = tkinterDnD.Tk()
root.title("Keksis 3 Patcher")
root.geometry("400x450")
root.resizable(False, False)
root.iconbitmap(resource_path('assets/icon.ico'))

zip_var = tk.StringVar()
zip_var.set('')
folder_var = tk.StringVar()
folder_var.set('')

def drop(pos):
    def inner(event):
        file_path = event.data
        if pos == 0:
            if file_path.lower().endswith(('.k3p', '.zip')):
                zip_var.set(file_path)
        elif pos == 1:
            if os.path.isdir(file_path):
                folder_var.set(file_path)
    return inner

def open_guide():
    button_extra["state"] = "disabled"
    GuideWindow(root)

logo = tk.PhotoImage(file=resource_path("assets/logo.png"))
logo_label = tk.Label(root, image=logo)
logo_label.pack()

label_zip = tk.Label(root, text="Patch File (.k3p, .zip):")
label_zip.pack()
entry_zip = ttk.Entry(root, ondrop=drop(0), textvariable=zip_var)
entry_zip.pack()
button_zip = ttk.Button(root, text="Select", command=select_zip_file, ondrop=drop(0))
button_zip.pack(pady=10)

label_folder = tk.Label(root, text="Pack Instance Folder:")
label_folder.pack()
entry_folder = ttk.Entry(root, ondrop=drop(1), textvariable=folder_var)
entry_folder.pack()
widget_folder_buttons=ttk.Label(root)
widget_folder_buttons.pack(pady=10)
button_folder = ttk.Button(widget_folder_buttons, text="Select", command=select_folder, ondrop=drop(1))
button_folder.pack(side="left")
button_extra = ttk.Button(widget_folder_buttons, text="?", command=open_guide, width=3)
button_extra.pack(side="right")

button_extract_and_delete = ttk.Button(root, text="Patch!", command=extract_and_delete)
button_extract_and_delete.pack(pady=25)

label_copyright = tk.Label(root, text="Copyright (c) 2024 LOLCATZ Digital. All rights reserved.", fg='#919191')
label_copyright.pack()

root.mainloop()