from flask import Flask, request, redirect, jsonify
import sendgrid
import requests
import json
import wolframalpha
import urllib
import sys
from wolfram3 import wolfram
import uuid
import os


app = Flask(__name__)
clientW = wolframalpha.Client("TTAVEX-73R7X8KQ9V")
clientSG = sendgrid.SendGridClient("JakeRossSilverman", "cornell01")


@app.route("/", methods=['POST'])
def getTextData():
	envelope = json.loads(request.form.get('envelope'))
	text = request.form.get('text')
	print 'text: ' + text
	ourEmail = envelope['to'][0]
	userEmail = envelope['from']
	userInput = text
	"""text = text.replace(' ', '+')"""
	print "text: " + str(text)

	appid = "TTAVEX-73R7X8KQ9V"
	query = text
	w = wolfram(appid)
	image = w.search(query)

	print ("image: " + str(image))

	if(image == False):
		message = sendgrid.Mail()
		message.add_to(userEmail)
		print userEmail
		print ourEmail
		message.set_subject('Result for: ' + userInput)
		message.set_text('No result available')
		message.set_from('AlphaText <' + ourEmail + '>')
		print clientSG._build_body(message)
		print clientSG.send(message)
	else:
		unique_filename = unicode(uuid.uuid4())

		r = requests.get(image, stream=True)
		f = open(unique_filename, 'wb')
		if r.status_code == 200:
			for chunk in r.iter_content():
				f.write(chunk)
    	   	f.close()
		"""print returnValue
		urllib.urlretrieve(returnValue, 'data.png') """
		message = sendgrid.Mail()
		message.add_to(userEmail)
		print userEmail
		print ourEmail
		message.set_subject('Result for: ' + userInput)
		message.set_text(' ')
		message.set_from('AlphaText <' + ourEmail + '>')
		message.add_attachment(unique_filename + '.png', unique_filename)
		print clientSG._build_body(message)
		print clientSG.send(message)
    
		os.remove(unique_filename)

	return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)

