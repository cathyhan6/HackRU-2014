from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import wolframalpha

app = Flask(__name__)
clientW = wolframalpha.Client("TTAVEX-73R7X8KQ9V")


@app.route("/wolf", methods=['GET', 'POST'])
def getTextData():
	text = request.values.get('Body', None)
	number = request.values.get('From', None)

	res = clientW.query(text)
	returnValue = next(res.results).text

	account_sid = "ACc9712f9632cb63e46876bc4a62e476af"
	auth_token = "a0f08f7a8d0870df130ee070b59009f0"
	clientT = TwilioRestClient(account_sid, auth_token)

	sms = clientT.sms.messages.create(
		body = returnValue, 
		to = number, 
		from_= "+13477325742"
		)
	return "Success"


if __name__ == '__main__':
    app.run(debug=True)

