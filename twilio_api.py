import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Read more at http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+18667069264",
  to="+13367697741"
)
print(message.sid)