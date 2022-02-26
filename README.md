# Remote Monitoring Service

A real-time monitoring service for sensors readings.

## Requirements Description

ESP chip is a microcontroller chip with a wireless module ready for wireless communication. 

Use this chip to develop the below requirements:

	1. Connect any two sensors (e.g. temperature and pressure) to the ESP.
	2. The sensors readings should be transferred through WiFi to some server and saved in real time into some sql database on that server.
	3. On the server, there should be a small application that sends control wireless signals to the ESP. For ex, a click on a button 
		to toggle the data acquisition between pressure and temperature. Or, a click on a button to raise an alarm led connected to the ESP
	4. The saved data on this server can be visualized on either a desktop software (might well be the server itself), or mobile app 
		(feel free to choose which mobile OS you like to use). So in brief, I need to see the signal drawn and updated on some 
		 graph on a computer screen or mobile screen.

## prerequisites

- [Node.js](https://nodejs.org/en/)
- [Python3](https://www.python.org/downloads/)
- [TypeScript](https://www.typescriptlang.org/)
- [Sqlite3](https://www.sqlite.org/)

## installation

<details>
<summary>Server</summary>
<br>
Inside the server folder in terminal run:
<pre>
$ npm install
$ npm run build
$ npm run start
</pre>
</details>
<details>
<summary>PyQt5 Application</summary>
<br>
Inside the desktop folder in terminal run:
<pre>
(both)       $ python -m venv .env
(terminal)   $ source .env/bin/activate
(Powershell) $ .env\Scripts\activate.ps1
(both)       $ pip install -r requirements.txt
(both)       $ python main.py
</pre>
</details>


## future improvements

Instead of using an API endpoints, I could have used a websocket connection. as right now it's not possible to send data from the ESP to the server. we faked the real-time by making the ESP check for the alarm every second.
