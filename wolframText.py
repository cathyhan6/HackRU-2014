from flask import Flask, request, redirect
import sendgrid
import wolframalpha

app = Flask(__name__)
clientW = wolframalpha.Client("TTAVEX-73R7X8KQ9V")
clientSG = sendgrid.SendGridClint("JakeRossSilverman", "cornell01")


@app.route("/wolf", methods=['GET', 'POST'])
def getTextData():
	text = request.values.get("text", None)
	userEmail = request.values.get("from", None)
	ourEmail = request.values.get("to", None)

	res = clientW.query(text)
	returnValue = next(res.results).text
	
	message = sendgrid.Mail()
	message.add_to(userEmail)
	message.set_subject('Result')
	message.set_text(returnValue)
	message.set_from('AlphaText <' + ourEmail + '>')
	status, msg = sg.send(message)


if __name__ == '__main__':
    app.run(debug=True)

