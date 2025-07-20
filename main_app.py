import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *
import subprocess
import sys
import os
import threading

def run_script(script_name):
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
        python_cmd = sys._base_executable
    else:
        base_dir = os.path.dirname(__file__)
        python_cmd = sys.executable

    script_path = os.path.join(base_dir, script_name)

    if os.path.basename(script_path) == os.path.basename(sys.executable):
        messagebox.showerror("Error", "Recursion detected. Aborting.")
        return

    def launch():
        # Show "Getting ready..." message
        status_label.config(text="Getting ready...", bootstyle="warning")
        try:
            # Start the subprocess
            proc = subprocess.Popen(
                ["python", script_path],
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            # Wait a short moment to let the webcam window appear
            proc.poll()
            app.after(10000, lambda: status_label.config(text=""))  # Clear after 10 second
        except Exception as e:
            status_label.config(text="")
            messagebox.showerror("Error", str(e))

    threading.Thread(target=launch, daemon=True).start()

# GUI Setup
app = ttk.Window(themename="cyborg")
app.title("AI Vision Control Panel")
app.geometry("770x600")

ttk.Label(app, text="AI Computer Vision Toolkit", font=("Helvetica", 23), bootstyle="info").pack(pady=60)
ttk.Label(app, text="").pack(pady=5)  # Spacer
ttk.Button(app, text="🖱️ Virtual Mouse", width=30, bootstyle="success-outline",
           command=lambda: run_script("ai_virtual_mouse.py")).pack(pady=10)
ttk.Label(app, text="").pack(pady=5)  # Spacer
ttk.Button(app, text="✋ Gesture Detection", width=30, bootstyle="primary-outline",
           command=lambda: run_script("hand_gesture_detection.py")).pack(pady=10)

# Status label at the bottom center
status_label = ttk.Label(app, text="", font=("Helvetica", 10), anchor="center", bootstyle="warning")
status_label.pack(side="bottom", pady=20, fill="x")

app.mainloop()
