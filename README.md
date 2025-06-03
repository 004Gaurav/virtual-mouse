# Virtual Mouse using Hand Gestures

A Python-based virtual mouse that uses a webcam and hand gesture recognition to control your computer’s mouse cursor and perform mouse actions — no physical mouse needed!

---

## Features

- Move mouse cursor by tracking index finger
- Left click using thumb + index finger pinch
- Right click using thumb + middle finger pinch
- Drag and drop using index + middle finger pinch and hold
- Open Calculator app using thumb + ring finger pinch
- Open Notepad using thumb + pinky finger pinch
- Toggle gesture control ON/OFF with `g` key
- Visual overlay on webcam feed showing status and instructions

---

## Technologies Used

- Python 3.9+
- OpenCV for webcam video capture and drawing
- MediaPipe for real-time hand tracking and landmark detection
- PyAutoGUI for controlling mouse and launching apps
- Subprocess for system command execution

---

## 📁 Access All Demo Videos

👉 [Click here to browse the `assets/` folder](https://github.com/004Gaurav/virtual-mouse/tree/main/assets)  
(Contains all demo videos and images)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Gaurav004/virtual-mouse.git
   cd virtual-mouse

