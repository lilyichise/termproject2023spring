#####notification_utils.py file########
import requests

###ALTERNATIVE 1#########
# def send_email(subject, message, recipient):
#     """Send an email with the specified subject and message to the given recipient."""
#     mailgun_url = "https://api.mailgun.net/v3/yourdomain.com/messages"
#     mailgun_key = "fc0adb3dd0aecad7923c8eb7def29586-70c38fed-c5f58e82" 
#     sender_email = "Study Groups <studygroups@yourdomain.com>"
    
#     response = requests.post(
#         mailgun_url,
#         auth=("api", mailgun_key),
#         data={
#             "from": sender_email,
#             "to": recipient,
#             "subject": subject,
#             "text": message
#         }
#     )
    
#     if response.status_code != 200:
#         raise Exception(f"Failed to send email: {response.text}")

#######ALTERNATIVE 2##########  
def send_email(subject, message, recipient):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox4db1e63519994e0f9a006f7a944e8688.mailgun.org/messages",
		auth=("api", "fc0adb3dd0aecad7923c8eb7def29586-70c38fed-c5f58e82"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox4db1e63519994e0f9a006f7a944e8688.mailgun.org>",
			"to": recipient,
			"subject": subject,
			"text": message})


def notify_match(chat_id, match_info):
    """Send a notification about a found match to a specific user."""
    subject = "Match found!"
    message = f"A match has been found for you: {match_info}"
    recipient = "recipient_email_address@example.com"
    send_email(subject, message, recipient)

#test funciton
send_email("test","test", "matthewsyrigos@gmail.com")