import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to control the LED
@app.route('/led', methods=['POST'])
def control_led():
    action = request.json.get('action')
    # Logic to control the LED (this will interact with your ESP32)
    if action == 'on':
        # Turn LED on
        pass
    elif action == 'off':
        # Turn LED off
        pass
    return jsonify({'status': f'LED is {action.upper()}'})

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

