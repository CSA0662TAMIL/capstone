# capstone

# License Plate Detection and Notification System

This Python application utilizes OpenCV for real-time license plate detection from video streams, extracts the license plate text using Tesseract-OCR, and then sends an email notification with the detected license plate text and an image of the license plate. This guide will walk you through the setup and execution process of the script.

## Prerequisites

- Python 3.x installed on your machine.
- OpenCV, Numpy, imutils, pytesseract, and smtplib libraries installed.
- Tesseract-OCR installed on your machine.
- A working email account for sending notifications.

## Installation

1. **Install Python Packages**: Ensure you have Python 3.x installed. Install the required Python libraries using pip:

    ```bash
    pip install numpy opencv-python imutils pytesseract
    ```

2. **Install Tesseract-OCR**:
    - **Windows**: Download the installer from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions. Note the installation path.
    - **Linux**: Install Tesseract using your distribution's package manager, for example:

        ```bash
        sudo apt update
        sudo apt install tesseract-ocr
        ```

3. **Configure Your Email Account**:
    - The script uses Gmail's SMTP server to send emails. You may need to enable "Less secure app access" or set up an "App Password" if you have two-factor authentication enabled on your Google account.

## Configuration

Before running the script, make a few necessary adjustments to match your setup:

- **Tesseract Path**: Replace the `tesseract_cmd` path with the path where Tesseract-OCR is installed on your machine.
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
    ```
- **Email Details**: Modify the `email_sender`, `email_receiver`, and `email_password` variables with your email details. If you use two-factor authentication, you should generate an app password.
    ```python
    email_sender = 'your_email@gmail.com'
    email_receiver = 'receiver_email@gmail.com'
    email_password = 'your_email_password_or_app_password'
    ```

## Running the Script

- Open a terminal or command prompt.
- Navigate to the directory containing the script.
- Run the script with Python:
    ```bash
    python script_name.py
    ```
- The application will open a window displaying the video feed from your default webcam.
- Point the camera at a license plate, and the system will attempt to detect and recognize the plate number.
- Upon successful detection, the application will draw a green bounding box around the detected license plate, display the recognized text on the video feed, and send an email with the license plate image and detected text.
- Press 'q' to quit the application.

## Note

- The accuracy of license plate detection and text recognition may vary depending on the quality of the video feed, lighting conditions, and the angle of the license plate in view.
- The script is configured to use Gmail's SMTP server for sending emails. If you use another email provider, you'll need to adjust the SMTP server settings accordingly.
- Ensure you comply with privacy laws and regulations in your jurisdiction when using this script.

This application is a basic demonstration of integrating various technologies for license plate detection and can be expanded or modified for more complex scenarios or other types of object detection and recognition tasks.
