from logipy import logi_led
from threading import Thread
from time import sleep


class LEDControler():
    def __init__(self):
        logi_led.logi_led_init()
        sleep(1)
        self.device = "A"
        self.threads = {"K": Thread(), "M": Thread()}
        self.mouse_colour = {"R": 100, "G": 100, "B": 100}
        self.kb_colour = 100
        logi_led.logi_led_set_target_device(7)
        logi_led.logi_led_set_lighting(100, 100, 100)

    # Flashes KB light
    # Hidden method because it's used for threading
    def _flash_kb(self, onTime, offTime, cycles, defaultColour, k):
        for _ in range(cycles):
            sleep(offTime)
            self.set_colour("K", k)
            sleep(onTime)
            self.set_colour("K", defaultColour)

    # Flashes Mouse light
    # Hidden method because it's used for threading
    def _flash_mouse(self, onTime, offTime, cycles, defaultColour, r, g, b):
        for _ in range(cycles):
            sleep(offTime)
            self.set_colour("M", r, b, g)
            sleep(onTime)
            self.set_colour("M", defaultColour["R"],
                                 defaultColour["G"],
                                 defaultColour["B"])

    # Sets the device using Logitech's arbitrayr numbers
    # Nice to use one function for this instead of two
    # Anything that changes colour should request device, so this remains hidden
    def _set_device(self, device):
        device = device.upper()
        if device == "A":
            logi_led.logi_led_set_target_device(7)
        elif device == "K":
            logi_led.logi_led_set_target_device(1)
        elif device == "M":
            logi_led.logi_led_set_target_device(2)
        else:
            raise ValueError("Device must be 'A', 'K', or 'M'")
        self.device = device

    # Transitions KB light from one colour to another
    # Hidden method because it's used for threading
    def _transition_kb(self, duration, k):
        change = abs(self.kb_colour - k)
        for _ in range(change):
            if self.kb_colour < k:
                self.set_colour("K", self.kb_colour + 1)
            elif self.kb_colour > k:
                self.set_colour("K", self.kb_colour - 1)
            sleep(duration / change)

    # Transitions Mouse light from one colour to another
    # Hidden method because it's used for threading
    def _transition_mouse(self, duration, r, g, b):
        change = {"R": abs(self.mouse_colour["R"] - r),
                  "G": abs(self.mouse_colour["G"] - g),
                  "B": abs(self.mouse_colour["B"] - b)}
        wait = duration / sum(change.values())
        # Arbitrary order is one that needs to be changed the most first
        # Not the most elegant way to do this though
        order = [max(change.keys(), key=lambda key: change[key]),
                 None, min(change.keys(), key=lambda key: change[key])]
        for i in "RGB":
            if i not in order: order[1] = i
        current = 0
        for i in range(sum(change.values())):
            if order[current] == "R":
                if self.mouse_colour["R"] < r:
                    self.set_colour("M", self.mouse_colour["R"] + 1,
                                         self.mouse_colour["G"],
                                         self.mouse_colour["B"])
                elif self.mouse_colour["R"] > r:
                    self.set_colour("M", self.mouse_colour["R"] - 1,
                                         self.mouse_colour["G"],
                                         self.mouse_colour["B"])
            elif order[current] == "G":
                if self.mouse_colour["G"] < g:
                    self.set_colour("M", self.mouse_colour["R"],
                                         self.mouse_colour["G"] + 1,
                                         self.mouse_colour["B"])
                elif self.mouse_colour["G"] > g:
                    self.set_colour("M", self.mouse_colour["R"],
                                         self.mouse_colour["G"] - 1,
                                         self.mouse_colour["B"])
            elif order[current] == "B":
                if self.mouse_colour["B"] < b:
                    self.set_colour("M", self.mouse_colour["R"],
                                         self.mouse_colour["G"],
                                         self.mouse_colour["B"] + 1)
                elif self.mouse_colour["B"] > b:
                    self.set_colour("M", self.mouse_colour["R"],
                                         self.mouse_colour["G"],
                                         self.mouse_colour["B"] - 1)
            change = {"R": abs(self.mouse_colour["R"] - r),
                      "G": abs(self.mouse_colour["G"] - g),
                      "B": abs(self.mouse_colour["B"] - b)}
            for i in change:
                if change[i] == 0 and i in order:
                    order.remove(i)
            # Shouldn't be needed but function was sometimes looping afterwards
            if len(order) == 0:
                break
            # This method of increacing 'current' means it will work with any
            #  amount of options, meaning we can remove the ones that don't need
            #  to be changed anymore
            current += 1
            if current > len(order) - 1:
                current = 0
            sleep(wait)

    # Just a nicer way to get info from outside the class
    def get_device(self): return self.device
    def get_mouse_colour(self): return self.mouse_colour
    def get_kb_colour(self): return self.kb_colour

    # The methods 'flash_colour()' and 'transition_colour()' start threads,
    #  which allows the main program to continue, so you might need to use this
    #  to prevent new changes
    def is_thread_running(self):
        for i in self.threads:
            if self.threads[i].is_alive():
                return True
        return False

    # The methods 'flash_colour()' and 'transition_colour()' start threads,
    #  which allows the main program to continue, so you might need to use this
    #  to sync back up
    def wait_for_threads(self): 
        for i in self.threads:
            if self.threads[i].is_alive():
                self.threads[i].join()

    # Flashes the selected colour on the selected device
    # Will flash on for 'onTime' and off for 'offTime'
    # Will loop for 'cycles' cycles
    def flash_colour(self, device, onTime, offTime, cycles, *args):
        self._set_device(device)
        if len(args) == 3:
            r, g, b = args[0], args[1], args[2]
            k = max(r, g, b)
        elif len(args) == 1:
            if self.get_device() == "K":
                k = r = g = b = args[0]
            else:
                raise ValueError("Must have Keyboard selected to use just one argument for colour")
        else:
            raise ValueError("Invalid number of arguments")
        if self.device == "A":
            self.threads["K"] = Thread(target=self._flash_kb,
                                       args=(onTime, offTime, cycles,
                                             self.kb_colour, k))
            self.threads["K"].start()
            self.threads["M"] = Thread(target=self._flash_mouse,
                                       args=(onTime, offTime, cycles,
                                             self.mouse_colour, r, g, b))
            self.threads["M"].start()
        elif self.device == "K":
            self.threads["K"] = Thread(target=self._flash_kb,
                                       args=(onTime, offTime, cycles,
                                             self.kb_colour, k))
            self.threads["K"].start()
        elif self.device == "M":
            self.threads["M"] = Thread(target=self._flash_mouse,
                                       args=(onTime, offTime, cycles,
                                             self.mouse_colour, r, g, b))
            self.threads["M"].start()

    # Instantly sets the selected device to the selected colour
    # Will be overwritten if 'flash_colour()' or 'transition_colour()' is running
    def set_colour(self, device, *args):
        self._set_device(device)
        if len(args) == 3:
            r, g, b = args[0], args[1], args[2]
            k = max(r, g, b)
        elif len(args) == 1:
            if self.get_device() == "K":
                r = g = b = args[0]
            else:
                raise ValueError("Must have Keyboard selected to use just one argument for colour")
        else:
            raise ValueError("Invalid number of arguments")
        logi_led.logi_led_set_lighting(r, g, b)
        if self.device == "A":
            self.mouse_colour = {"R": r, "G": g, "B": b}
            self.kb_colour = max(self.mouse_colour.values())
        elif self.device == "K":
            self.kb_colour = max(r, g, b)
        elif self.device == "M": 
            self.mouse_colour = {"R": r, "G": g, "B": b}

    # Transitiopns from the current colour to the selected colour on the selected
    #  device over 'duration' seconds
    def transition_colour(self, device, duration, *args):
        self._set_device(device)
        if len(args) == 3:
            r, g, b = args[0], args[1], args[2]
            k = max(r, g, b)
        elif len(args) == 1:
            if self.get_device() == "K":
                k = r = g = b = args[0]
            else:
                raise ValueError("Must have Keyboard selected to use just one argument for colour")
        else:
            raise ValueError("Invalid number of arguments")
        if self.device == "A":
            self.threads["K"] = Thread(target=self._transition_kb,
                                       args=(duration, k))
            self.threads["K"].start()
            self.threads["M"] = Thread(target=self._transition_mouse,
                                       args=(duration, r, g, b))
            self.threads["M"].start()
        elif self.device == "K":
            self.threads["K"] = Thread(target=self._transition_kb,
                                       args=(duration, k))
            self.threads["K"].start()
        elif self.device == "M":
            self.threads["M"] = Thread(target=self._transition_mouse,
                                       args=(duration, r, g, b))
            self.threads["M"].start()


# Demonstration for if you launch the wrapper instead of importing it
if __name__ == "__main__":
    a = LEDControler()
    a.set_colour("A", 0, 0, 0)
    a.set_colour("M", 0, 75, 75)
    sleep(1)
    a.transition_colour("K", 5, 100)
    a.transition_colour("M", 5, 100, 0, 100)
    a.wait_for_threads()
    a.transition_colour("A", 5, 0, 0, 0)
    a.wait_for_threads()
    a.flash_colour("A", 0.25, 0.25, 10, 100, 0, 0)
    a.wait_for_threads()
    print("Done")
    sleep(3)
