from flask import Flask
from flask import request, jsonify, render_template
from lib.chat import RWKVChat

app = Flask(__name__)
rwkvchat = RWKVChat()

@app.route('/', methods=['GET'])
def home():
    return render_template('templates/index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.values.get('message', None)
    user = request.values.get('user', '')
    answer = rwkvchat.get_answer(message=message, user=user)
    res = {
        'status': 'ok',
        'answer': answer
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
