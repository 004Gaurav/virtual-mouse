import math

def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def to_pixel_coords(landmarks, width, height, index):
    """Convert normalized landmark coordinates to pixel coordinates"""
    return int(landmarks[index].x * width), int(landmarks[index].y * height)

def get_finger_states(landmarks, tip_ids=[4, 8, 12, 16, 20]):
    """
    Return list of booleans indicating if each finger is up (True) or down (False).
    Compares tip y-coordinate with PIP joint y-coordinate.
    """
    fingers = []
    for tip in tip_ids:
        tip_y = landmarks[tip].y
        pip_y = landmarks[tip - 2].y
        fingers.append(tip_y < pip_y)
    return fingers
