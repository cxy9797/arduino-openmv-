#include <ArduinoJson.h>
#include <SoftwareSerial.h>
SoftwareSerial softSerial(10,11); // RX, TX
volatile int cx;
volatile int cy;
volatile char z;
String json;
int buzzer=19;   //蜂鸣器

void setup()
{
  pinMode(buzzer,OUTPUT);
  cx = 0;
  cy = 0;
  z = 0;
  json = "";
  Serial.begin(9600);
  softSerial.begin(9600);
}

void loop()
{
   digitalWrite(buzzer,HIGH);
  if (softSerial.available() > 0) 
   {
    z = char(softSerial.read());
    json = String(json) + String(z);
    if (z == '}')
     {
      DynamicJsonDocument doc(200); //声明一个JsonDocument对象
      deserializeJson(doc, json);
      JsonObject obj = doc.as<JsonObject>();
      int cx = doc["cx"];
      int cy = doc["cy"];
      if (cx!=0&&cy!=0)
       {
        Serial.print("cx = ");
        Serial.print(cx);
        Serial.print("cy = ");
        Serial.println(cy);
       digitalWrite(buzzer,LOW);
        delay(100);
        digitalWrite(buzzer,HIGH);
        delay(100);
        digitalWrite(buzzer,LOW);
        delay(100);
        digitalWrite(buzzer,HIGH);
        delay(100);
        }
        json = "";
      }
    }
}
