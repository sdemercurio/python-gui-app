import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500, bg="#8960d8")
canvas.pack()

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#8960d8")
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#8960d8")
runApps.pack()

root.mainloop()