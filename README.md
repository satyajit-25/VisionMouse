# AI Computer Vision Toolkit (Virtual Mouse & Hand Gesture Detection)

## 🌟 Project Overview

This project presents an **AI Computer Vision Toolkit**, a Python application that leverages computer vision to provide innovative ways of interacting with your computer. It offers two primary functionalities: an AI Virtual Mouse for hands-free cursor control and a Hand Gesture Detection module that recognizes various predefined hand poses.

The goal of this project is to explore and implement natural, touchless human-computer interaction methods using real-time hand tracking.

## ✨ Features

### 🖱️ AI Virtual Mouse
* **Cursor Control:** Move your mouse cursor by simply moving your index finger.
* **Left Click:** Perform a left click by bringing your index finger and thumb close together.
* **Right Click:** Perform a right click by bringing your middle finger and thumb close together.
* **Dragging:** Click and hold objects by closing your index and middle fingers (while your thumb is extended).
* **Scrolling:** Scroll up or down by closing your index and middle fingers and then moving your hand vertically while your thumb is closed.

### ✋ Hand Gesture Detection
* **Real-time Recognition:** Detects and labels various hand gestures in real-time.
* **Supported Gestures:**
    * Open Palm
    * Victory (Peace sign)
    * One Finger
    * Three Fingers
    * Fist
    * Thumbs Up
    * Gun
    * Spider-Man
    * Rock
    * Call
    * Noice
    * Unknown (for unrecognized gestures)

## 🚀 Technologies Used

* **Python:** The core programming language for the application.
* **OpenCV:** Open Source Computer Vision Library, used for real-time video capture and image processing.
* **MediaPipe:** A framework used for high-fidelity hand tracking and landmark detection.
* **PyAutoGUI:** Used for programmatically controlling the mouse (moving, clicking, scrolling).
* **Tkinter & Ttkbootstrap:** Used for creating the graphical user interface (GUI) of the control panel.

## ⚙️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.x (Recommended: 3.8+)
* A webcam

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/AI-Virtual-Mouse-Gesture-Detection.git](https://github.com/your-username/AI-Virtual-Mouse-Gesture-Detection.git)
    cd AI-Virtual-Mouse-Gesture-Detection
    ```
    *(Replace `your-username` and `AI-Virtual-Mouse-Gesture-Detection` with your actual GitHub username and repository name.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    ```
    * **On Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Install Dependencies:**
    Install all required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you haven't created `requirements.txt` yet, run `pip freeze > requirements.txt` after installing `opencv-python`, `mediapipe`, `pyautogui`, and `ttkbootstrap`.)*
    *(Manual install if no `requirements.txt` yet: `pip install opencv-python mediapipe pyautogui ttkbootstrap`)*

## 🏃 How to Run

1.  **Activate your virtual environment** (if you created one, as shown in the installation steps).
2.  **Run the main application:**
    ```bash
    python main_app.py
    ```
3.  A control panel window will appear. From there, you can choose to launch either "Virtual Mouse" or "Gesture Detection."

## 🎬 Demo Video

Watch a short demonstration of the AI Computer Vision Toolkit in action:

[https://www.linkedin.com/feed/update/urn:li:activity:7352624575869857792/]


## 📸 Screenshots

![AI Control Panel](https://github.com/satyajit-25/VisionMouse/blob/main/Result/Screenshot%202025-07-10%20174300.png)
*Control Panel*

![Virtual Mouse in Action](https://github.com/satyajit-25/VisionMouse/blob/main/Result/Screenshot%202025-07-10%20174444.png)
*AI Virtual Mouse in action, showing drag control.*

![Gesture Detection](https://github.com/satyajit-25/VisionMouse/blob/main/Result/Screenshot%202025-07-10%20174659.png)
*Hand Gesture Detection recognizing a "Victory" sign.*

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
