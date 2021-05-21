import tkinter as tk
from tkinter import ttk
from toolbar import ToolBar
from viewer import Viewer
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.filename = None
        self.origin_image = None
        self.processed_image = None
        
        self.title("Segmentation and Edge Detection")

        self.toolbar = ToolBar(master=self)
        separator = ttk.Separator(master=self)
        self.image_viewer = Viewer(master=self)

        self.toolbar.pack(pady=10)
        separator.pack(fill=tk.X, padx=20, pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)
