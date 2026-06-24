from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

SHEETS_URLS = {
    'recovery':  'https://script.google.com/macros/s/AKfycbxmUzo3yQ3dKhUWMHcuWBN8roIcF1FT0QkEX0Pgsj0yfMgTXDYlrZ5qfk8EJYHDj_X6/exec',
    'athlete':   'https://script.google.com/macros/s/AKfycbx9l5a09R12eGp6HRdqGNlJRy7vrFfgpHtAfU9kevfrzXolhE5xY9gTK0cDmBOrClau/exec',
    'hydration': 'https://script.google.com/macros/s/AKfycbyQE3OdwrJCjxAb0lBE0zLI9M9z3fkfShf9d7ZLV4gDXn3pl9pL-0Jni4BSt59h0RdFqQ/exec',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    test = data.get('test')
    if test not in SHEETS_URLS:
        return jsonify({'ok': False}), 400
    try:
        requests.post(SHEETS_URLS[test], json=data, timeout=5)
    except Exception:
        pass
    return jsonify({'ok': True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)