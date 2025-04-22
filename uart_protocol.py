from machine import UART
import time
 
uart = UART(2, baudrate=9600, tx=17, rx=16)
 
def send_message(receiver_id, line_position):
    START = 0x41
    SENDER = 0x01  
    END = 0x42

 
    if line_position < 0:
        line_position &= 0xFF
 
    msg = bytes([START, SENDER, receiver_id, line_position, END])
    uart.write(msg)
    print("Sent:", [hex(b) for b in msg])
 
def read_message():
    if uart.any():
        msg = uart.read(5)
        if msg and msg[0] == 0x41 and msg[-1] == 0x42:
            print("Received:", [hex(b) for b in msg])
            return msg
        else:
            print("Malformed or no message.")
    return None