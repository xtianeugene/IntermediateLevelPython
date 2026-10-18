import tkinter as tk
from tkinter import messagebox

def start():
    seconds = int(entry.get()) * 60
    tick(seconds)

def tick(seconds):
    if seconds <= 0:
        messagebox.showinfo("Pomodoro", "Time's up!")
        return
    mins, secs = divmod(seconds, 60)
    label.config(text=f"{mins:02d}:{secs:02d}")
    root.after(1000, tick, seconds - 1)

root = tk.Tk()
root.title("Pomodoro")
label = tk.Label(root, font=("Arial", 30), text="25:00")
label.pack(padx=20, pady=10)
entry = tk.Entry(root)
entry.insert(0, "25")
entry.pack()
tk.Button(root, text="Start", command=start).pack(pady=10)
root.mainloop()