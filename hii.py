import twilio

from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to='your_phone_number_to_call',
    from_='your_twilio_phone_number',
    url='http://demo.twilio.com/docs/voice.xml'  # URL containing TwiML instructions for the call
)

print(call.sid)  # Print the SID of the call
