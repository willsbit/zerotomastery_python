from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Twillio test SMS.",
                     from_='+123123123123',
                     to='+123123123123'
                 )

print(message.sid)
