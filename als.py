#!/usr/bin/python3 als.py

import time
from Relay import Relay
from ALSensor import ALSensor

def ALTrigger(pin):
    if als.isTriggerred():
        print("Hello... is there anybody out there?")
        r.on()
    else:
        print("Waiting...")
        r.off()
    

als = ALSensor(15, ALTrigger)
r = Relay(13)
r.off()

try:
    while 1>0:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Interupted")
    pass



