#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "93AA@unifi";         // Replace with your Wi-Fi SSID
const char* password = "11931193Aa1"; // Replace with your Wi-Fi password

const char* serverURL = "https://f-domain.onrender.com/led"; // Replace with your Render Flask server URL

const int ledPin = 13; // GPIO 2 (typically the built-in LED on the ESP32)

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);   // Turn LED off

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    // Make a POST request to the server
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"action\":\"get_status\"}"; // Example payload, modify as needed

    int httpResponseCode = http.POST(payload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Response from server:");
      Serial.println(response);

      // Simple logic to turn LED on or off based on server response
      if (response.indexOf("on") > 0) {
        digitalWrite(ledPin, HIGH);  // Turn LED on
      } else if (response.indexOf("off") > 0) {
        digitalWrite(ledPin, LOW);   // Turn LED off
      }

    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("Wi-Fi not connected");
  }

  delay(3000); // Wait for 10 seconds before sending the next request
}