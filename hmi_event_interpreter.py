class HMIEventInterpreter:
    def __init__(self, hmi_event_handler):
        self.hmi_event_handler = hmi_event_handler
        self.wheel = 0

    def handle_event(self, event):
        if(event[0] == 1):
            wheeldiff = event[6] - self.wheel
            if(wheeldiff != 0 ):
                if(wheeldiff > 8):
                    wheeldiff = -1
                if(wheeldiff < -8):
                    wheeldiff = 1
                if(wheeldiff > 0):
                    self.hmi_event_handler.wheelRight()
                else:
                    self.hmi_event_handler.wheelLeft()
                self.wheel = event[6]
            if(event[2] == 8):
                print("nav_right button")
            if(event[2] == 32):
                print("nav_left button")
            if(event[2] == 16):
                print("nav_down button")
            if(event[2] == 128):
                print("nav_up button")
            if(event[2] == 64):
                print("back button")
            if(event[2] == 1):
                print("stop button")
            if(event[2] == 2):
                print("rec button")
            if(event[2] == 4):
                print("play button")
            if(event[1] == 1):
                self.hmi_event_handler.wheelButton()
            if(event[1] == 32):
                print("instance button")
            if(event[1] == 16):
                print("browse button")
            if(event[1] == 4):
                print("enter button")
            if(event[3] == 1):
                print("shift button")
            if(event[3] == 128):
                print("ffw button")      
            if(event[3] == 64):
                print("rwd button") 
            if(event[3] == 8):
                print("loop button")
