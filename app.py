from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins
openai_client = OpenAI()

@app.route('/send-message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a workplace discrimination legal assistant in the Philippines."},
            {"role": "user", "content": user_input},
        ]
    )
    bot_response = response.choices[0].message.content
    return jsonify({'message': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
