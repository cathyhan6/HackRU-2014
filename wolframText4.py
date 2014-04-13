from flask import Flask, request, redirect, jsonify
import sendgrid
import requests
import json
import wolframalpha
import urllib
import sys
from wolfram3 import wolfram
import uuid


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
	text = text.replace(' ', '+')
	print "text: " + text

	appid = "TTAVEX-73R7X8KQ9V"
	query = text
	w = wolfram(appid)
	image = w.search(query)

	print ("image: " + image)

	r = requests.get(image, stream=True)
	f = open('./image', 'wb')
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
	message.set_subject('Result')
	message.set_text('success')
	message.set_from('AlphaText <' + ourEmail + '>')
	message.add_attachment('image.png', './image')
	print clientSG._build_body(message)
	print clientSG.send(message)

	return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)

