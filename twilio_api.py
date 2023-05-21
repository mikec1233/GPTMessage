import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Read more at http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_sms(message_body, from_number = os.getenv('TWILIO_NUM'), to_number = os.getenv('PERSONAL_NUM')):
    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )
    print(message.sid)
    return message.sid