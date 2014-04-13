from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def getTextData():
	text = request.values.get('Body', none)
	number = request.values.get('From', none)

	# todo Wolfram api stuff

	account_sid = "PN88dd7bd53b53c71f7dd274e5039265ad"
	auth_token = "a0f08f7a8d0870df130ee070b59009f0"
	client = TwilioRestClient(account_sid, auth_token)

	sms = client.sms.messages.create(
		body = "sent success", 
		to = number, 
		from_= "+3477325742"
		)


if __name__ == '__main__':
    app.debug = True
    app.run()

