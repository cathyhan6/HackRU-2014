from flask import Flask, request, redirect, jsonify
import sendgrid
import json
import wolframalpha

app = Flask(__name__)
clientW = wolframalpha.Client("TTAVEX-73R7X8KQ9V")
clientSG = sendgrid.SendGridClient("JakeRossSilverman", "cornell01")


@app.route("/", methods=['POST'])
def getTextData():
	text = request.values.get("text", None)
	userEmail = json.loads(request.values.get("envelope", None))["from"]
	ourEmail = request.values.get("to", None)

	res = clientW.query(text)
	returnValue = next(res.results).text
	message = sendgrid.Mail()
	message.add_to(userEmail)
	print userEmail
	print ourEmail
	message.set_subject('Result')
	message.set_text(returnValue)
	message.set_from('AlphaText <' + ourEmail + '>')
	print clientSG.send(message)

	return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)

