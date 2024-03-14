import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
root = tk.Tk()
root.title("Image Sketch Converter")
root.geometry("800x600")  # Thiết lập kích thước cửa sổ



# Global variable to store the file path
file_path = None

# Global variable to store the image label
image_label = None

# Function to convert the image
def convert_image():
    global file_path, image_label
    
    # Check if a file has been selected
    if file_path:
        # Clear the existing image label
        if image_label:
            image_label.grid_forget()

        print(file_path)
        print(os.path.basename(file_path))

        
        # Read the image
        image = cv2.imread(os.path.basename(file_path))
        print(image)
        
        # Convert color channels
        im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        # Invert grayscale
        inv_gray = 255 - gray
        
        # Apply Gaussian blur
        blur_img = cv2.GaussianBlur(inv_gray, (101, 101), 0)
        
        # Invert blurred image
        inv_blur = 255 - blur_img
        
        # Create sketch image
        sketch_img = cv2.divide(gray, inv_blur, scale=255.0)
        
        # Save the converted image
        save_path = os.path.basename(file_path) + '_sketch.png'
        cv2.imwrite(save_path, sketch_img)
        
        # Open the converted image using PIL
        converted_image = Image.open(save_path)
        converted_image.thumbnail((600,600))
        
        # Create PhotoImage object
        photo = ImageTk.PhotoImage(converted_image)
        
        # Create label to display the converted image
        image_label = tk.Label(root, image=photo)
        image_label.image = photo
        image_label.grid(row=1, column=0, columnspan=2)

# Function to open file dialog and select image
def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((600,600))
        img = ImageTk.PhotoImage(img)
        global image_label
        image_label = tk.Label(root, image=img)
        image_label.image = img
        image_label.grid(row=1, column=0, columnspan=2)
        print(file_path)

# Button to select image
browse_button = tk.Button(root, text="Browse Image", command=open_file)
browse_button.grid(row=0, column=0, pady=10)

# Button to convert image
convert_button = tk.Button(root, text="Convert", command=convert_image)
convert_button.grid(row=0, column=1, pady=10)

root.mainloop()
