"""

## Senex Module for Pygame

- Every Functions need to be setted in a cicle loop
- Thanks for dowloading this file!

"""

import pygame

#TO DO add Player Component

def RGBToHex(r, g, b):
    """

# RGB to Hex
--------
## Args:
    r (int): 0 <--> 255
    g (int): 0 <--> 255
    b (int): 0 <--> 255

--------
### Returns:
    str: #000000 <--> #FFFFFF
"""
    
    return '#%02X%02X%02X' % (r, g, b)

def hex2rgb(color):
    """
# Hex to RGB
--------
## Args:
    color (str): #000000 <--> #FFFFFF

--------
### Returns:
    tuple[0:2]: int: 0 <--> 255
"""
    
    
    hex = color.lstrip('#')
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def colored(color, text):
    """
# Colored
--------

### Returns:
    colored str
"""


    import matplotlib.colors as mcol
    
    rgb = mcol.to_hex(color) if color in mcol.cnames.keys() or type(color) != tuple else color
    if type(rgb) != tuple: rgb = hex2rgb(rgb)
    
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(rgb[0], rgb[1], rgb[2], text)


GE = None
AM = None
Inputs = list()

class GameManager():
    """       
# Defaults
--------        
### Make an instance of this class to allow this module to work properly

----------------------------------------------------------------------------------------
- easy way to access a very common used function of pygame"""
    
    def __init__(self, window_resolution: tuple, screen_num: int = 4, fps: int = 30, screen_molt: float = 1.0, time_molt = 1, minmax_res: tuple = (1, 2), actual_resmolt: int = 1):
        """       
# Defaults
--------        
### Make an instance of this class to allow this module to work properly

----------------------------------------------------------------------------------------
- easy way to access a very common used function of pygame"""


        import traceback, pygame
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        
        def_name = text[:text.find('=')].strip()
        self.__setClass(def_name)
        
        # Errori
        GE.__CheckErrors(GameManager, def_name, 0)
        GE.__CheckErrors(window_resolution, def_name, 1)
        
        a = screen_molt
        b = time_molt
        
        
        import time
        
        self.__screenNum = screen_num
        self.__minHW = window_resolution[0] * minmax_res[0], window_resolution[1] * minmax_res[0]
        self.__maxHW = window_resolution[0] * minmax_res[1], window_resolution[1] * minmax_res[1]
        
        self.__dfWH = pygame.display.Info().current_w, pygame.display.Info().current_h
        
        self.__origDfWH = self.__dfWH[0] / self.__screenNum, self.__dfWH[1] / self.__screenNum
        
        self.__df_fps = fps
        self.__df_molt = screen_molt

        self.__div = int(self.__df_molt) if not int(self.__df_molt/2) else 0
        self.__prec_molt = 1
        self.__screen_molt = 1
        self.__created = True
        self.__window_resolution = window_resolution
        
        self.setScreenMolt(a)
        self.setTimeMolt(b)
        self.setScreenResolution((window_resolution[0] * screen_molt, 
                                  window_resolution[1] * screen_molt))
        self.setFps(fps)
        
        self.__last_time = time.time()
        self.__delta_time = 1
        
        self.__Ticks = 0
        self.__clock = self.getClock()
        
        c = actual_resmolt if actual_resmolt > 0 and actual_resmolt <= self.__screenNum else 1
        self.setMultipliers(c)
        
        self.__mouse_pos = tuple
        
        self.__Debug = False
        
        self.__list_textDebug = list()
        self.__printLine = list()
        self.__list_BannedElement = list()
        self.__delay_dis = list()
        self.__list_seconds = list()
        self.__num_print = 0
        self.__show_console = False
        
        self.__myfunct = None
        self.Event = None
        self.__line = ""
        self.Global_variables = dict()
        
        self.__Log()
        
        
    def __setClass(self, name):
        global GE
        GE = self
        
        def_name = "Defaults"
        if GE == self:
            
            t = "\n"+str(GE.__class__.__name__)+"() --> "+str(name)+" | class created correctly!\n"
            c = "#7ccbaa"
            print(colored((c), t))
            pygame.mixer.pre_init()
            pygame.init()
            
            print(colored(("#53754d"), "____________\n"))
            print(colored(("#53754d"), "DEBUG: \n\n"))
        return def_name
        
        
        
    def __Log(self):
        self.__debug_pos = self.getScreenResolution()[0] - 135 * self.getScreenMolt(), 0
        self.__debug_distance_line = 80 * self.getScreenMolt(), 20 * self.getScreenMolt()
        
        
        self.__bg_debug = "#383434"
        
        self.__debug_print = PrintLine( 
                    size = 14,
                    colorshadow="#369124",
                    color="#3ebd25",
                    backgroundcolor= self.__bg_debug,
                    defaultText = "Debug - Text:".upper(),
                    shadowdistance= 5,
                    alignment="left"
                
                )
        
        self.__debug_pos = (self.getScreenResolution()[0] - self.__debug_print.getLineSize()[0], 0)
        self.__debug_print.setPos(self.__debug_pos)
        
    
    def ShowConsole(self, flag: bool = None):
        if self.__Debug:
            self.__show_console = flag if flag != None else not self.__show_console
    
    def ShowDebug(self, flag: bool = None):
        self.__Debug = flag if flag != None else not self.__Debug
        
    def __getStateDebug(self):
        return self.__Debug
    
    def __destroyLastElement(self):
        if len(self.__list_textDebug) > 0:
            if self.__line in self.__list_textDebug:
                self.__list_BannedElement.append(self.__line)
                
    def isDebugging(self):
        return self.__Debug
    
    def ConsoleLog(self, text, text_color: str = None, backgroundColor: str = None, size: str = 5, haslife = True, timelife: float = 8.0):
        if self.__show_console:
            t = text if text != None else "Invalid Text input"
            c = text_color if text_color != None else "Green"
            b = backgroundColor if backgroundColor != None else None
            
            import traceback
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            
            text = "".join(text.split())
            def_name = text[:text.find(',')].strip().split("Log(")[1]
            
            if "text" in text:
                def_name = text[:text.find(',')].strip().split("text=")[1].strip("\"")
                
            order = 0
            if def_name in self.__list_textDebug:
                order = self.__list_textDebug.index(def_name) + 1
            
            if len(self.__delay_dis) >= order + 1: 
                self.__delay_dis[order - 1] = Delay(timelife, self.__destroyLastElement)
            else:
                self.__delay_dis.append(Delay(timelife, self.__destroyLastElement))
        
        
            line = PrintLine(   
                                pos = (0, order+1),
                                colorshadow="Black",
                                backgroundcolor = b,
                                color = c,
                                size = size,
                                defaultText = t,
                                shadowdistance= 4,
                                alignment="left"
                            
                            )
            
            pos = (self.getScreenResolution()[0] - self.__debug_print.getLineSize()[0]/2 - line.getLineSize()[0]/2,
                        line.getPos()[1] * self.__debug_distance_line[1] - self.__debug_distance_line[1])
            
            line.setPos(pos)
            
            delay = self.__delay_dis[order - 1]
        
            
            seconds = PrintLine(
                
                                pos = (0, order+1),
                                colorshadow="Black",
                                color = "#6c6a7b",
                                size = size,
                                shadowdistance= 4,
                                defaultText = str(delay.getRemaining()) + " sec",
                                alignment="left"
                            )
            
            seconds.setPos((self.getScreenResolution()[0] - seconds.getLineSize()[0], 
                            pos[1]))
            
            
            line_number = "- line: " + str(line_number)
            
            number_line = PrintLine(
                
                                pos = (0, order+1),
                                colorshadow="#c5c529",
                                color = "#f9f931",
                                size = size,
                                shadowdistance= 4,
                                defaultText = line_number,
                                alignment="left"
                            
                            )
            
            number_line.setPos((self.__debug_pos[0], 
                                pos[1]))
            
            
            if len(self.__printLine) > self.__num_print:
                self.__num_print = len(self.__printLine)
            
            
            if self.__list_textDebug.count(def_name) > 1 or def_name in self.__list_BannedElement:
                
                if def_name in self.__list_textDebug:
                    self.__printLine.pop(self.__list_textDebug.index(def_name))
                    self.__list_seconds.pop(self.__list_textDebug.index(def_name))
                    self.__list_textDebug.remove(def_name)
            
            elif self.__list_textDebug.count(def_name) <= 1:
                self.__list_textDebug.append(def_name)
                self.__printLine.append(line)
                
                self.__list_seconds.append([seconds, delay, haslife, number_line, line_number])
            
            
            if haslife:
                if def_name in self.__list_textDebug:
                    self.__line = def_name
                    
                    for delay in self.__delay_dis:
                        delay.Start()
        
    def __DebugWindow(self):
        
        color = "Green" if self.getActualFps() >= self.getFps() / self.getTimeMolt() else "Red"
        
        
        VIEW = PrintLine(
                    pos = (0,0), 
                    color = "White",
                    size = 10,
                    backgroundcolor = "#88883c",
                    alignment="left"
                
                )
        
        VIEW.Print("Resolution: "+str(self.getScreenResolution()[0])+"x"+str(self.getScreenResolution()[1]))
        
        
        SCREEN_MOLT = PrintLine(
                    pos = (0, VIEW.getPos()[1] + VIEW.getLine().get_size()[1]), 
                    color = "White",
                    size = 8,
                    backgroundcolor = "#2d8f9a",
                    alignment="left"
                
                )
        
        SCREEN_MOLT.Print("Screen Molt: "+str(self.getScreenMolt()))
        
        
        FPS = PrintLine(
                    pos = (VIEW.getPos()[0] + VIEW.getLine().get_size()[0], VIEW.getPos()[1]), 
                    color = "White",
                    size = 10,
                    backgroundcolor = color,
                    alignment="left"
                
                )
        
        FPS.Print("FPS: "+str(self.getActualFps(2)))
        
        
        TIME_MOLT = PrintLine(
                    pos = (FPS.getPos()[0], FPS.getPos()[1] + FPS.getLine().get_size()[1]), 
                    color = "White",
                    size = 8,
                    backgroundcolor = "#4d6aa3",
                    alignment="left"
                
                )
        
        TIME_MOLT.Print("Time Molt: "+str(self.getTimeMolt()))
        
        
        if self.__show_console:
            self.__Log()
            
            if len(self.__printLine) > 0:
                
                size = self.__debug_print.getLine().get_rect()
                rect = pygame.Rect(self.__debug_pos[0], self.__debug_pos[1], size[2], ((self.__debug_distance_line[1]/2) * (self.__num_print + 1)) * 2)
                pygame.draw.rect(self.getScreen(), self.__bg_debug, rect)
                self.__debug_print.Print()
            
            self.__debug_pos = (self.getScreenResolution()[0] - self.__debug_print.getLineSize()[0], 0)
            self.__debug_print.setPos(self.__debug_pos)
                
                
            for line in self.__printLine:
                line.Print()
                
            for line in self.__list_seconds:
                if line[2]:
                    line[0].Print(str(line[1].getRemaining()) + " sec")
                    
                line[3].Print(line[4])
                
        
    def Quit(self):
        import sys
        
        print(colored(("#fb3f3f"), "\n--- Exit from the program ---"))
        pygame.quit()
        sys.exit()
        
    def getClock(self):
        return pygame.time.Clock()
    
    def getCenterScreen(self):
        return tuple(ris/2 for ris in self.getScreenResolution())
    
    def getDivisorScreen(self, divisor):
        return tuple(ris/divisor for ris in self.getScreenResolution())
    
    def CheckComands(self, funct: classmethod = None):
        self.__myfunct = funct if funct != None else None
    
    def setFullScreen(self):
        self.__screen_molt = self.__screenNum - 1
        self.setMultipliers(screen_multiplier = self.__screenNum)
        
    def getMousePos(self):
        return self.__mouse_pos
        
    def Update(self):
        """ 

# Update
----------------------------------------------------------------------------------------
- Used to update the screen


"""     
        import time, pygame, sys
        self.__delta_time = time.time() - self.__last_time
        self.__delta_time *= self.getFps()
        self.__last_time = time.time()
        
        self.__mouse_pos = pygame.mouse.get_pos()

        self.__Ticks += 1 / self.getFps()
        if int(self.__Ticks) > 1000:
            self.__Ticks = 0
            
        if AM != None:
            for name in list(AM.Volume.keys()):
                AM.setVolume(name, AM.getVolume(name))
            
        if self.__getStateDebug():
            self.__DebugWindow()
            
        pygame.display.flip()
        self.__clock.tick(self.getFps())
            
        
        for event in pygame.event.get():
            self.Event = event
            
            if event.type == pygame.KEYDOWN:
                for input in Inputs:
                    functions = list(input.ReturnKeys().keys())
                    for func in functions:
                        input.Check(func, event.key)
            
            if self.__myfunct != None:
                self.__myfunct()
        
    def getTime(self):
        return pygame.time.get_ticks()
    
    def getDeltaTime(self):
        return self.__delta_time
    
    def getDelay(self):
        return self.__Ticks
    
    def getTicks(self):
        return (GE.getTime()//GE.getFps())
    
    def CheckTicks(self, milliseconds: float):
        """ 

# CheckTicks
----------------------------------------------------------------------------------------
- It's a way to have an infinite counter and ripetitive

----------------------------------------------------------------------------------------
### - Return: True/False

        IF Ticks / everyMillesec % 1 == 0 :
            return True
        return False


"""
        if round(self.getTicks()/milliseconds, 2) % 1 == 0:
            return True
        return False
    
    
    
    def setScreen(self, resolution, fullscreen = False):
        if fullscreen:
            self.__game_window = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
        else:
            pygame.display.init()
            self.__game_window = pygame.display.set_mode(resolution)
    
    def getScreen(self):
        return self.__game_window
        
    def setScreenResolution(self, pygame_display_screen_mode: tuple):
        var = pygame_display_screen_mode
        
        a = False
        if pygame_display_screen_mode >= self.__dfWH:
            var = self.__dfWH
            old_screen_res = (pygame_display_screen_mode[0] / self.getScreenMolt() + pygame_display_screen_mode[1] / self.getScreenMolt()) / 2
            screen_res = (var[0] / old_screen_res + var[1] / old_screen_res)//2
            self.setScreenMolt(screen_res)
            a = True
            
        if pygame_display_screen_mode <= self.__minHW:
            var = self.__minHW
            old_screen_res = (pygame_display_screen_mode[0] / self.getScreenMolt() + pygame_display_screen_mode[1] / self.getScreenMolt()) / 2
            screen_res = (var[0] / old_screen_res + var[1] / old_screen_res)//2
            self.setScreenMolt(screen_res)
        
        
        self.__window_resolution = var
        self.setScreen(self.__window_resolution, a)
        
    def getScreenResolution(self):
        return self.__window_resolution
    
    def setFps(self, var):
        self.__fps = var * self.getTimeMolt()
        
    def getFps(self):
        return self.__fps
    
    def getActualFps(self, round_value: int = 10):
        return round(self.__clock.get_fps(), round_value)
    
    def setScreenMolt(self, screen_multiplier: int):
        self.__prec_molt = self.__screen_molt if self.__created else self.__screen_molt * 1.3
        if self.__div and self.__created:
            self.__screen_molt = (2 / self.__div) / screen_multiplier
            self.__created = False
        else:
        
            self.__screen_molt = screen_multiplier
            if not self.__created:
                self.__screen_molt = screen_multiplier / 1.3
        
        
    def setMultipliers(self, screen_multiplier: int = 0, time_multiplier: int = 0, defaultfunctionReload: classmethod = None):
        
        s = screen_multiplier if screen_multiplier != 0 else self.getScreenMolt()
        d = time_multiplier if time_multiplier != 0 else self.getTimeMolt()
        
        w, h = self.__minHW 
        Temp_Res = (w * s, h * s)
        
        if Temp_Res > self.__dfWH:
            self.setScreenResolution((w * self.__screenNum, h * self.__screenNum))
            self.setScreenMolt(self.__screenNum)
            
        if s != self.getScreenMolt():
            self.setScreenResolution(Temp_Res)
            self.setScreenMolt(s if s <= self.__screenNum else self.__screenNum)
            
            if defaultfunctionReload != None: 
                defaultfunctionReload()
                print(colored("#384935","\n RESOLUTION --> "+str(self.getScreenResolution())+" | - Resolution of screen and of the components ( MOLT = "+str(self.getTimeMolt())+" ) has successfully been changed!\n"))
            else:
                print(colored("#384935","\n RESOLUTION --> "+str(self.getScreenResolution())+" | - Resolution of screen has successfully been changed!\n"))
            
            
        if d != self.getTimeMolt():
            self.setTimeMolt(d if d <= self.__screenNum else self.__screenNum)
            self.setFps(self.__df_fps)
            print(colored("#748071","\n FPS --> "+str(self.getFps())+" | - FPS have successfully been changed!\n"))
        
    def getScreenMolt(self):
        return round(self.__screen_molt, 2)
    
    def getIntScreenMolt(self):
        return int(self.__screen_molt)
    
    def getPrecScreenMolt(self):
        return self.__prec_molt
    
    def setTimeMolt(self, time_molt: int):
        self.__time_molt = time_molt
        
    def getTimeMolt(self):
        return self.__time_molt
    
    
    def __CheckErrors(self, var, nameclass: str, tipo: int):
        import sys
        # ERRORS
        
        if tipo == 0:
            try:
                var
            except ValueError:
                sys.exit(colored("#ff0000","\n"+"GameEngine | ValueRequired: You have to before make an istance of Defaults() to use correctly the engine"))
                
        elif tipo == 1:
            if type(var) != tuple:
                sys.exit(colored("#ff0000","\n"+str(nameclass)+" | ValueRequired: You have to set the Screen in Defaults() method"))
        

class Do():
    """ 

# DO
----------------------------------------------------------------------------------------
- Repeats a part of your code, tot times (specificated)
- You have before to make an istance "otside every cicles"

"""
    def __init__(self):
        """ 

# DO
----------------------------------------------------------------------------------------
- Repeats a part of your code, tot times (specificated)
- You have before to make an istance "otside every cicles"

"""
        self.__min = 0

    def Once(self, myfunction = None):
        """ 

# Once
----------------------------------------------------------------------------------------
- One time per your entire code and then it stops

"""
        return self.Times(myfunction, 1)

    def Times(self, myfunction = None, times = 2):
        """ 

# Times
----------------------------------------------------------------------------------------
- Tot times per your entire code and then it stops

"""
        if self.__min < times:
            self.__min += 1
            if myfunction != None: myfunction()
            return True
        return False

class Flip_Flop():
    """ 

# Flip_Flop
----------------------------------------------------------------------------------------
- Repeats a part of your code, ON/OFF per times (specificated)
- You have before to make an istance "otside every cicles"

"""
    def __init__(self):
        """ 

# Flip_Flop
----------------------------------------------------------------------------------------
- Repeats a part of your code, ON/OFF per times (specificated)
- You have before to make an istance "otside every cicles"

"""
        self.__min = 0
        
        
    def AfterOnce(self, myfunction = None):
        """ 

# AfterOnce
----------------------------------------------------------------------------------------
- One time is ON and then OFF

"""
        return self.AfterTimes(myfunction, 1)

    def AfterTimes(self, myfunction = None,  times = 2):
        """ 

# AfterOnce
----------------------------------------------------------------------------------------
- Tot times specificated is on state ON and then OFF

"""
        if self.__min < times:
            self.__min += 1
            return False
        else:
            if myfunction != None: myfunction()
            self.__min = 0
            return True

class Delay():
    """ 

# Delay
----------------------------------------------------------------------------------------
- To make events or recall function after tot time in a cicle
- You have before to make an istance "otside every cicles"

"""
    def __init__(self, sec, myfunction = None):
        """ 

# Delay
----------------------------------------------------------------------------------------
- To make events or recall function after tot time in a cicle

"""
        self.__FPS = GE.getFps()
        self.__min = 0 
        self.__max = sec * self.__FPS
        self.__increment = 1
        self.__function = myfunction
        self.__flag = True
        
    def getActualSecond(self):
        return self.__min // self.__FPS

    def getMaxSecond(self):
        return self.__max/self.__FPS

    def getRemaining(self):
        return self.getMaxSecond() - self.getActualSecond()

    def Start(self):
        """ 

# Start
----------------------------------------------------------------------------------------
- To start the delay 
- #### Once it will be finished it would be off

"""
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                if self.__function != None: self.__function()
                self.__flag = False

    def ReStart(self):
        """ 

# Restart
----------------------------------------------------------------------------------------
- To Restart the delay
- #### Once it will be finished it would be off

"""
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    def Infinite(self):
        """ 

# Infinite
----------------------------------------------------------------------------------------
- Start --> Restart --> Start ...
- #### Once it is finished, it will restart again by 0


"""
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/self.__FPS, self.__max/self.__FPS, self.__function))

