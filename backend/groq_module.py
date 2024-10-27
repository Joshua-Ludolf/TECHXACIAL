"""This module is responsible for handling the groq API requests."""
from flask import Flask, request, jsonify
from groq import Groq
import os

os.environ['GROQ_API_KEY'] = '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'
os.environ['GROQ_API_URL'] = 'https://api.groq.io/v1/translate'

def chat_bot(input):
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


def translate():
    data = request.json
    text = data['text']
    target_language = data['target_language']

    headers = {
        'Authorization': f'Bearer {os.getenv("GROQ_API_KEY")}',
        'Content-Type': 'application/json'
    }

    payload = {
        'q': text,
        'target': target_language
    }
    
    response = request.post(os.getenv("GROQ_API_URL"), headers=headers, json=payload)
    return jsonify(response.json())
