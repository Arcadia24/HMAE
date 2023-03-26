# **Microphone network for the project cui-cui**

This project aims to a microphone network by creating modules to collect sound via I2S and send this data using HTTP.

## **Hardware**

A module is composed of:
* A sound sensor (INMP441)
* A microcontroller (ESP32)
* A battery (if you want to be autonomous)
* a battery charger 

### **Pins**

| INMP441      | ESP32    |
|--------------|-----------|
| VDD          | 3.3      |
| GND          | GND  |
| SD | IN (GPIO32) |
| L/R | GND|
|WS | WS (GPIO15) |
|SCK | BCK (GPIO14) |

To make your system autonomous you can connect a battery or more but **be careful** when using it.

## **Client**

### **Installation**

Install 3 libraries to run the program:
* SPIFFS
* WiFi
* HTTPClient

### **Parameters**

You can modify easily:
* I2S_SAMPLE_RATE (line 11)
* RECORD_TIME (line 14)
* ssid (line 246) *
* password (line 247) *
* urlAPI (270) *

*It's mandatory to modify the parameter

Rest of the parameters I don't recommend modifying them.

## **API**

### **Installation**

run : 

``` pip install -r requirements.txt ``` 

to install dependencies

### **Parameters**

you can modify in the ``` main.py``` script the parameters:
* args (line 11), it contains all the parameters to modify the mel-spectrogram transformation
* audio_path : path where audios are saved
* spectrogram_path : path where spectrograms are saved

### **Run the API**

run the API by running the command in bash:

``` python3 -m API.main```

## **Acknolegments**

Thanks to:
* [Phil Schatzmann](https://github.com/pschatzmann) for his library that help me to understand I2S using INMP441.
* [That Project youtube channel](https://www.youtube.com/watch?v=RZVzZfndIS0&t=33s) for the POST request creation and the structure of the project