from PIL import Image
import os

def resize_folder(folder, width):
    for name in os.listdir(folder):
        if name.lower().endswith(".jpg", ".jpeg", ".png"):
            path = os.path.join(folder, name)
            img = Image.open(path)
            ratio = width / img.width
            img.resize((width, int(img.height * ratio))).save(path)
            print("Resized:", name)

if __name__ == "__main__":
    resize_folder(input("Folder: "), int(input("Width: ")))