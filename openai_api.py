import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-6jWqtZzRBRGyorjBskMsFAjj"
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_response(message_content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant working as a text message response bot. Your goal is to provide accurate information in a brief, punctual, and accurate way."},
            {"role": "user", "content": message_content},
        ]
    )

    return (response['choices'][0]['message']['content'])
