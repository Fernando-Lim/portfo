import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

def send_email(data):
    try:
        # Fetch email configuration from environment variables
        mail_server = os.getenv('MAIL_SERVER')
        mail_port = int(os.getenv('MAIL_PORT', 25))
        mail_username = os.getenv('MAIL_USERNAME')
        mail_password = os.getenv('MAIL_PASSWORD')
        mail_use_tls = os.getenv('MAIL_USE_TLS') == 'True'
        mail_use_ssl = os.getenv('MAIL_USE_SSL') == 'True'
        mail_default_sender = os.getenv('MAIL_DEFAULT_SENDER')

        # Extract data from input
        recipient_email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]

        # Create email
        msg = MIMEMultipart()
        msg['From'] = mail_default_sender
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add the email body
        msg.attach(MIMEText(message, 'plain'))

        # Setup SMTP connection
        if mail_use_ssl:
            server = smtplib.SMTP_SSL(mail_server, mail_port)
        else:
            server = smtplib.SMTP(mail_server, mail_port)

        if mail_use_tls:
            server.starttls()

        # Login and send email
        server.login(mail_username, mail_password)
        server.sendmail(mail_default_sender, recipient_email, msg.as_string())
        server.quit()

        print(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")
