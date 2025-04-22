from machine import SoftI2C, Pin
import time

i2c = SoftI2C(sda=Pin(8), scl=Pin(9))

while True:
    devices = i2c.scan()
    if devices:
        print("I2C devices found:")
        for d in devices:
            print(" - Decimal:", d, " | Hex:", hex(d))
    else:
        print("No I2C devices found.")
    time.sleep(2)

