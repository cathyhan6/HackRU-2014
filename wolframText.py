from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def getTextData():
	text = request.values.get('Body', None)
	number = request.values.get('From', None)

	# todo Wolfram api stuff

	account_sid = "ACc9712f9632cb63e46876bc4a62e476af"
	auth_token = "a0f08f7a8d0870df130ee070b59009f0"
	client = TwilioRestClient(account_sid, auth_token)

	sms = client.sms.messages.create(
		body = "sent success", 
		to = number, 
		from_= "+13477325742"
		)
	return "Success"


if __name__ == '__main__':
    app.run(debug=True)

