from twilio.rest import Client
import os

# Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    from_number = os.getenv('TWILIO_PHONE_NUMBER')
    message = client.messages.create(
        to=to_number,
        from_= os.getenv('TWILIO_PHONE_NUMBER'),
        body=message
    )
    return message.sid