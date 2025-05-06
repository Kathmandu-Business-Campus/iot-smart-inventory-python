import serial
import time
from pynput.keyboard import Controller

# Set your Arduino's serial port here
SERIAL_PORT = '/dev/ttyACM0'  # Or '/dev/ttyUSB0' depending on your system
BAUD_RATE = 9600

keyboard = Controller()

# Open serial connection
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
            keyboard.type(line)
            keyboard.press('\n')
            keyboard.release('\n')

except KeyboardInterrupt:
    print("Stopped.")
finally:
    ser.close()
