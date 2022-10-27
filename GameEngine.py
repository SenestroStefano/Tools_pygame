from calendar import c
import pygame, sys, os

"""

--- Senex Module for Pygame ---

"""


"""DELAY IN PYGAME"""

FPS = 30
clock = pygame.time.Clock()

class Delay():
    def __init__(self, sec, event):
        self.__FPS = sec[1]
        self.__min = 0 
        self.__max = sec[0] * self.__FPS
        self.__increment = 1
        self.__function = event
        self.__flag = True

    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                self.__function()
                self.__flag = False

    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    def Infinite(self):
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/self.__FPS[1], self.__max/self.__FPS, self.__function))


class Delay_noEvent():
    def __init__(self, sec):
        self.__FPS = sec[1]
        self.__min = 0 
        self.__max = sec[0] * self.__FPS
        self.__increment = 1
        self.__flag = True

    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                self.__flag = False
                return True

        return False

    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    def Infinite(self):
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/self.__FPS, self.__max/self.__FPS, self.__function))


class DO():
    def __init__(self):
        self.__flagOnce = True
        self.__min = 0

    def Once(self, event):
        if self.__flagOnce:
            self.__flagOnce = False
            event()

    def Times(self, times, event):
        if self.__min < times:
            self.__min += 1
            event()


class FLIP_FLOP():
    def __init__(self):
        self.__flagOnce = False
        self.__min = 0


    def AfterOnce(self, event):
        if self.__flagOnce:
            self.__flagOnce = False
            event()
        else:
            self.__flagOnce = True

    def AfterTimes(self, times, event):
        if self.__min < times:
            self.__min += 1
        else:
            event()
            self.__min = 0

Do = DO()
FlipFlop = FLIP_FLOP()

def MiaFunzione():
    print("Ciao")

def testa():
    x = 0
    while True:


        #delay.ActualState()
        #lambda: print("Bella")
        FlipFlop.AfterTimes(20, lambda: print("Bella"+str(x)))
        x += 1


        clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    testa()