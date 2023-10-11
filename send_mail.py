#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "sendmail071@gmail.com"
receiver_email = "sendmail071@gmail.com"
sender_password = "pvyh cjsc eskb wgar"
subject = input("Enter subject of the Email: ")
message = input("Enter the text for Email: ")

# Create a function to send an email
def send_email(sender_email, receiver_email, password, subject, message):
    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    print(msg)
    msg.attach(MIMEText(message, 'plain'))
    print(msg)

    # Connect to the SMTP servver and send
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"SMTP Exception: {str(e)}")
    finally:
        server.quit()

send_email(sender_email, receiver_email, sender_password, subject, message)
