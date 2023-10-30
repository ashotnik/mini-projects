#!/usr/bin/python3
"""Imports"""
import subprocess
try:
    import smtplib
except ImportError:
    print("smtplib library not found. Installing...")
    subprocess.check_call(["pip", "install", "smtplib"])
    import smtplib   
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SENDER_EMAIL = "sendmail071@gmail.com"
RECEIVER_EMAIL = "tigran.barsegyan@gmail.com"
SENDER_PASSWORD = "pvyh cjsc eskb wgar"  # This should be a valid password for the sender's email account
SUBJECT = input("Enter subject of the Email: ")  # Prompt user for email subject
MESSAGE = input("Enter the text for Email: ")  # Prompt user for email message

# Create a function to send an email
def send_email(sender_email, receiver_email, password, subject, message):
    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Connect to Gmail's SMTP server using SSL on port 465
        server.login(sender_email, password)  # Log in to the sender's email account

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
        print("Email sent successfully!")

    except smtplib.SMTPException as error:
        print(f"SMTP Exception: {str(error)}")
    finally:
        server.quit()  # Quit the server

# Call the send_email function to send the email
send_email(SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD, SUBJECT, MESSAGE)
