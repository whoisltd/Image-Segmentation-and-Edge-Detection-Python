from tkinter import Frame, Button, LEFT, filedialog
import cv2
import numpy as np
# from segmentation

class ToolBar(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.edited_image = None
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
        self.edge_detect_button.bind("<ButtonRelease>", self.edge_detect_button_released)
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
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
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
    
    def segmentation_button_released(self, event):
        # if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
        #     if self.master.is_image_selected:
                pixel_values = self.master.processed_image.reshape((-1, 3))
                pixel_values = np.float32(pixel_values)
                #define stopping criteria
                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 100, 0.2)
                #number of clusters (K)
                k = 3
                _, labels, (centers) = cv2.kmeans(pixel_values, k , None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                #convert back to 8 bit values
                centers = np.uint8(centers)
                #flatten the labels array
                labels = labels.flatten()
                #convert all pixels to the color of the centroids
                segmented_image = centers[labels.flatten()]
                #reshape back to the original image dimension
                segmented_image = segmented_image.reshape(self.master.processed_image.shape)
                self.master.processed_image = segmented_image
                #show the image
                self.master.image_viewer.show_image()
    
    def edge_detect_button_released(self, event):
        # if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
        #     if self.master.is_image_selected:
                #Detect edge
                edged = cv2.Canny(self.master.processed_image, 150, 200)
                #find contours
                contours, hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                #draw Contours
                cv2.drawContours(self.master.processed_image,contours,-1,(0,255,0),3)
                self.master.image_viewer.show_image()

    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()

