import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Relay:

    def __init__(self, channel):
        self._channel = channel
        print(f'Relay activated on PIN {self._channel}')
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(self._channel, GPIO.OUT)
        # GPIO.cleanup() # Clean up

    def off(self):
        GPIO.output(self._channel, GPIO.HIGH)

    def on(self):
        GPIO.output(self._channel, GPIO.LOW)

    def isOn(self):
        return GPIO.input(self._channel)



if __name__ == '__main__':
    r = Relay(16)
    r.on()
    time.sleep(2)
    r.off()