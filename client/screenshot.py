from PIL import ImageGrab
import datetime
import os

def take_screenshot():
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshots/{time}.png")

if __name__ == "__main__":
    os.makedirs("screenshots", exist_ok=True)
    take_screenshot()