#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <DHT.h>
#include <ArduinoJson.h>
#define DHTPIN D3

#define led D5
DHT dht(DHTPIN, DHT11);  

const char* ssid ;
const char* password;
const char* serverName = "http://remote-monitoring-api.herokuapp.com/reading";
//const char* serverName = "http://192.168.1.7:3000/reading";
unsigned long lastTime = 0;
unsigned long timerDelay = 2000;
char char_array_user[255];
char char_array_pass[255];
char *data[]={char_array_user,char_array_pass};
int network_num = 0;

void control_led (){
      WiFiClient client;
      HTTPClient http;
      //String serverPath = "http://192.168.1.7:3000/";
      String serverPath = "http://remote-monitoring-api.herokuapp.com/control/alarm";

      http.begin(client, serverPath.c_str());
      int httpResponseCode = http.GET();
      String payload = http.getString(); 
      Serial.println(payload);
      const size_t capacity = JSON_OBJECT_SIZE(1)+ 60;
      DynamicJsonBuffer jsonBuffer(capacity);
      JsonObject& root = jsonBuffer.parseObject(payload);
      if (!root.success()) {
        Serial.println(F("Parsing failed!"));
        return;
      }
      Serial.println(F("alarm:"));Serial.println(root["alarm"].as<char*>());
      String is_set = root["alarm"].as<char*>();
      if(is_set == "1"){
          digitalWrite(led,HIGH);
        }else{
          digitalWrite(led,LOW);
          }
  }
  
char* serial_tochar(int choose_data) {
    while(Serial.available()==0) { }
    String str =Serial.readString();
    str.toCharArray(data[choose_data], str.length());
    return data[choose_data];
  }
void connect_wifi() {
    char * username;
    Serial.println("Please enter the username: ");
    username = strtok(serial_tochar(0), " ");
    char * password;
    Serial.println("Please enter the password: ");
    password = strtok(serial_tochar(1), " ");
    WiFi.begin(username, password);

    uint8_t i = 0;
    while(WiFi.status() != WL_CONNECTED && i < 20) {
      Serial.print(".");
      delay(500);
      i++;
    }
  }

void print_wifi(){
  network_num = WiFi.scanNetworks();
  Serial.print("number of network equal :");
  Serial.println(network_num);
  for (int i=0;i<network_num;i++){
    Serial.print("WiFi name : ");
    Serial.println(WiFi.SSID(i));
    Serial.print("Signal Strenth : ");
    Serial.println(WiFi.RSSI(i));
    Serial.println("------------");
    }
  }
void setup() {
  Serial.begin(115200);
  print_wifi();
  connect_wifi();
  pinMode(led,OUTPUT);
  Serial.println("Connecting....");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Timer set to 2 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}


void loop() {
  //Send an HTTP POST request every 10 minutes
  if ((millis() - lastTime) > timerDelay) {
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
      http.begin(client, serverName);
      // Specify content-type header
      //http.addHeader("Content-Type", "application/x-www-form-urlencoded");
      // Data to send with HTTP POST
      //String httpRequestData = "api_key=tPmAT5Ab3j7F9&sensor=BME280&value1=24.25&value2=49.54&value3=1005.14";           
      // Send HTTP POST request
      //int httpResponseCode = http.POST(httpRequestData);
      // If you need an HTTP request with a content type: application/json, use the following:
      http.addHeader("Content-Type", "application/json");
      String json ;
      float h = dht.readHumidity();
      float t = dht.readTemperature();
      if (isnan(h) || isnan(t)) 
         {
              return;
         }
      Serial.print("temp = ");
      Serial.println(t);
      Serial.print("humity= ");
      Serial.println(h);
      json = "{\"timestamp\":\"" + String(millis()) + "\",";
      json +="\"humidity\":\"" + String(h) + "\",";
      json += "\"temperature\":\"" + String(t) + "\"}";    
      int httpResponseCode = http.POST(json);

      // If you need an HTTP request with a content type: text/plain
      //http.addHeader("Content-Type", "text/plain");
      //int httpResponseCode = http.POST("Hello, World!");
     
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
        
      // Free resources
      http.end();
      control_led();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
}
