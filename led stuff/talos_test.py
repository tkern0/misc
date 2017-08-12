import time
from wrapper import LEDControler

LOG_FILE = "D:\SteamLibrary\steamapps\common\The Talos Principle\Log\Talos.log"
LED = LEDControler()

with open(LOG_FILE, "w"): pass
log = open(LOG_FILE, "rb")

while True:
    latest_line = log.readline()[16:]
    if not latest_line:
        time.sleep(0.017)
    else:
        if latest_line.startswith(b"Picked: D"):
            LED.flash_colour("M", 0.25, 0.25, 3, 0, 0, 100)
        if latest_line.startswith(b"Picked: M"):
            # Colours are hard :|
            LED.flash_colour("M", 0.25, 0.25, 3, 100, 100, 50)
        if latest_line.startswith(b"Picked: N"):
            LED.flash_colour("M", 0.25, 0.25, 3, 100, 0, 0)
        if latest_line.startswith(b"Started simulation on 'Content/Talos/Levels/"):
            if latest_line[44:].startswith(b"Nexus.wld"):
                LED.set_colour("M", 0, 0, 0)
            if latest_line[44:].startswith(b"Cloud_1"):
                LED.set_colour("M", 100, 25, 0)
            if latest_line[44:].startswith(b"Cloud_2"):
                LED.set_colour("M", 75, 50, 0)
            if latest_line[44:].startswith(b"Cloud_3"):
                LED.set_colour("M", 50, 75, 0)
        if latest_line.startswith(b"USER: /eternalize"):
            LED.set_colour("M", 0, 25, 50)
            LED.flash_colour("M", 0.05, 0.05, 20, 50, 25, 75)