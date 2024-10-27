from twilio.rest import Client
import os

# Twilio credentials
account_sid = 'SK5e1aa1c447d710c4c9361e410d601054'
auth_token = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    from_number = os.getenv('TWILIO_PHONE_NUMBER')
    message = client.messages.create(
        to = to_number,
        from_= from_number,
        body = message
    )
    return message.sid