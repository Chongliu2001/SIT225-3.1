#include "thingProperties.h"

// Define the pins for the HC-SR04 sensor
const int trigPin = 9;  // Trig pin connected to digital pin 9
const int echoPin = 10; // Echo pin connected to digital pin 10

void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);

  // Initialize the properties defined in Arduino Cloud
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  // Set the trigger pin as output and the echo pin as input
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Wait for connection to stabilize
  delay(1500);
}

void loop() {
  // Update the Arduino Cloud connection
  ArduinoCloud.update();

  // Measure the distance using HC-SR04
  distance = measureDistance();

  // Print the distance to the serial monitor for debugging
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Wait 30 seconds before the next measurement
  delay(30000);
}

// Function to measure distance using HC-SR04
float measureDistance() {
  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Trigger the sensor by setting the trigPin high for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, and calculate the distance
  long duration = pulseIn(echoPin, HIGH);
  float distance = duration * 0.034 / 2;

  return distance;
}
