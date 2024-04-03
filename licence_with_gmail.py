import cv2
import numpy as np
import pytesseract
import imutils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

# Email configuration - replace with your details
email_sender = 'sender@gmail.com'
email_receiver = 'receiver@gmail.com'
email_password = 'email_app_password'

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    return edged

def detect_license_plate(image):
    contours = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if contours:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                return approx
    return None

def recognize_license_plate(image, contour):
    x, y, w, h = cv2.boundingRect(contour)
    license_plate_roi = image[y:y+h, x:x+w]
    license_plate_text = pytesseract.image_to_string(license_plate_roi, config='--psm 8 --oem 3')
    return license_plate_text.strip()

def send_email(image, license_plate_text):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = 'License Plate Detected'
    
    _, img_encoded = cv2.imencode('.png', image)
    image_msg = MIMEImage(img_encoded.tobytes(), name='license_plate.png')
    msg.attach(image_msg)
    
    body = f"Detected License Plate Text: {license_plate_text}"
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    processed_frame = preprocess(frame)
    contour = detect_license_plate(processed_frame)
    
    if contour is not None:
        license_plate_text = recognize_license_plate(frame, contour)
        if license_plate_text:
            print("License Plate Text:", license_plate_text)
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            cv2.putText(frame, license_plate_text, (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            send_email(frame, license_plate_text)
    
    cv2.imshow('License Plate Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
