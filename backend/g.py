"""This module is responsible for handling the groq API requests."""
import os
from groq import Groq

os.environ['GROQ_API_KEY'] = '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'

def groq(input):
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the concept of Finances",
            }
        ],
        model="llama3-8b-8192",
    )


    return str(chat_completion.choices[0].message.content)
