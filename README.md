# Raspberry Pi Flask Server

Python Flask Web Server used to control LED state. See 'RPI_iOS' for iOS application.

## Layout

```
pi@raspberrypi: $ tree
.
├── app.py           - Flask server
├── static
│   └── style.css    - CSS Styling
└── templates
    └── index.html   - HTML Webpage
```

## Running Flask server

```
pi@raspberrypi: $ sudo python3 app.py 

[*] Setting up GPIO Pins
[*] Flashing LED
[*] Raspberry Pi IP Address: 10.0.0.184
[*] Port number 8080

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 

 * Debugger is active!
 * Debugger PIN: 976-720-464
10.0.0.244 - - [19/Oct/2020 22:47:35] "GET /ledYlw/on HTTP/1.1" 200 -
10.0.0.244 - - [19/Oct/2020 22:47:36] "GET /ledYlw/off HTTP/1.1" 200 -
10.0.0.244 - - [19/Oct/2020 22:47:37] "GET /ledYlw/on HTTP/1.1" 200 -
10.0.0.244 - - [19/Oct/2020 22:47:37] "GET /ledYlw/off HTTP/1.1" 200 -
10.0.0.244 - - [19/Oct/2020 22:47:39] "GET /ledYlw/on HTTP/1.1" 200 -
10.0.0.244 - - [19/Oct/2020 22:47:39] "GET /ledYlw/off HTTP/1.1" 200 -
```
