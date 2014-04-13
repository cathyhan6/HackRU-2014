from flask import Flask, request, redirect
import twilio.twiml

app = Flask(Wolfram_sms)

@app.route("/", methods=['GET, 'POST])
def foo():
	r