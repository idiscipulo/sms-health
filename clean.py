# import libraries
from twilio.rest import Client
# account credentials
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"
my_num = "+YOUR PHONE NUMBER"
# create client
client = Client(account_sid, auth_token)
# get message from twilio
for message in client.messages.list():
	try:
		# delete message
		client.messages(message.sid).delete()
	except:
		# error output
		print("error: no message to delete")