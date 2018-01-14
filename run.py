# key banks
YES = ['yes', 'yea', 'yup']
NO = ['no', 'nah', 'nope']

# import libraries
from twilio.rest import Client
import parse as p
# account credentials
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"
my_num = "+YOUR PHONE NUMBER"
# create client
client = Client(account_sid, auth_token)
tag = ''
# main loop
while True:
	# get message from twilio
	for message in client.messages.list():
		# if recieved message
		if message.direction == "inbound":
			# message to lowercase
			my_message = message.body.lower()
			# if first message in exchange
			if tag == '':
				# get symptom tag
				tag = p.get_tag(my_message)
				# get follow up
				return_message = p.get_follow(tag)
				# if no follow up
				if return_message == '':
					# get first tag
					tag = p.get_sub_tag(tag, 'yes')
					# get response
					return_message = p.get_response(tag)
					# clear tag
					tag = ''
			else:
				# get symptom sub_tag
				if my_message in YES:
					tag = p.get_sub_tag(tag, 'yes')
				elif my_message in NO:
					tag = p.get_sub_tag(tag, 'no')
				else:
					tag = ''
				# get response
				return_message = p.get_response(tag)
				# clear tag
				tag = ''
			# send message
			client.api.account.messages.create(
				to = message.from_,
				from_ = my_num,
				body = return_message)
			try:
				# delete message
				client.messages(message.sid).delete()
			except:
				# error output
				print("error: no message to delete")