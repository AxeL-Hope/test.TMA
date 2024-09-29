import requests
from flask import Flask, render_template, request, jsonify
from config import authBotToken

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/button/<int:button_id>', methods=['POST'])
def button_action(button_id):
    data = request.json
    print(data)
    url = f"https://api.telegram.org/bot{authBotToken}/sendMessage"
    payload = {
        'chat_id': data['userId'],
        'text': f"{data['initDataUnsafe']}"
    }
    response = requests.post(url, json=payload)
    return jsonify(f"{response.text}")


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=80)
