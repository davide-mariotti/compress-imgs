from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

def select_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    # Compress the image with selected quality
    compress_image(file_path, quality.get())

def select_folder():
    # Open file dialog to select a folder
    folder_path = filedialog.askdirectory()
    # Compress all images in the folder with selected quality
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith(".jpg"):
            compress_image(file_path, quality.get())
            
def compress_image(file_path, quality):
    if not os.path.exists("compressed"):
        os.makedirs("compressed")
    # Open the image
    image = Image.open(file_path)
    # Save the image with selected quality in "compressed" folder
    new_file_path = "compressed\\compressed_" + str(quality) + " " + os.path.basename(file_path)
    image.save(new_file_path, "JPEG", quality=quality)

# Create the main window
root = Tk()
root.geometry("400x220")
root.title("Mariotti Compressor V1.2")
root.config(bg="#d7d7d7")
root.resizable(False, False)

# Create a label to show the selected quality
quality_label = Label(root, text="Quality (1-100):", font="Arial 20")
quality_label.pack()

# Create a text area to enter the quality
quality = IntVar(value=85)
quality_entry = Entry(root, textvariable=quality, font="Arial 20", width=5)
quality_entry.pack()

# Create a button to select a single image
select_image_button = Button(root, text="Select Image", command=select_image, font="Arial 20")
select_image_button.pack()

# Create a button to select a folder
select_folder_button = Button(root, text="Select Folder", command=select_folder, font="Arial 20")
select_folder_button.pack()

footer_label = Label(root, text="\u00A9 by Davide Mariotti", font=("Arial", 12))
footer_label.pack()

# Start the main event loop
root.mainloop()

#per creare un .exe lanciare
#pyinstaller -w --onefile mariotti-compressor.py
