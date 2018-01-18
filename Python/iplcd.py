#!/usr/bin/env python
from datetime import datetime
from RPLCD.gpio import *
import socket
from time import sleep


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "No Connection"
    return ip

def get_date(): return datetime.now().strftime("%y-%m-%d")
def get_time(): return datetime.now().strftime("%H:%M")

LCD = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24], numbering_mode=GPIO.BOARD)

while True:
    LCD.clear()
    LCD.cursor_pos = (0, 0)    
    LCD.write_string(get_date())
    LCD.cursor_pos = (0, 11)
    LCD.write_string(get_time())
    LCD.cursor_pos = (1, 0)
    ip = get_ip()
    LCD.write_string(ip)
    if ip == "No Connection":
        sleep(1)
    else:
        sleep(60)
