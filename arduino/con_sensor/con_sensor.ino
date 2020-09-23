#include "DHT.h"

// DHT Sensor
uint8_t DHTPin = D8;

#define DHTTYPE DHT11

// Initialize DHT sensor.
DHT dht(DHTPin, DHTTYPE);

float Temperature;
float Humidity;


void setup() {
  Serial.begin(115200);
  delay(100);
  pinMode(DHTPin, INPUT);
  Serial.println("DHT22 test!");

  dht.begin();
  Serial.println("Connecting to ");
}

void loop() {
  Temperature = dht.readTemperature(true); // Gets the values of the temperature
  Humidity = dht.readHumidity();

  Serial.print("Temperatura: ");
  Serial.print(Temperature);
  Serial.print(" °C ");
  Serial.print("Humidity: ");
  Serial.print(Humidity);
  Serial.println(" %");
  delay(1000);
}
