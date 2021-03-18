import cv2, numpy as np, collections
#import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


class fallAction:
    init = False
    detectedAngles = collections.deque(5*[0], 5)
    

    def check(self, angle):
        if not self.init:
            print(angle)
            
            if angle == None:
                print("angle = None")
                angle=0
            
            self.detectedAngles.appendleft(angle)
            #print(self.detectedAngles)S
            
            
        if all(i >= 70 for i in self.detectedAngles) and all(i <= 100 for i in self.detectedAngles):
            #winsound.Beep(frequency, duration)
            print("!!!!!!!!!!! FALL DETECTED !!!")