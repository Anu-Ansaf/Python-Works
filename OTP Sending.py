import random

from twilio.rest import Client

otp = random.randint(10000, 99999)
account_sid = "Find From Twolio account "
token = "Find From Twolio account"
client = Client(account_sid, token)

message = client.messages.create(
    body='OTP :' + str(otp),
    from_="Your Trial Number",
    to='Your Phone Number'
)

print(message.sid)
print(otp)
