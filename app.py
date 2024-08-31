import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize LED status
led_status = 'off'  # Default LED status

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to control the LED
@app.route('/led', methods=['POST'])
def control_led():
    global led_status  # Use global variable to track LED status
    print(f"Received a POST request: {request.json}")  # Log the incoming request
    action = request.json.get('action')
    print(f"Action received: {action}")  # Log the action received

    if action == 'on':
        led_status = 'on'  # Update LED status to 'on'
        # Logic to turn LED on (if applicable to your setup)
        # For example, you might send a signal to the ESP32 here
        return jsonify({'status': 'on'})

    elif action == 'off':
        led_status = 'off'  # Update LED status to 'off'
        # Logic to turn LED off (if applicable to your setup)
        # For example, you might send a signal to the ESP32 here
        return jsonify({'status': 'off'})

    elif action == 'get_status':
        # Return the current status of the LED
        return jsonify({'status': led_status})

    return jsonify({'status': f'LED is {led_status.upper()}'})

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
