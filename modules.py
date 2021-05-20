from tkinter import Toplevel, Button, RIGHT
import numpy as np
import cv2

class Modules(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.edited_image = None
        
    def segmentation(self):
        self.edited_image = cv2.