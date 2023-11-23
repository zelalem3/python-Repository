from twilio.rest import Client
account_sid = "AC55fd17cd47a5d1341d7707cf7a559cec"
auto_token = "2a8d39cc4b4951c8ccdfd70bfb903095 "
client = Client(account_sid, auto_token)
message = client.message \
    .create\
        (
        body= "hello zelalem, how are you?"
        from=
        to=
        )