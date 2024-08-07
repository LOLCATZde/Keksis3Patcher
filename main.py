import tkinter as tk
from tkinter import ttk
import os
import sys
import logging
import datetime
import main_window
from zip_managing import *
from tkinterdnd2 import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if "-debug" in sys.argv:
    logs_folder_path = resource_path('logs')
    if not os.path.exists(logs_folder_path):
        os.makedirs(logs_folder_path)

    log_filename = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.log')
    log_path = os.path.join(logs_folder_path, log_filename)
    log_path = os.path.join(resource_path('logs'), log_filename)
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Launch arguments: {sys.argv}")

def print_log(message):
    if "-debug" in sys.argv:
        logging.basicConfig(filename=resource_path('keksis_3_patcher.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(message)

class GuideWindow(tk.Toplevel):
    def guide_close(self):
        from main_window import button_extra
        button_extra["state"] = "enabled"
        self.destroy()
        
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Keksis 3 Patcher - Help")
        self.geometry("450x330")
        self.resizable(False, False)

        tab_control = ttk.Notebook(self)
        tab_control.pack(fill='both')

        default_tab = None

        for file_name in os.listdir(resource_path('guides')):
            if file_name.endswith(".txt"):
                with open(os.path.join(resource_path('guides'), file_name), "r") as file:
                    content = file.read().splitlines()
                    tab = tk.Frame(tab_control)
                    tab_control.add(tab, text=content[0])
                    widget_text=ttk.Label(tab)
                    widget_text.pack(pady=10, padx=30)
                    for line in content[1:]:
                        line_x = line.replace("\\u2191", "\u2191")
                        label = tk.Label(widget_text, text=line_x, wraplength=350, justify='left')
                        label.pack()
                    if file_name == "modrinth.txt":
                        default_tab = tab

        if default_tab is not None:
            tab_control.select(default_tab)
        else:
            tab_control.select(tab_control.winfo_children()[0])
        
        self.protocol("WM_DELETE_WINDOW", self.guide_close)
