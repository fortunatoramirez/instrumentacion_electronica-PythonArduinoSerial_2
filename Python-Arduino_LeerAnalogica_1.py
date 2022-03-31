import serial
import time

# Conectando por serial a Arduino
print("Conectando al Arduino...")
arduino = serial.Serial('COM6', 9600, timeout = 3.0)
print("Conectado al Arduino.")

while True:
    arduino.write("r".encode())
    val = arduino.readline().strip()
    if not val:
        continue
    #val = float(val)
    val = int(val)
    print(val)
    time.sleep(0.5)