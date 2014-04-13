from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import wolframalpha

app = Flask(__name__)
clientW = wolframalpha.Client("TTAVEX-73R7X8KQ9V")

@app.route("/", methods=['GET, 'POST])
def doEverything():
	text = request.values.get('Body', none)
	number = request.values.get('From', none)

	result = clientW.query(text)

	account_sid = "PN88dd7bd53b53c71f7dd274e5039265ad"
	auth_token = "a0f08f7a8d0870df130ee070b59009f0"
	clientT = TwilioRestClient(account_sid, auth_token)

	sms = clientT.sms.messages.create(
		body = result, 
		to = number, 
		from_= "+3477325742"
		)


if __name__ == '__main__':
    app.run()

