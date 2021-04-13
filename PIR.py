import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class PIR:

    def __init__(self, channel, callback):
        self._channel = channel
        self._callback = callback
        print(f'PIR activated on PIN {self._channel}')
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(self._channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        GPIO.add_event_detect(self._channel, GPIO.BOTH, callback=self._callback)
        # GPIO.cleanup() # Clean up

    def isTriggerred(self):
        return GPIO.input(self._channel)