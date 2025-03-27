from uart_protocol import send_message, read_message
import time


receiver_id = 0x05  


# change receiver id as needed:
# 0x03 = Motor Controller
# 0x04 = OLED Display
# 0x05 = WiFi Module


line_position = -60


while True:
    send_message(receiver_id, line_position)
    time.sleep(0.5)
    read_message()  
    time.sleep(1.5)


    line_position += 10
    if line_position > 100:
        line_position = -100