import smtplib
from app import get_db

def send_email(subject, message, recipient):
    """Send an email with the specified subject and message to the given recipient."""
    sender_email = "your_email_address@example.com"
    sender_password = "your_email_password"

    # Create a secure connection to the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)

        # Construct the message to be sent
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(sender_email, recipient, email_message)

def notify_match(user_id, match_info):
    """Send a notification about a found match to a specific user."""
    subject = "Match found!"
    message = f"A match has been found for you: {match_info}"
    
    # Get the email and password of the user from the database
    db = get_db()
    user_data = db.get_user(user_id)
    recipient_email = user_data[1]
    recipient_password = user_data[2]
    
    # Send the email to the user's email address using their email and password
    send_email(subject, message, recipient_email)
    
    # Send a confirmation email to the match's email address
    match_email = match_info.split(':')[-1].strip()
    match_subject = "Match found!"
    match_message = f"A match has been found for you: {user_data[0]} ({user_data[1]})"
    send_email(match_subject, match_message, match_email)
