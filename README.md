# Remote-control-vehicle-for-warehouses-and-hangars-with-Raspberry-pi-4

This project provides a basic software stack for controlling a small vehicle using a Raspberry Pi 4. It allows remote operation either through a Flask based web interface or via a PC using keyboard arrows. Various sensors can also be monitored to detect hazards in warehouses or hangars.

## Features

- **Web control interface**: A Flask app (`control.py`) serves a simple page where you can move the vehicle forward, reverse, left, right or stop.
- **PC keyboard control**: By launching the script in PC control mode, the vehicle can be maneuvered using arrow keys.
- **Sensor monitoring**: `sensor.py` reads flame and gas sensors, displays temperature and humidity from a DHT11 module, and streams the camera view.

## Hardware

The code assumes the following connections on the Raspberry Pi:

- L298N motor driver connected to GPIO pins 17, 22, 23, 24 and enables on 27, 25.
- A buzzer on pin 21 and an LED on pin 2 used when reversing or alerting.
- Optional flame sensor on pin 19, gas sensor on pin 16, and DHT11 on pin 4.

Refer to the images in this repository for wiring details:

- `L298N-DC-and-raspberrypi4-connection.png` shows the motor driver connections.
- `raspberrypi4-sensors-and-breadboard-connection.png` demonstrates how sensors are attached.

## Running

1. Install dependencies on the Raspberry Pi:
   ```bash
   pip install flask gpiozero RPi.GPIO dht11 opencv-python
   ```
2. Clone this repository and ensure `index.html` is inside the `templates` directory.
3. Start the controller:
   ```bash
   python Remote-control-vehicle-for-warehouses-and-hangars-with-Raspberry-pi-4/control.py
   ```
   When prompted, enter `1` for web control or `2` for PC keyboard control.
4. To monitor sensors and the camera, run:
   ```bash
   python Remote-control-vehicle-for-warehouses-and-hangars-with-Raspberry-pi-4/sensor.py
   ```

The Flask app listens on port 5000. Open a browser on the same network to the Pi's IP address at `http://<pi-ip>:5000/` and use the onscreen buttons to drive the vehicle.

## Directory structure

```
Remote-control-vehicle-for-warehouses-and-hangars-with-Raspberry-pi-4/
├── control.py
├── pc_lib.py
├── sensor.py
└── templates/
    └── index.html
```

These scripts are intentionally simple and can be adapted to fit different vehicles or additional sensors.
