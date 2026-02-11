import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

sender_email=os.getenv("SENDER_EMAIL")
app_password=os.getenv("APP_PASSWORD")


def send_email(receiver_email: str, subject: str, content: str) -> str:
    """Send an email to the given receiver with the given subject and content."""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    return f"Email sent successfully to {receiver_email}"


if __name__ == "__main__":
    from secrets import receiver_email
    print(send_email(receiver_email, "Hello from Python 🐍", "This email was sent using Python!"))