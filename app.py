from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup GPIO
LED_PIN = 2  # GPIO pin where the LED is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route('/led', methods=['POST'])
def control_led():
    data = request.json
    action = data.get('action')
    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return jsonify({'status': 'LED is ON'})
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return jsonify({'status': 'LED is OFF'})
    else:
        return jsonify({'error': 'Invalid action'}), 400

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
