import serial
import time

ser = serial.Serial("COM3", 9600, timeout=2)
time.sleep(2)

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    print(line)
    