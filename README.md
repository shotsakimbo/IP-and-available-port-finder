# IP-and-available-port-finder
finds the IP address and available port and sends it through SMS using twilio API

## Required installations
- open file location and type **cmd** and **enter** in the top left
- enter these into the command prompt: 
```bash
pip install twilio
```
## Configuring SMS
- create twilio account at https://www.twilio.com/try-twilio
- on the left under develop, click on phone numbers> manage> active numbers
- create a number
- next click on verified caller IDs and enter and verify your number
- on the top right click on acoount and open API keys and tokens
- you will be able to se your account SID and auth token, you will need these
- you will need to edit this section:
```python
# send IP and port number through Twilio
account_sid = 'ACCOUNT SID'
auth_token = 'AUTH TOKEN'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body='IP: ' + external_ip + ', Port: ' + str(port),
    from_='TWILIO NUMBER',
    to='VERIFIED TWILIO NUMBER(YOUR NUMBER)'
)
```
## Converting to .exe
- open file location and type **cmd** and **enter** in the top left
- enter these into the command prompt under your file location: 
```bash
pip install pyinstaller
```
```bash
pyinstaller --onefile -w main.py
```
- **--onefile** makes the exe compact instead of having multiple files
- **-w** hides the command prompt when the it is running
# ⚠️DISCLAIMER/WARNING⚠️
- **THIS IS FOR EDUCATIONAL PURPOSES ONLY**
- This tool is not intended for malicious purposes, such as IP grabbing or any other form of cyber attack. I am not responsible for any misuse or damage caused by this tool.

