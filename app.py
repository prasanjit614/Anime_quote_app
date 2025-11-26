from flask import Flask, render_template, jsonify
import random
from quotes import quotes

app = Flask(__name__)

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/api/quote', methods=['GET'])
def api_quote():
        quote = random.choice(quotes)
        return jsonify(quote)
if __name__ == '_main_':
    print("Starting Flask app on http://127.0.0.1:5000")
    app.run(debug=True)
