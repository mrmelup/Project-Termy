import platform
import tkinter as tk
from tkinter import messagebox

def warning_box(message, title="Warning"):
  if platform.system() == "Windows":
    import ctypes

    ctypes.windll.user32.MessageBoxW(0, message, title, 0x30 | 0x40000)
  else:
    # Cross-platform fallback for macOS and Linux
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    messagebox.showwarning(title, message)
    root.destroy()

warning_box("This is a warning message.", "Warning")