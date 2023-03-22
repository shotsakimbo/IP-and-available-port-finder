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
account_sid = 'ACCOUNT SID'
auth_token = 'AUTH TOKEN'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body='IP: ' + external_ip + ', Port: ' + str(port),
    from_='TWILIO NUMBER',
    to='VERIFIED TWILIO NUMBER(YOUR NUMBER)'
)
