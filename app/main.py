from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return '<h1>Telegate bot proxy</h1>'

@app.route('/msg')
def msg():
    botId = request.args.get('botid')
    chatId = request.args.get('chatid')
    messageText = request.args.get('message')

    url = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (botId, chatId, messageText)

    response = requests.get(url)

    return response.text
