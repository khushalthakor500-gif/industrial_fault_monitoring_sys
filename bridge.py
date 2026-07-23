import serial
import json
import time

arduino = serial.Serial("COM3", 9600, timeout=1)

time.sleep(2)

while True:
    try:
        line = arduino.readline().decode().strip()

        if line:
            print(line)

            data = line.split(",")

            sensor = {
                "temperature": float(data[0].split(":")[1]),
                "current": float(data[1].split(":")[1]),
                "gas": int(data[2].split(":")[1]),
                "vibration": int(data[3].split(":")[1])
            }

            with open("sensor_data.json", "w") as f:
                json.dump(sensor, f)

    except Exception as e:
        print(e)