class Timer():
    """ 

# Timer
----------------------------------------------------------------------------------------
- Timer in pygame
- ### You have before to make an istance "otside every cicles"
- #### Default state: countdown (change -> reversed value)

"""
    def __init__(self, time: tuple = (0, 0), molt_sec = 1,  myfunction = None, pos = None, size = 20, color = 'Black', font = 'freesansbold.ttf', reversed: bool = True, removeEvents: bool = True):
        """ 

# Timer
----------------------------------------------------------------------------------------
- Timer in pygame
- ### You have before to make an istance "otside every cicles"
- #### Default state: countdown (change -> reversed value)

"""


        self.__pos = pos
        if pos != None and type(pos) == tuple: self.__pos = pos

        self.__max_min = time[0]
        self.__max_sec = time[1] * GE.getFps()

        self.setTime(0, 0)
        if reversed:
            self.setTime(time[0], time[1])
            if time[0] == 0 and time[1] == 0: self.setTime(time[0], 1)

        self.__decrement = molt_sec
        self.__mainfunction = myfunction
        self.__flag = True
        self.__color = color
        self.__font = font
        self.__size = size * int(GE.getScreenMolt() + 0.9)
        self.__reversed = reversed
        self.__do = Do()
        self.__listfunctions = []
        self.__destroyfunctions = removeEvents
        self.__cicles = self.getTime()[0] * GE.getFps() * 60 + self.getTime()[1] * GE.getFps()
        self.__maxCicles = 0 if self.__reversed else (self.__max_min * GE.getFps() * 60 + self.__max_sec)

        self.__CheckTimerText()


    def __CheckTimerText(self):
        if self.__getSeconds() < 10:
            self.__text2 = ":0"
        else:
            self.__text2 = ":"

        if self.__getMinutes() < 10:
            self.__text1 = "0"
        else:
            self.__text1 = ""

    def AddEvent(self, time: tuple, myfunction: classmethod):
        """ 

# AddEvent
----------------------------------------------------------------------------------------
- Add a function in a selected period of time
- #### Once it is finished, Default --> delete event (editable)

"""
        if not (time, myfunction) in self.__listfunctions: self.__listfunctions.append((time, myfunction))

    def Start(self):
        """ 

# Start
----------------------------------------------------------------------------------------
- To start the timer
- #### Once it will be finished, it would be off

"""

        for event in self.__listfunctions:
            if self.getTime() == event[0]:
                
                self.__do.Once(lambda: event[1]())
                self.__do = Do()
                
                if self.__destroyfunctions and event in self.__listfunctions:
                    self.__listfunctions.pop(self.__listfunctions.index(event))

        if self.__flag and not self.IsOver():
            value =  60 * GE.getFps()
            if self.__reversed:

                self.__seconds -= (self.__decrement * GE.getDeltaTime()) / GE.getTimeMolt()
                self.__cicles -= (self.__decrement * GE.getDeltaTime()) / GE.getTimeMolt()

                if self.__seconds <= 0:
                    self.__seconds = value
                    self.__minutes -= 1
            else:

                self.__seconds += (self.__decrement * GE.getDeltaTime()) / GE.getTimeMolt()
                self.__cicles += (self.__decrement * GE.getDeltaTime()) / GE.getTimeMolt()
    
                if self.__seconds > value:
                    self.__seconds = 0
                    self.__minutes += 1


            self.__CheckTimerText()

        else:
            if self.__mainfunction != None: self.__do.Once(self.__mainfunction)
            self.Pause()

    def ReStart(self):
        """ 

# Restart
----------------------------------------------------------------------------------------
- To Restart the timer
- #### Once it will be finished, it would be off


"""
        if not self.__flag:
            self.__flag = True
            self.__minutes = self.__max_min

    def Pause(self):
        """ 

# Pause
----------------------------------------------------------------------------------------
- To set it in pause mode

"""
        self.__flag = False

    def DePause(self):
        """ 

# Depause
----------------------------------------------------------------------------------------
- To set it a depause mode, so to continue

"""
        self.__flag = True

    def AddSeconds(self, secs):
        """ 

# AddSeconds
----------------------------------------------------------------------------------------
- Function that allows to add seconds (+/-) on the timer
- #### Automatically converts seconds into minutes

"""     

        # Ripristino il DO()
        
        self.__do = Do()
        min = 60
        tot = round(self.__getSeconds() + secs, 3)

        if tot >= min or tot < 0:
            
            if secs < 0:
                parse_value = -0.999
            else:
                parse_value = +0.999

            self.__minutes += int(secs/min + parse_value)
            
            # PROPORZIONE

            # (secondi passati * time_molt) / totaleFPS --> per ottenere il moltiplicatore
            molt = int(secs / GE.getFps() * GE.getDeltaTime())

            # secondi passati - moltiplicatore * totale di sec in un minuto --> per ottenere i secondi da aggiungere al timer
            # (in caso rimanesse la somma sotto al minuto)
            var = secs - (molt * min)

            # (secondi attuali + secondi da aggiungere) - totale sec in un minuto --> per settare i secondi al timer
            # (in caso la somma e' superiore al minuto)
            d = (self.__getSeconds() + var) - min
            
            self.__seconds += var

            if self.__getSeconds() > min:
                self.__seconds = d
    
        else:
            self.__seconds += secs
    
        if self.__getSeconds() > min + 1:
            self.__seconds = 0

        self.__CheckTimerText()
    
    def Stop(self):
        """ 

# Stop
----------------------------------------------------------------------------------------
- To stop the timer
- #### It will be start by the default value

"""
        self.__init__(self.__max_sec, self.__molt_sec, self.__mainfunction)

    def Show(self):
        """ 

# Show
----------------------------------------------------------------------------------------
- To show the timer as a pygame.font.render on game window
- ### Output --> pygame.font.render

"""
        text = pygame.font.Font(self.__font, self.__size).render((self.__text1+str(self.__getMinutes())+str(self.__text2)+str(int(self.__getSeconds()))), True, self.__color)
        if self.__pos == None: self.__pos = (GE.getScreen().get_width()/2 - text.get_width()/2, 35 * GE.getScreenMolt())
        GE.getScreen().blit(text, self.__pos)

    def ChangeTextColor(self, color):
        self.__color = color

    def ChangeTextSize(self, size):
        self.__size = size * int(GE.getScreenMolt() + 0.9)

    def ChangeTextFont(self, font):
        self.__font = font

    def __getSeconds(self):
        return round(self.__seconds / (GE.getFps() / GE.getTimeMolt()), 2)
        
    def __getMinutes(self):
        return self.__minutes

    def IsOver(self):
        if self.__reversed:
            if not int(self.__getMinutes()) and not int(self.__getSeconds()): return True 
            else: return False
        else:
            if int(self.__getMinutes()) == self.__max_min and int(self.__getSeconds()) == (self.__max_sec // GE.getFps()): return True 
            else: return False
        
    def getTime(self):
        """ 

# GetTime
----------------------------------------------------------------------------------------
- Returns a tuple of the actual minutes and seconds
- #### Return --> (minutes: int, seconds: int)

"""
        return (int(self.__getMinutes()), int(self.__getSeconds()))

    def setTime(self, minutes: int = None, seconds: int = None):
        """ 

# SetTime
----------------------------------------------------------------------------------------
- Set minutes, and seconds
- #### Parametres --> minutes: int, seconds: int

"""     
        self.__do = Do()
        if minutes != None and type(minutes) == int: self.__minutes = minutes
        if seconds != None and type(seconds) == int: self.__seconds = seconds * GE.getFps()

    def CheckTime(self, v: tuple = (0, 0)):
        """ 

# CheckTime
----------------------------------------------------------------------------------------
- Checks a tuple of the actual minutes and seconds with the tuple passed as parametrer
- ### IF (Timer.minutes: int, Timer.seconds: int) == (Parametrer.minutes: int, Parametrer.seconds: int)
- #### Returns: True/False

"""
        return True if self.getTime() == v else False

    def ActualState(self):
        if self.__flag:
            print("| Current Tick: %d | Function Tick: %d | Function: %s |" %(self.__cicles, self.__maxCicles, self.__mainfunction))

class PrintLine():
    """ 

# PrintLine
----------------------------------------------------------------------------------------
- it's a pygame.font.render but easier to set

"""
    def __init__(
                self, 
                pos = None, defaultText = "default text", alignment = "center", size = 25, 
                font = 'freesansbold.ttf', color = "Green", backgroundcolor = None, colorshadow = None, shadowdistance = 2, bordercolor = "Black", borderwidth = 1, 
                showborder = False, showpoints=False, showcoords=False
                
                ):
        """ 

# PrintLine
----------------------------------------------------------------------------------------
- it's a pygame.font.render but easier to set

"""
        self.__pos = pos
        self.__text = str(defaultText) 
        self.__size = size * int(GE.getScreenMolt() + 0.9)
        self.__alignment = alignment
        self.__font = font
        self.__color = color
        self.__bg = backgroundcolor
        self.__colorshadow = colorshadow
        self.__shadow_distance = shadowdistance
        self.__bordercolor = bordercolor
        self.__borderwidth = borderwidth * int(GE.getScreenMolt() + 0.9)
        self.__showborder = showborder
        self.__showpoints = showpoints
        self.__showcoords = showcoords
        
        if self.__pos == None: 
            self.__pos = GE.getScreenResolution()
        
        self.__line = pygame.font.Font(self.__font, self.__size).render((self.__text), True, self.__color, self.__bg)
    
    def setPos(self, pos: tuple = (0, 0)):
        self.__pos = pos if (0,0) != tuple else GE.getScreenResolution()
    
    def getPos(self):
        return self.__pos
    
    def setColor(self, color):
        self.__color = color
        
    def getColor(self):
        return self.__color
    
    def setSize(self, size):
        self.__size = size * GE.getIntScreenMolt()
    
    def getSize(self):
        return self.__size
    
    def getLineSize(self):
        return self.__line.get_size()

    def Print(self, text: str = None):
        """ 

# Print
----------------------------------------------------------------------------------------
- Pass every type of text
- ### No parametres = str "Default Value"

"""
        if text != None and type(text) == str: self.__text = str(text)
        self.__Print()


    def getLine(self):
        return self.__line


    def __Print(self):
        self.__line = pygame.font.Font(self.__font, self.__size).render((self.__text), True, self.__color, self.__bg)
        text = self.__line
        
        
        
        position = self.__pos
        point = self.__pos
        if self.__alignment == "center":
            position = (self.__pos[0]/2 - text.get_width()/2, self.__pos[1]/2 - text.get_height()/2)
            point = (self.__pos[0] + text.get_width()/2, self.__pos[1] + text.get_height()/2)
        elif self.__alignment == "end":
            position = (self.__pos[0] + text.get_width()/2, self.__pos[1])
            point = (self.__pos[0] + text.get_width(), self.__pos[1])
            
        
        if type(self.__colorshadow) == str:
            shadow = pygame.font.Font(self.__font, self.__size).render((self.__text), True, self.__colorshadow, self.__bg)
            distance = self.__shadow_distance * GE.getScreenMolt()
            
            GE.getScreen().blit(shadow, (position[0] + self.__size*distance/500, position[1] + self.__size*distance/200))
        
        GE.getScreen().blit(text, position)
        
        if self.__showborder:            
            pygame.draw.rect(GE.getScreen(), self.__bordercolor, pygame.Rect(position[0], position[1], text.get_width(), text.get_height()), self.__borderwidth)

        if self.__showpoints:
            pygame.draw.circle(GE.getScreen(), "Green", position, 5 * GE.getScreenMolt() * self.__size/36)
            pygame.draw.circle(GE.getScreen(), "Blue", (position[0] + text.get_width(), position[1] + text.get_height()), 5 * GE.getScreenMolt() * self.__size/36)
            pygame.draw.circle(GE.getScreen(), "Red", point, 3 * GE.getScreenMolt() * self.__size/36)
            
        if self.__showcoords:
            
            diff = 2
            size = self.__size//diff
            
            pos = (self.getPos()[0]//GE.getScreenMolt(), self.getPos()[1]//GE.getScreenMolt())
            dim  = (text.get_size()[0]//GE.getScreenMolt(), text.get_size()[1]//GE.getScreenMolt())
            
            coords = pygame.font.Font('freesansbold.ttf', size).render("pos: "+str(pos), True, "Black")
            dimensions = pygame.font.Font('freesansbold.ttf', size).render("dim: "+str(dim), True, "#383838")
            
            pygame.draw.circle(GE.getScreen(), "Black", position, 3 * GE.getScreenMolt() * self.__size/40)
            GE.getScreen().blit(coords, (position[0] + text.get_width()/2 - coords.get_width()/2, position[1] - text.get_height()/1.6))
            GE.getScreen().blit(dimensions, (position[0] + text.get_width()/2 - dimensions.get_width()/2, position[1] + text.get_height()*1.2))
        
# DA RIVEDERE
class Dialogue():
    """ 

# Dialogue
----------------------------------------------------------------------------------------
- It's a interface bar created for dialogues
- It's a sync class (so until it's not dead the other components won't update), but it allows you to pass a function that realoads itself
- ### You are free to change text when you want with Print() method
- #### You have before to make an istance "otside every cicles" and then set your preferences on the instance


"""
    def __init__(self, background: tuple = (180, 192, 212), pos: tuple = None, wh: tuple = None, vel_text: int = 3, show_flashing = True, size_char = 12, default_text = "This is an example of Dialogue", wordsperline = None, charmax = 140, text_color = "White", colorshadow = None, shadowdistance = 2, offset = 5, debug = False, updateFunction = None, escapeFunction = None):      
        """ 

# Dialogue
----------------------------------------------------------------------------------------
- It's a interface bar created for dialogues
- It's a sync class (so until it's not dead the other components won't update), but it allows you to pass a function that realoads itself
- ### You are free to change text when you want with Print() method
- #### You have before to make an istance "otside every cicles" and then set your preferences on the instance

"""
        import matplotlib.colors as mcol

        self.__ot = offset * GE.getScreenMolt()
        
        if wh == None: self.__wh = (GE.getScreenResolution()[0] - self.__ot * 2, 100 * GE.getScreenMolt())
        else: self.__wh = wh[0] * GE.getScreenMolt(), wh[1] * GE.getScreenMolt()
        
        if pos == None: self.__pos = (0 * GE.getScreenMolt() + self.__ot, GE.getScreenResolution()[1] - self.__wh[1])
        else: self.__pos = pos[0] * GE.getScreenMolt(), pos[1] * GE.getScreenMolt()
        
        self.__text = default_text
        self.__text_color = text_color
        
        if type(background) == tuple: self.__background = RGBToHex(background[0], background[1], background[2])
        else: self.__background = background if background in mcol.cnames.keys() else mcol.to_hex(background)
        
        self.__descr = ""
        self.__incr = vel_text / GE.getTimeMolt() * GE.getDeltaTime()
        self.__def_incr = self.__incr
        self.__delay = 0
        self.__sizechar = size_char if size_char > 0 else 12
        self.__classic_sizechar = 12
        self.__wordlimit = wordsperline
        if wordsperline == None or wordsperline < 2: self.__wordlimit = (8 * 2) - int((8 * size_char) / self.__classic_sizechar)
        self.__classic_wordlimit = 8
        self.__charmax = charmax
        self.__update_funct = updateFunction
        self.__escape_funct = escapeFunction
        self.__finished = False
        self.__flag = False
        self.__show_flashing = show_flashing
        self.__flag_flash = False
        self.__shadows = (colorshadow, shadowdistance)
        self.__debug = debug
        self.__distancex, self.__distancey = self.__wh[0] - 40 * GE.getScreenMolt(), 5 * GE.getScreenMolt()
        self.__do = Do()
        self.__flip_flop = Flip_Flop()
        
        self.__new_line = ""
        self.__flag_new = False
        
        self.__df_wordsperline = self.__wordlimit
        self.__df_sizechar = self.__sizechar
        
        self.__flag_format = False
        
        if type(self.__background) == str: self.__background = hex2rgb(self.__background)

        self.__rect = pygame.Rect(self.__pos[0], self.__pos[1], self.__wh[0], self.__wh[1])

    def Print(self, text: str):
        """ 

# Print
----------------------------------------------------------------------------------------
- Pass every type of text
- ### No parametres = str "Default Value"
- #### Char limit 400

"""
        
        self.__delay = 0
        self.__flag = False
        self.__finished = False
        
        if not self.__flag_format:
            self.__wordlimit = self.__df_wordsperline 
            self.__sizechar = self.__df_sizechar
        
        if text != "":
            self.__text = text
            
            c = 0
            for val in range(len(self.__text)):
                if self.__text[val] != " ":
                    c = val
                    break
                    
            self.__text = self.__text[c:]
            
        if len(self.__text) > self.__charmax:
            import traceback
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip().split(".")[0]
            length = len(self.__text) - self.__charmax
            self.__text = self.__text[:self.__charmax]
            c = "Yellow"
            t = "\nline "+str(line_number)+" | "+def_name+".Print(\"Your Text\") --> Note: Text shorten cause too long!! (-"+str(length)+" char)"
            self.__do.Once(lambda: print(colored(c, t)))
        
        self.__incr = self.__def_incr
        
        while not self.__finished:
            
            try:
                if self.__update_funct != None: self.__update_funct()
            except RecursionError:
                import sys
                raise RecursionError(colored("#ff0000", "\nRecursionError: You need to call Dialogue() class in another function to work properly!"))
            
            
            def comands():    
                if GE.Event.type == pygame.QUIT:
                    GE.Quit()
            
                if GE.Event.type == pygame.KEYDOWN:
                    if GE.Event.key == pygame.K_ESCAPE:
                        if self.__escape_funct != None: self.__escape_funct()
                    
                    if GE.Event.key == pygame.K_SPACE:
                        if self.__flag_new and self.__flag:
                            self.__flag_new = False
                            self.__finished = True
                            self.Print(self.__new_line)
                        
                        if self.__flag or self.__finished:
                            self.__finished = True
                            self.__flag_format = False
                        
                        self.__flag = not self.__flag
                        self.__incr = 18 / GE.getTimeMolt() * GE.getDeltaTime()
                        
                        
            GE.CheckComands(comands)
            self.__appendText()
        
            if not "." in self.__background and self.__background != None: 
                self.__dark = 20; self.__dark = (self.__dark, self.__dark, self.__dark); 
                self.__PrintBG()
            else: self.__PrintIM()
            
            GE.Update()
            
        self.__finished = False
            
        
    def __appendText(self):
        
        if self.__flip_flop.AfterTimes(times = 30 * GE.getTimeMolt() * GE.getDeltaTime()):
            self.__flag_flash = not self.__flag_flash
        
        if int(self.__delay) < len(self.__text): 
            self.__descr = self.__text[:int(self.__delay)+1]
        else:
            self.__descr = self.__text
        
        self.__delay += 10 / GE.getFps() * GE.getTimeMolt() * GE.getDeltaTime() * self.__incr

    def __PrintBG(self):
        pygame.draw.rect(GE.getScreen(), self.__background, self.__rect, 0, 4 * int(GE.getScreenMolt() + 0.9))
        pygame.draw.rect(GE.getScreen(), tuple(map(lambda i, j: abs(i - j), self.__background, self.__dark)), self.__rect, 2 * int(GE.getScreenMolt() + 0.9), 4 * int(GE.getScreenMolt() + 0.9))
        
        chiaro = (255 - self.__background[0], 255 - self.__background[1], 255 - self.__background[2])
        
        
        size = 22 * GE.getScreenMolt()
        pos = [
                (self.__rect[0] + self.__distancex + self.__ot, self.__rect[3] + self.__rect[1] + self.__distancey - self.__ot - size), 
                (self.__rect[0] + self.__distancex + self.__ot + size, self.__rect[3] + self.__rect[1] + self.__distancey - self.__ot - size),  
                (self.__rect[0] + self.__distancex + self.__ot + size/2, self.__rect[3] + self.__rect[1] + self.__distancey - self.__ot - size/3.5)
                
                ]
        
        chiaro_tri = tuple(map(lambda i, j: abs(i - j), self.__background, self.__dark))
        
        if self.__show_flashing and self.__flag_flash:
            pygame.draw.polygon(GE.getScreen(), tuple(map(lambda i, j: i + j//1.2, self.__background, chiaro)), pos)
            pygame.draw.polygon(GE.getScreen(), tuple(map(lambda i, j: i + j//1.6, chiaro_tri, chiaro)), pos, 2 * int(GE.getScreenMolt() + 0.9))
        
        self.__PrintTX()

    def __PrintIM(self):
        pass

    def __PrintTX(self):

        
        words = self.__text.split(" ")
        nword = len(words)
        
        nlines = (nword // self.__wordlimit) + 1
        
        
        wordsperline = []
        for j in range(len(words)):
            wordsperline.append(" ".join(words[self.__wordlimit*j:self.__wordlimit*(j+1)]))
        
        a = []
        b = []
        
        last_line = ""
        for i in range(nlines):    
            
            limS = len(wordsperline[i-1])
            limD = len(wordsperline[i])
            
            
            a.append(limS)
            b.append(limD)
            
            if i == 0:
                text_passed = self.__descr[ a[i] : b[i] ]
            else:
                text_passed = self.__descr[ sum(a[0:i+1]) : sum(b[0:i+1]) ]
                
            if len(text_passed) > 0:
                resto = 0
                
                for j in range(len(text_passed)):
                    if text_passed[j] == " " and i != 0:
                        resto = j + 1
                        break
                        
                text_passed = self.__descr[ sum(a[0:i+1])+resto : sum(b[0:i+1])+resto ]
            
            space_line = (7 + self.__sizechar) * GE.getScreenMolt()
            
            line = PrintLine(
                
                    pos = (self.__pos[0] + self.__ot*2, self.__pos[1] + self.__ot*2 + (space_line * i)), 
                    
                    alignment = "start", size = self.__sizechar, 
                    
                    color=self.__text_color, 
                    
                    colorshadow=self.__shadows[0], shadowdistance=self.__shadows[1],
                    
                    showborder=self.__debug, showpoints=self.__debug, showcoords=self.__debug
                    
                )
            
            if line.getPos()[1] < self.__pos[1] + self.__wh[1] - self.__ot*3 and line.getPos()[0] < self.__pos[0] + self.__wh[0]:
                line.Print(text_passed)
                last_line = text_passed
            else:
                self.__flag_new = True
                
            if line.getPos()[0] + line.getLine().get_width() + self.__ot*2 > self.__pos[0] + self.__wh[0]:
                            
                if self.__wordlimit - 1 >= 2:
                    self.__wordlimit -= 1

                
                self.__flag_format = True
        
        if last_line != "" and self.__flag_new and text_passed[-5:] != self.__text[-5:]: 
            self.__new_line = self.__text.split(last_line)[1]
        else:
            self.__flag_new = False
        
        if text_passed[-5:] == self.__text[-5:]:
            self.__flag = True

class InputKeys():
    """
# InputKeys
----------------------------------------------------------------------------------------
- A way to set InputKeys and assign them with a custom name
- #### You have before to make an istance "otside every cicles"

    """
    
    def __init__(self, isglobal: bool = False, debug: bool = False, ):
        """
# InputKeys
----------------------------------------------------------------------------------------
- A way to set InputKeys and assign them with a custom name
- #### You have before to make an istance "otside every cicles"

        """
        self.__dict = {}
        self.__functionDict = {}
        self.__do = Do()
        self.__NotfoundValues = []
        
        self.__debug = debug

        if isglobal:
            Inputs.append(self)
        
        import traceback
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        self.__def_name = text[:text.find('=')].strip()    
    
    def Add(self, name: str = "default", commandlist : list = [], function = None):
        """
# Add
----------------------------------------------------------------------------------------
- Add new InputKeys with a name
- ### Parametres -->  name: str = "default", commandlist : list = []

        """
        self.__dict[name.lower()] = commandlist if type(commandlist) == list else [commandlist]
        self.__functionDict[name.lower()] = (function if function != None else (lambda: print(colored("Red", "No function has been set yet!"), GE.ConsoleLog("No function has been set yet!", "Red"))) if self.__debug else None)
    
    def Check(self, name: str, key : classmethod, holded: bool = False):
        """
# Check
----------------------------------------------------------------------------------------
- Check the inputs with the name passed
- ### Parametres -->  name: str, key : classmethod
- #### Returns: True/False

        """
        key_pressed = pygame.key.name(key)
        key_holded = True if holded else bool(pygame.key.get_pressed().count(1))
        
        import traceback
        
        if not name.lower() in self.__NotfoundValues:
            self.__do = Do()
            
        if name.lower() in self.__dict.keys():
            if key_pressed in self.__dict[name.lower()] and key_holded:
                self.__functionDict[name.lower()]() if self.__functionDict[name.lower()] != None else 0
                
                if self.__debug:
                    t = " "+str(self.__def_name)+" | - " +str(name.lower())+" --> "+str(self.__functionDict[name.lower()].__name__)+"()\n"
                    c = "#6b4040"
                    print(colored(c, t))
                    GE.ConsoleLog(t, c)
                return True
            return False
        else:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            self.__do.Once(lambda: print(colored(("#faf676"),"\nline "+str(line_number)+" | "+str(def_name)+".Check("+name+") --> Note: name \""+name+"\" has not been registered!\n")))
            (self.__NotfoundValues.append(name.lower()) ) if name.lower() not in self.__NotfoundValues else 0
        
    def Remove(self, name: str):
        """
# Remove
----------------------------------------------------------------------------------------
- Remove an input from your inputs dict

        """
        if name in self.__dict.keys():
            self.__dict.pop(name.lower())
        
    def Clear(self):
        """
# Clear
----------------------------------------------------------------------------------------
- Restore your inputs dict

        """
        self.__dict.clear()
        
    def ReturnKeys(self, found: bool = True):
        """
# ReturnKeys
----------------------------------------------------------------------------------------
- Returns the dict of found/unfound values
- #### Return: self.__dict if found else self.__NotfoundValues

        """
        return self.__dict if found else self.__NotfoundValues
        

class AudioManager():
    def __init__(self, MaxVolume: int = 10, Default_Values: tuple = (5, 0)):
        self.setMaxVolume(MaxVolume)
        
        a = (Default_Values[0] * self.getMaxVolume() // 10)
        b = (Default_Values[1] * self.getMaxVolume() // 10) 
        
        self.__GvolumeS = a
        self.__GvolumeM = b
        
        self.Volume = {}
        self.Sounds = {}
        self.Music = {}
        
        global AM
        AM = self
        
        
    def getVolume(self, name):
        return self.Volume[name] if name in list(self.Volume.keys()) else None
        
    def setVolume(self, name: str, volume: int):
        if self.Volume[name] <= self.getMaxVolume() and volume <= self.getMaxVolume():
            
            if name in list(self.Sounds.keys()):
                self.Volume[name] = volume
                self.Sounds[name].set_volume(volume * self.__GvolumeS)
                return
                
            if name in list(self.Music.keys()):
                self.Volume[name] = volume
                self.Music[name].set_volume(volume * self.__GvolumeM)
                return
            
            
    def isMaxVolume(self, Value):
        return True if (not Value) or (Value == self.getMaxVolume()) else False
        
    def AddSound(self, name: str, path: list, volume: int = 1):
        
        self.Volume[name] = volume
        self.Sounds[name] = pygame.mixer.Sound(path)
        
        self.Sounds[name].set_volume(volume * self.__GvolumeS)
        
        
    def AddMusic(self, name: str, path: list, volume: int = 1):
        if name in list(self.Sounds.keys()):
            return
            
        self.Volume[name] = volume
        self.Music[name] = pygame.mixer.Sound(path)
        
        self.Music[name].set_volume(volume * self.__GvolumeM)
        
    def setGlobalVolumeSound(self, volume):
        self.__GvolumeS = volume
        
    def getGlobalVolumeSound(self):
        return self.__GvolumeS
    
    def setGlobalVolumeMusic(self, volume):
        self.__GvolumeM = volume
            
    def AddSoundVolume(self, volume):
        if self.__GvolumeS + volume <= self.getMaxVolume() and self.__GvolumeS + volume >= 0:
            self.__GvolumeS += volume
            self.__flagMaxVolume = False
    
    def AddMusicVolume(self, volume):
        if self.__GvolumeM + volume <= self.getMaxVolume() and self.__GvolumeM + volume >= 0:
            self.__GvolumeM += volume            
            self.__flagMaxVolume = False
        
    def getGlobalVolumeMusic(self):
        return self.__GvolumeM
        
    def setMaxVolume(self, volume):
        self.__MaxVolume = volume
        
    def getMaxVolume(self):
        return self.__MaxVolume

if __name__ != "__main__":
    print(colored(("#87CEEB"),"\r\nGameEngine 1.0 - Created by Senex03 || Welcome!!"))