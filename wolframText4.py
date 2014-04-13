from flask import Flask, request, redirect, jsonify
import sendgrid
import json
import wolframalpha
import urllib
import sys
from wolfram3 import wolfram

app = Flask(__name__)
clientW = wolframalpha.Client("TTAVEX-73R7X8KQ9V")
clientSG = sendgrid.SendGridClient("JakeRossSilverman", "cornell01")


@app.route("/", methods=['POST'])
def getTextData():
	envelope = json.loads(request.form.get('envelope'))
	text = request.form.get("text")
	userEmail = envelope['to'][0]
	ourEmail = envelope['from']

	appid = "TTAVEX-73R7X8KQ9V"
	query = text
	w = wolfram(appid)
	w.search(query)

	"""print returnValue
	urllib.urlretrieve(returnValue, 'data.png') """
	message = sendgrid.Mail()
	message.add_to(userEmail)
	print userEmail
	print ourEmail
	message.set_subject('Result')
	message.set_text('success')
	message.set_from('AlphaText <' + ourEmail + '>')
	print clientSG.send(message)

	return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)

