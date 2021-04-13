#!/usr/bin/python3 PIR-Switch.py

import time
from Relay import Relay
from PIR import PIR

PIR_PIN = 15
RELAY_PIN = 13

def trigger(pin):
    if pir.isTriggerred():
        print("Motion detected!!!")
        r.on()
    else:
        print("All is quiet.")
        r.off()
    

pir = PIR(PIR_PIN, trigger)
r = Relay(RELAY_PIN)
r.off()

try:
    while 1>0: time.sleep(0.1)

except KeyboardInterrupt:
    print("\nInterupted... Goodbye!\n")
    r.off()
