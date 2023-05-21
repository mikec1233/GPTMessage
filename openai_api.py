import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-6jWqtZzRBRGyorjBskMsFAjj"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the use of an ephemeral port."},
    ]
)

print(response['choices'][0]['message']['content'])
