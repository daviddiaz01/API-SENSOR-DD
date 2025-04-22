from machine import SoftI2C, Pin
import time

i2c = SoftI2C(scl=Pin(9), sda=Pin(8), freq=100000)
OPT4060_ADDR = 0x44

led = Pin(15, Pin.OUT)

while True:
    
    i2c.writeto(OPT4060_ADDR, bytes([0x0A, 0x30, 0x78]))
    time.sleep_ms(100)

    i2c.writeto(OPT4060_ADDR, bytes([0x00]))
    data = i2c.readfrom(OPT4060_ADDR, 16)

    red   = ((data[0] & 0x0F) << 8) | data[1]
    green = ((data[4] & 0x0F) << 8) | data[5]
    blue  = ((data[8] & 0x0F) << 8) | data[9]
    clear = ((data[12] & 0x0F) << 8) | data[13]

    print("Red:", red, "Green:", green, "Blue:", blue, "Clear:", clear)

    if red > green and red > blue and red > 200:
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    else:
        led.off()
        time.sleep(0.5)