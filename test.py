# PYTHON FILE FOR TESTING

import ctypes

def show_error(title, message):
    # 0x10 displays the red "X" error icon; 0x40000 ensures it stays on top
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x30 | 0x40000)

show_error("Warning", "Stop doing that")
