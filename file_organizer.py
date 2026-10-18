import os, shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Docs": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
}

def organize(folder):
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            ext = os.path.splitext(name)[1].lower()
            for cat, exts in CATEGORIES.items():
                if ext in exts:
                    dest = os.path.join(folder, cat)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(path, os.path.join(dest, name))
                    break

if __name__ == "__main__":
    organize(input("Folder to organize: "))

