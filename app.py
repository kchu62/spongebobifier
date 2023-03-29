from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def alternate_case(text):
    result = []
    capitalize = True
    for char in text:
        if char.isalpha():
            if capitalize:
                result.append(char.upper())
            else:
                result.append(char.lower())
            capitalize = not capitalize
        else:
            result.append(char)
    return ''.join(result)


@app.route('/api/message', methods=['POST'])
def process_message():
    data = request.get_json()
    text = data.get('message', '')
    response = alternate_case(text)
    res = make_response(jsonify({'response': response}))
    return res


if __name__ == '__main__':
    app.run(debug=True)
