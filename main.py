from twilio_api import send_sms
from openai_api import gpt_response

#user message (will be changed to recieve from message)
user_message = "Explain the use of an ephemeral port."

#give message to gpt model
function_response = gpt_response(user_message)

#send the message
send_sms(function_response)
