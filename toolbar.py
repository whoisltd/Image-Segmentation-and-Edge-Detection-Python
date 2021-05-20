from tkinter import Frame, Button, LEFT, filedialog
import cv2
import numpy as np

class ToolBar(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.new_button = Button(self, text="New")
        self.save_button = Button(self, text="Save")
        self.save_as_button = Button(self, text="Save as")
        self.segmentation_button = Button(self, text="Segmentation")
        self.edge_detect_button = Button(self, text="Edge detect")
        self.clear_button = Button(self, text="Clear")

        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.segmentation_button.bind("<ButtonRelease>", self.segmentation_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)

        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        self.segmentation_button.pack(side=LEFT)
        self.edge_detect_button.pack(side=LEFT)
        self.clear_button.pack()
    
    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.x1 = 1
                self.y1 = 1
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.zoom_image = self.master.processed_image
                self.routate_image = self.master.processed_image
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
    
    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                save_image = self.master.processed_image
                filename_extension = self.master.filename.split('.')[-1]
                filename = filedialog.askopenfilename()
                filename = filename + '.' + filename_extension
                cv2.imwrite(filename, save_image)
    
    def clear_button_released(self, event):
            if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
                if self.master.is_image_selected:
                    self.master.processed_image = self.master.original_image.copy()
                    self.master.image_viewer.show_image()

