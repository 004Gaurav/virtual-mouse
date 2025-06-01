import time
import pyautogui
import subprocess
from utils import distance, to_pixel_coords

class GestureController:
    def __init__(self, screen_width, screen_height):
        self.screen_w = screen_width
        self.screen_h = screen_height
        self.prev_x, self.prev_y = 0, 0
        self.smoothening = 7
        self.gesture_enabled = True
        self.last_click_time = 0
        self.last_launch_time = 0

    def toggle_gesture(self):
        self.gesture_enabled = not self.gesture_enabled
        return self.gesture_enabled

    def move_mouse(self, index_x, index_y, frame_w, frame_h):
        # Map webcam coords to screen coords and smooth movement
        screen_x = self.screen_w / frame_w * index_x
        screen_y = self.screen_h / frame_h * index_y
        curr_x = self.prev_x + (screen_x - self.prev_x) / self.smoothening
        curr_y = self.prev_y + (screen_y - self.prev_y) / self.smoothening
        pyautogui.moveTo(curr_x, curr_y)
        self.prev_x, self.prev_y = curr_x, curr_y

    def handle_gestures(self, landmarks, frame_w, frame_h):
        now = time.time()

        # Get pixel coords of key fingertips
        thumb = to_pixel_coords(landmarks, frame_w, frame_h, 4)
        index = to_pixel_coords(landmarks, frame_w, frame_h, 8)
        middle = to_pixel_coords(landmarks, frame_w, frame_h, 12)
        ring = to_pixel_coords(landmarks, frame_w, frame_h, 16)
        pinky = to_pixel_coords(landmarks, frame_w, frame_h, 20)

        # Left click: Thumb + Index
        if distance(thumb, index) < 40 and now - self.last_click_time > 1:
            pyautogui.click()
            self.last_click_time = now

        # Right click: Thumb + Middle
        elif distance(thumb, middle) < 40 and now - self.last_click_time > 1:
            pyautogui.click(button='right')
            self.last_click_time = now

        # Drag: Index + Middle close together
        if distance(index, middle) < 50:
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()

        # Open Calculator: Thumb + Ring
        if distance(thumb, ring) < 40 and now - self.last_launch_time > 2:
            subprocess.Popen("calc")
            self.last_launch_time = now

        # Open Notepad: Thumb + Pinky
        if distance(thumb, pinky) < 40 and now - self.last_launch_time > 2:
            subprocess.Popen("notepad")
            self.last_launch_time = now
