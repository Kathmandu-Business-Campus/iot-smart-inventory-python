import serial
import requests

# Set your Arduino's serial port here
SERIAL_PORT = '/dev/ttyACM0'  # Or '/dev/ttyUSB0' depending on your system
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Give Arduino time to reset

print("Listening to Arduino...")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            # Note:
            # Instead of using pynput for emulating keyboard, 
            # you may use requests library to send request to your web application server.
            print(f"Received: {line}")
            requests.post('http://localhost:8000/path/name', data=line)

except KeyboardInterrupt:
    print("Stopped.")
finally:
    ser.close()
