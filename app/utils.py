import logging
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

twilio_number = os.getenv("TWILIO_NUMBER")
to_number = os.getenv("TO_NUMBER")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(to_number, text):
    try:
        message = client.messages.create(
            from_=f'whatsapp:{twilio_number}',
            body=text,
            to=f'whatsapp:{to_number}',
        )
        logger.info(f'Message sent to {to_number}: {message.body}')
    except Exception as e:
        logger.error(f'Error sending message to {to_number}: {e}')
