from twilio_api import send_sms
from openai_api import gpt_response
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/sms", methods=["POST", "GET"])

def handle_sms():
#user message (will be changed to receive from message)
    #user_message = request.values.get('Body', None)
    user_message = request.form["Body"]

    resp = MessagingResponse()
#give message to gpt model
    function_response = gpt_response(user_message)

#send the message (Can now use TwiML)
    #send_sms(function_response)
    resp.message(function_response)
    return str(resp)

if __name__ == "__main__":
    app.run(port = 5001, debug=True)
