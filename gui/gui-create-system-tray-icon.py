import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import threading
import time
import os
import sys
import subprocess

# Function to create an image for the icon
def create_image():
    # Generate an image and draw a pattern
    image = Image.new('RGB', (64, 64), 'blue')
    dc = ImageDraw.Draw(image)
    dc.rectangle((32, 32, 64, 64), fill='white')
    dc.rectangle((0, 0, 32, 32), fill='white')
    return image

# Function to quit the application
def quit_action(icon, item):
    icon.stop()
    # Perform any cleanup here
    global running
    running = False

# Function to reload the script
def reload_action(icon, item):
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Function to edit the script
def edit_action(icon, item):
    script_path = os.path.abspath(__file__)
    subprocess.Popen(['notepad', script_path])  # Change 'notepad' to your preferred editor if necessary

# Function to open the script location
def open_location_action(icon, item):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    subprocess.Popen(['explorer', script_dir])

# Example function to run your main task
def main_task():
    while running:
        print("Running...")
        time.sleep(1)

# Create a system tray icon
icon = pystray.Icon("test_icon")
icon.menu = pystray.Menu(
    item("Reload", reload_action),
    item("Edit Script", edit_action),
    item("Open Script Location", open_location_action),
    item("Quit", quit_action)
)

icon.icon = create_image()

# Running the main task in a separate thread
running = True
thread = threading.Thread(target=main_task)
thread.start()

# Run the system tray icon
icon.run()

# Wait for the main task to finish before exiting
thread.join()
