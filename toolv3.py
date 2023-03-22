import socket
import urllib.request
from twilio.rest import Client

# get user's IP address
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# create a socket object to get open port number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(1)
port = s.getsockname()[1]
s.close()

# send IP and port number through Twilio
account_sid = 'ACaab8ff7d7a20e2d6a9a3322beebf7dd1'
auth_token = '57a64e7f169aa128947c46c4b349a37a'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body='IP: ' + external_ip + ', Port: ' + str(port),
    from_='+18885306548',
    to='+19493243484'
)
