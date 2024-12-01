from flask import Flask, request, Response
import requests

app = Flask(__name__)

TOKEN = '7242300888:AAE13NFIxOkA0x4dZ2Af9eQGD37WIfJ623g'

WEBHOOK_URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://96b8-38-56-236-175.ngrok-free.app/message'
requests.get(WEBHOOK_URL)

@app.route('/sanity')
def sanity():
    return "Server is running"

@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")

    # Get the chat ID and message text from the incoming request
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    # Respond to the user with the same text they sent
    response_text = f"You said: {text}"
    send_message(chat_id, response_text)

    # Send a "Got it" message as well
    send_message(chat_id, "Got it")

    return Response("success")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


if __name__ == '__main__':
    app.run(port=5002)



