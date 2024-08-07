from flask import Flask, redirect, request, session, url_for, render_template
import requests
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/callback')
async def callback():
    logging.debug("Callback function called")
    verifier = request.args.get('oauth_verifier')
    logging.debug(f"Verifier: {verifier}")
    return "Callback received", 200

if __name__ == '__app1__':
    app.run(debug=True)