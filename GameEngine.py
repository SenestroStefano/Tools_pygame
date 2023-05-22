"""

## Senex Module for Pygame

- Every Functions need to be setted in a cicle loop
- Thanks for dowloading this file!

"""

import pygame

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


def text2rgb(color):
    """
# Text to RGB
--------

### Returns:
    tuple[0:2]: int: 0 <--> 255
"""
    import matplotlib.colors as mcol
    
    rgb = mcol.to_rgb(color) if color in mcol.cnames.keys() else KeyError("This color doesn't exist") 
    return rgb

def text2hex(color):
    """
# Text to HEX
--------

### Returns:
    str: #000000 <--> #FFFFFF
"""
    import matplotlib.colors as mcol
    
    rgb = mcol.to_hex(color) if color in mcol.cnames.keys() else KeyError("This color doesn't exist") 
    return rgb

def textcolor(color):
    import matplotlib.colors as mcol
    return True if color in mcol.cnames.keys() else False

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


def __clear(text, element):
    t = str(text)
    
    els = [x for x in element]
    for el in els:
        t = "".join(t.split(el))
    return t
    

def debug(*args, **kwargs):
    import traceback
    
    try:
        color = GE.DEBUG_COLOR
    except NameError:
        color = "#9fcc98"
        
    color2 = "#d4e066"
    
    (filename,line_number,function_name,text)=traceback.extract_stack()[-2]            
    text1 = colored(color2, "\n - line " + str(line_number)) + " | "
    (print(text1 + colored(color, __clear(args, "(),'"))) 
    if len(kwargs) == 0 
    else [print(text1 + colored(color, 
                                __clear((__clear(key, "=")+": " + 
                                            kwargs[key]), "(),'"))) for key in kwargs.keys()])


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
    
    def __init__(self, window_resolution: tuple = (0, 0), default_window_resolution: tuple = (0, 0), screen_num: int = 4, fps: int = 30, screen_molt: float = 1.0, time_molt = 1, minmax_res: tuple = (1, 2), actual_resmolt: int = 1, debug_color: str = "green"):
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
        
        a = screen_molt
        b = time_molt
        
        self.DEBUG_COLOR = RGBToHex(debug_color) if type(debug_color) == tuple else text2hex(debug_color) if not textcolor(debug_color) else debug_color 
        
        self.__screenNum = screen_num if screen_num != 0 else 1
        self.__dfWH = pygame.display.Info().current_w, pygame.display.Info().current_h
        win_res = window_resolution if window_resolution != (0, 0) else ([dim / self.__screenNum for dim in self.__dfWH])
        df_win_res = default_window_resolution
        
        # Errori
        GE.__CheckErrors(GameManager, def_name, 0)
        
        
        import time
        
        v = minmax_res[1] if self.__screenNum == minmax_res[1] else self.__screenNum
        self.__minWH = win_res[0] * minmax_res[0], win_res[1] * minmax_res[0]
        self.__maxWH = win_res[0] * v, win_res[1] * v
        
        self.__mindfWH = self.__dfWH[0] / self.__screenNum, self.__dfWH[1] / self.__screenNum
        
        
        self.__listofresolutions = [(win_res[0] * (n+1), win_res[1] * (n+1)) for n in range(self.__screenNum - 1)]
        self.__listofresolutions.append(self.__dfWH)
        
        self.__listofscreenmultiplayer = [(res[0] / (win_res[0] if df_win_res == (0, 0) else df_win_res[0]) + res[1] / (win_res[1] if df_win_res == (0, 0) else df_win_res[1]))/2 for res in self.__listofresolutions]
        
        
        self.__df_fps = fps
        self.__df_molt = screen_molt

        self.__div = int(self.__df_molt) if not int(self.__df_molt/2) else 0
        self.__prec_molt = 1
        self.__screen_molt = 1
        self.__created = True
        self.__window_resolution = win_res
        
        self.setScreenMolt(a)
        self.setTimeMolt(b)
        self.setScreenResolution((win_res[0] * screen_molt, 
                                  win_res[1] * screen_molt))
        self.setFps(fps)
        
        self.__last_time = time.time()
        self.__delta_time = 1
        
        self.__Ticks = 0
        self.__clock = self.getClock()
        
        c = actual_resmolt if actual_resmolt > 0 and actual_resmolt <= self.__screenNum else 1
        self.setMultipliers(c)
        
        self.__mouse_pos = tuple
        
        self.Debug = False
        
        self.__list_textDebug = list()
        self.__printLine = list()
        self.__list_BannedElement = list()
        self.__delay_dis = list()
        self.__list_seconds = list()
        self.__num_print = 0
        self.__show_console = False
        
        self.__myfunct = dict()
        self.__line = ""
        self.Global_variables = dict()
        
        self.__Log()
        
        self.Event = None
        self.Key_Pressed = False
        
        
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
        
    def getListofScreenMultiplayers(self):
        return self.__listofscreenmultiplayer
    
    def getListofScreenResolutions(self):
        return self.__listofresolutions
        
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
        if self.Debug:
            self.__show_console = flag if flag != None else not self.__show_console
    
    def ShowDebug(self, flag: bool = None):
        self.Debug = flag if flag != None else not self.Debug
        
    def __getStateDebug(self):
        return self.Debug
    
    def __destroyLastElement(self):
        if len(self.__list_textDebug) > 0:
            if self.__line in self.__list_textDebug:
                self.__list_BannedElement.append(self.__line)
                
    def isDebugging(self):
        return self.Debug
    
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
            if (def_name, line_number) in self.__list_textDebug:
                order = self.__list_textDebug.index((def_name, line_number)) + 1
            
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
            
            
            line_text = "- line: " + str(line_number)
            
            number_line = PrintLine(
                
                                pos = (0, order+1),
                                colorshadow="#c5c529",
                                color = "#f9f931",
                                size = size,
                                shadowdistance= 4,
                                defaultText = line_text,
                                alignment="left"
                            
                            )
            
            number_line.setPos((self.__debug_pos[0], 
                                pos[1]))
            
            
            if len(self.__printLine) > self.__num_print:
                self.__num_print = len(self.__printLine)
            
            
            if self.__list_textDebug.count((def_name, line_number)) > 1 or (def_name, line_number) in self.__list_BannedElement:
                
                if (def_name, line_number) in self.__list_textDebug:
                    self.__printLine.pop(self.__list_textDebug.index((def_name, line_number)))
                    self.__list_seconds.pop(self.__list_textDebug.index((def_name, line_number)))
                    self.__list_textDebug.remove((def_name, line_number))
            
            elif self.__list_textDebug.count((def_name, line_number)) <= 1:
                self.__list_textDebug.append((def_name, line_number))
                self.__printLine.append(line)
                
                self.__list_seconds.append([seconds, delay, haslife, number_line, line_number])
            
            
            if haslife:
                if (def_name, line_number) in self.__list_textDebug:
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
                pygame.draw.rect(self.getScreen(), self.__bg_debug, rect, 0, 4)
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
        import traceback, pygame
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        
        def_name = text[:text.find('=')].strip().split("(")[1]
        
        if not def_name in self.__myfunct.keys():
            self.__myfunct[def_name] = funct if funct != None else None

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
            
            
            
            if len(list(self.__myfunct.items())) > 0:
                
                try:
                    for function in list(self.__myfunct.values()):
                        function()
                except RuntimeError:
                    pass
            
            if event.type == pygame.KEYDOWN:
                self.Key_Pressed = True
                for input in Inputs:
                    functions = list(input.ReturnKeys().keys())
                    for func in functions:
                        input.Check(func, event.key)
            
            if event.type == pygame.KEYUP:
                self.Key_Pressed = False
            
        
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
            a = True
        
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
        self.__prec_molt = self.__screen_molt
        self.__screen_molt = screen_multiplier
        
        
    def setMultipliers(self, screen_multiplier: int = 0, time_multiplier: int = 0, defaultfunctionReload: classmethod = None):
        
        s = int(screen_multiplier) if screen_multiplier != 0 else self.getIntScreenMolt()
        d = time_multiplier if time_multiplier != 0 else self.getTimeMolt()
        
        w, h = self.__minWH 
        Temp_Res = (w * s, h * s)
            
        if s != self.getScreenMolt():
            if s-1 < len(self.__listofresolutions):
                self.setScreenMolt(self.__listofscreenmultiplayer[s-1])
                self.setScreenResolution(self.__listofresolutions[s-1])
            
        if defaultfunctionReload != None: 
            defaultfunctionReload()
            print(colored("#384935","\n RESOLUTION --> "+str(self.getScreenResolution())+" | - Resolution of screen and of the components ( MOLT = "+str(self.getScreenMolt())+" ) has successfully been changed!\n"))
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



__every_sec = Flip_Flop()
def print_every_second(*args, **kwargs):
    __every_sec.AfterTimes(lambda: print(*args, **kwargs), GE.getFps())


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
        self.__pause = False
        
    def getActualSecond(self):
        return self.__min // self.__FPS

    def getMaxSecond(self):
        return self.__max/self.__FPS

    def getRemaining(self):
        return self.getMaxSecond() - self.getActualSecond()

    def Pause(self):
        """ 

# Pause
----------------------------------------------------------------------------------------
- To pause the delay (set stand by the delay)

"""
        self.__pause = False

    def UnPause(self):
        """ 

# UnPause
----------------------------------------------------------------------------------------
- To Remove the pause state

"""
        self.__pause = True

    def Start(self):
        """ 

# Start
----------------------------------------------------------------------------------------
- To start the delay 
- #### Once it will be finished it would be off

"""
        if self.__flag or not self.__pause:
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

                self.__seconds -= self.__decrement * GE.getDeltaTime()
                self.__cicles -= self.__decrement * GE.getDeltaTime()

                if self.__seconds <= 0:
                    self.__seconds = value
                    self.__minutes -= 1
            else:

                self.__seconds += self.__decrement * GE.getDeltaTime()
                self.__cicles += self.__decrement * GE.getDeltaTime()
    
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

    def UnPause(self):
        """ 

# UnPause
----------------------------------------------------------------------------------------
- To set it a unpause mode, so to continue

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
            
            self.__seconds += var * GE.getFps()

            if self.__getSeconds() > min:
                self.__seconds = d * GE.getFps()
    
        else:
            self.__seconds += secs * GE.getFps()
    
        if self.__getSeconds() > min + 1:
            self.__seconds = 0

        self.__cicles = self.getTime()[0] * GE.getFps() * 60 + self.getTime()[1] * GE.getFps()
        
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
        return round(self.__seconds / GE.getFps(), 2)
        
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

    def ActualState(self, every_tick: bool = False):
        if self.__flag:
            text = colored("#ffd723", "\tTimer -> ") + colored("#65ff3e","Current Tick: %d | Function Tick: %d | Function:%s |" %(self.__cicles, self.__maxCicles, str(self.__mainfunction).split("<")[1].rstrip(".").lstrip("function")))
            print(text) if every_tick else print_every_second(text)

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
    def __init__(self, background: tuple = (180, 192, 212), pos: tuple = None, wh: tuple = None, vel_text: int = 3, show_flashing: bool = True, triangle_size = 22, offset_text: tuple = (0, 0), offset_triangle: tuple = (0, 0), offset: int = 5, size_char = 12, default_text = "This is an example of Dialogue", font : str = "freesansbold.ttf", wordsperline = None, charmax = 140, text_color = "White", colorshadow = None, shadowdistance = 2, debug = False, updateFunction = None, escapeFunction = None):      
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
        self.__offset = (offset_text[0] * GE.getScreenMolt(), offset_text[1] * GE.getScreenMolt())
        self.__offset_triangle = (offset_triangle[0] * GE.getScreenMolt(), offset_triangle[1] * GE.getScreenMolt())
        
        if wh == None: self.__wh = (GE.getScreenResolution()[0] - self.__ot * 2, 70 * GE.getScreenMolt())
        else: self.__wh = wh[0] * GE.getScreenMolt(), wh[1] * GE.getScreenMolt()
        
        if pos == None: self.__pos = (0 * GE.getScreenMolt() + self.__ot, GE.getScreenResolution()[1] - self.__wh[1])
        else: self.__pos = pos[0] * GE.getScreenMolt(), pos[1] * GE.getScreenMolt()
        
        self.__font = font
        self.__text = default_text
        self.__text_color = text_color
        self.__lastchars = self.__text[-5:]
        
        self.__isimage = False
        
        self.__size_triangle = triangle_size * GE.getScreenMolt()
        
        if type(background) is list:
            self.__background = background
            self.__isimage = True
        else:
            if type(background) is tuple: self.__background = RGBToHex(background[0], background[1], background[2])
            else: self.__background = background if background in mcol.cnames.keys() else mcol.to_hex(background)
            
        
        self.__descr = ""
        self.__incr = vel_text / GE.getTimeMolt() * GE.getDeltaTime()
        self.__def_incr = self.__incr
        self.__delay = 0
        self.__sizechar = size_char if size_char > 0 else 12
        self.__classic_sizechar = 12
        self.__wordlimit = wordsperline
        if wordsperline == None or wordsperline < 2: self.__wordlimit = (8 * 2) - int((8 * size_char) / self.__classic_sizechar)
        self.__charmax = charmax
        self.__update_funct = updateFunction
        self.__escape_funct = escapeFunction
        self.__finished = False
        self.__pressed = False
        self.__endofthedialogue = False
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
        
        if type(self.__background) == str and not self.__isimage: self.__background = hex2rgb(self.__background)

        self.__rect = pygame.Rect(self.__pos[0], self.__pos[1], self.__wh[0], self.__wh[1])


        if self.__isimage:
            img = pygame.image.load(self.__background[0]).convert_alpha()
            self.__img = pygame.transform.scale(img, (img.get_width() * self.__background[1] * GE.getScreenMolt(), img.get_height() * self.__background[1] * GE.getScreenMolt()))
            
            self.__wh = img.get_size()


        self.__images = []
        self.__lines = []

    def Print(self, text: str):
        """ 

# Print
----------------------------------------------------------------------------------------
- Pass every type of text
- ### No parametres = str "Default Value"
- #### Char limit 400

"""
        
        self.__delay = 0
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
        self.__lastchars = self.__text[-5:]
        
        while not self.__finished:
            
            try:
                if self.__update_funct != None: self.__update_funct()
            except RecursionError:
                raise RecursionError(colored("#ff0000", "\nRecursionError: You need to call Dialogue() class in another function to work properly!"))
            
            
            def dialogue_comands():    
                if GE.Event.type == pygame.QUIT:
                    GE.Quit()
            
                if GE.Event.type == pygame.KEYDOWN:
                    if GE.Event.key == pygame.K_ESCAPE:
                        if self.__escape_funct != None: self.__escape_funct()
                    
                    if GE.Event.key == pygame.K_SPACE:
                        if self.__endofthedialogue:
                            self.__finished = True
                        
                        if not self.__pressed:                         
                            if self.__flag_new:
                                self.__flag_new = False
                                self.Print(self.__new_line)
                                
                            self.__incr = (self.__def_incr * 4) / GE.getTimeMolt() * GE.getDeltaTime()
                        
                        self.__pressed = True
                        
                        
                        
            self.__appendText()
        
            if not self.__isimage and self.__background != None: 
                self.__dark = 20; self.__dark = (self.__dark, self.__dark, self.__dark); 
                self.__PrintBG()
            else: self.__PrintIM()

            for image in self.__images:
                GE.getScreen().blit(*image)
            
            for line in self.__lines:
                line.Print()

            
            self.__PrintTX()
            
            if self.__show_flashing: self.__RenderTriangle()
            
            
            GE.CheckComands(dialogue_comands)
            GE.Update()
        
        self.__pressed = False
        self.__wordlimit = self.__df_wordsperline
        self.__endofthedialogue = False
        
        
    def __appendText(self):
        
        if self.__flip_flop.AfterTimes(times = 30 * GE.getTimeMolt() * GE.getDeltaTime()):
            self.__flag_flash = not self.__flag_flash
        
        if int(self.__delay) < len(self.__text): 
            self.__descr = self.__text[:int(self.__delay)+1]
        else:
            self.__descr = self.__text
        
        self.__delay += 10 / GE.getFps() * GE.getTimeMolt() * GE.getDeltaTime() * self.__incr


    def AddImage(self, path: str, pos: tuple = None, multiplayer: int = 1):
        """
# AddImage
----------------------------------------------------------------------------------------
- Add a Image in the dialogue view

## Args:

- path: \"Mypath/myimag.png\" --> str

- pos: (0, 0) --> tuple (You need to set the ScreenMolt)

- multiplayer: pygame.transform.scale(img, **1) --> int
        
        """
        
        p = pos if pos != None else self.__pos
        
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (img.get_width() * multiplayer * GE.getScreenMolt(), img.get_height() * multiplayer * GE.getScreenMolt()))

        self.__images.append([img, p])
        
    
    def AddLine(self, *args, **kwargs):
        """
# AddLine
----------------------------------------------------------------------------------------
- Add a Printline in the dialogue view

## Args:

- pos = None (You need to set the ScreenMolt), defaultText = "default text", alignment = "center", size = 25

- font = 'freesansbold.ttf', color = "Green", backgroundcolor = None, colorshadow = None, 
shadowdistance = 2, bordercolor = "Black", borderwidth = 1

- showborder = False, showpoints=False, showcoords=False
        
        """
        line = PrintLine(*args, **kwargs)
        
        self.__lines.append(line)

    def __RenderTriangle(self):
        
        size = self.__size_triangle
        pos = [
                (self.__rect[0]+ self.__offset_triangle[0] + self.__distancex + self.__ot, self.__rect[3] + self.__rect[1] + self.__offset_triangle[1] + self.__distancey - self.__ot - size), 
                (self.__rect[0] + self.__offset_triangle[0] + self.__distancex + self.__ot + size, self.__rect[3] + self.__rect[1] + self.__offset_triangle[1] + self.__distancey - self.__ot - size),  
                (self.__rect[0] + self.__offset_triangle[0] + self.__distancex + self.__ot + size/2, self.__rect[3] + self.__rect[1] + self.__offset_triangle[1] + self.__distancey - self.__ot - size/3.5)
                
                ]
        
        if self.__flag_flash:
            
            if self.__isimage:
                pygame.draw.polygon(GE.getScreen(), "White", pos)
                pygame.draw.polygon(GE.getScreen(), "Grey", pos, 2 * int(GE.getScreenMolt() + 0.9))
            else:
                chiaro = (255 - self.__background[0], 255 - self.__background[1], 255 - self.__background[2])
                chiaro_tri = tuple(map(lambda i, j: abs(i - j), self.__background, self.__dark))
                pygame.draw.polygon(GE.getScreen(), tuple(map(lambda i, j: i + j//1.2, self.__background, chiaro)), pos)
                pygame.draw.polygon(GE.getScreen(), tuple(map(lambda i, j: i + j//1.6, chiaro_tri, chiaro)), pos, 2 * int(GE.getScreenMolt() + 0.9))
        

    def __PrintBG(self):
        pygame.draw.rect(GE.getScreen(), self.__background, self.__rect, 0, 4 * int(GE.getScreenMolt() + 0.9))
        pygame.draw.rect(GE.getScreen(), tuple(map(lambda i, j: abs(i - j), self.__background, self.__dark)), self.__rect, 2 * int(GE.getScreenMolt() + 0.9), 4 * int(GE.getScreenMolt() + 0.9))

    def __PrintIM(self):
        GE.getScreen().blit(self.__img, self.__rect.topleft)
        
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
                
                    pos = (self.__pos[0] + self.__ot*2 + self.__offset[0], self.__pos[1] + self.__ot*2 + self.__offset[1] + (space_line * i)), 
                    
                    alignment = "start", size = self.__sizechar, 
                    
                    color=self.__text_color, font=self.__font,
                    
                    colorshadow=self.__shadows[0], shadowdistance=self.__shadows[1],
                    
                    showborder=self.__debug, showpoints=self.__debug, showcoords=self.__debug
                    
                )
            
            # text_passed = "Default"
            if line.getPos()[1] + line.getLineSize()[1] < self.__pos[1] + self.__wh[1] * GE.getScreenMolt():
                last_line = text_passed
                self.__pressed = False
                line.Print(last_line)
            else:
                self.__flag_new = True
                
            if line.getPos()[0] + line.getLineSize()[0] > self.__pos[0] + self.__wh[0] * GE.getScreenMolt():
                
                if self.__wordlimit - 1 >= 2:
                    self.__wordlimit -= 1
                
                self.__flag_format = True
        
        
        val = -5
        if last_line != "" and self.__flag_new and text_passed[val:] != self.__lastchars: 
            self.__new_line = self.__text.split(last_line)[1]
        else:
            self.__flag_new = False
        
        if text_passed[val:] == self.__lastchars:
            self.__endofthedialogue = True

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
        key_holded = True if holded else bool(pygame.key.get_pressed().count(True))
        
        import traceback
        
        
        if not name.lower() in self.__NotfoundValues:
            self.__do = Do()
        
        if name.lower() in self.__dict.keys():    
            cond = key_pressed in self.__dict[name.lower()] and key_holded
            
            if cond:
                self.__functionDict[name.lower()]() if self.__functionDict[name.lower()] != None else 0
                
                if self.__debug:
                    t = " "+str(self.__def_name)+" | - " +str(name.lower())+" --> "+str(self.__functionDict[name.lower()].__name__)+"()\n"
                    c = "#6b4040"
                    print(colored(c, t))
                    GE.ConsoleLog(t, c)
            
            return cond
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


class __Sprite():
    def __init__(self):
        self.__Sprites = dict()
        self.__Names = dict()
    
    def newSprite(self, name: str = "Default"):
        self.__Sprites[name] = dict()
        
        return self.Name(name)
    
    def Remove(self, name):    
        import traceback
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
    
        
        if name in self.__Sprites:
            self.__Sprites.pop(name)
        else:
            print(colored("#faf676", "\nline "+str(line_number)+" | "+name+" --> The name of Sprite doesn't already exist"))
        
        if name in self.__Names:
            self.__Names.pop(name)
    
    def Clear(self):
        self.__Sprites.clear()
        self.__Names.clear()
    
    def ReturnDict(self):
        return self.__Sprites
    
    def Name(self, name: str = "Default"):
        
        if name in self.__Sprites:
            if name not in self.__Names:
                self.__Names[name] = self.__name(name, self.__Sprites)
            return self.__Names[name]
        else:
            import traceback
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        
            print(colored("#faf676", "\nline "+str(line_number)+" | "+name+" --> The name of Sprite doesn't exist"))
        
            return None
        
        
    class __name():
        def __init__(self, name: str = "Default", sprites: dict = {"Default":{}}):
            
            self.__speed_animations = 0.2
            self.__actual_value = 0
            self.__start_value_animation = 0.9

            self.__Sprites = sprites
            self.__Velocity = {"start_value": self.__start_value_animation, "value": self.__actual_value, "speed": self.__speed_animations}
            self.__name = name
            
        def ReturnDict(self):
            return self.__Sprites[self.__name]
            
        def SetAnimationSpeed(self, animation_speed: int = 4, start_value: float = 0.9):
            self.__speed_animations = int(animation_speed) / GE.getFps() * GE.getTimeMolt() * GE.getDeltaTime()
            self.__actual_value = 0
            self.__start_value_animation = start_value
            
            self.__Velocity = {"start_value": self.__start_value_animation, "value": self.__actual_value, "speed": self.__speed_animations}
            
            
        def AddToSpriteStates(self, states: list = ["up", "down", "left", "right"]):
            if self.__name in self.__Sprites:
                self.__Sprites[self.__name] = dict([(state, list()) for state in states])
                
            return self
                
        def LoadImages(self, name_state: str = "up", path: str = "directory/", convert_alpha: bool = False, scale: int = 1, flip_x: bool = False, flip_y: bool = False, num_range: int = None):
            import os, re
            
            n_range = num_range
            FileNames = os.listdir(path)

            try:
                FileNames.sort(key=lambda f: int(re.sub('\D', '', f)))
            except:
                FileNames.sort()
                
            sorted(FileNames)

            files = []
            for filename in FileNames:
                if "." in filename:
                    files.append(filename)
                
            files = files[:n_range]
                
            self.__Sprites[self.__name][name_state] =    [   
                                                pygame.image.load(path + "/" + file).convert_alpha() if convert_alpha 
                                                else pygame.image.load(path + "/" + file).convert() 
                                                for file in files
                                            ]
            
            
            s = scale * GE.getScreenMolt()
            self.__Sprites[self.__name][name_state] =    [   
                                                pygame.transform.scale(img, (img.get_width() * s, img.get_height() * s))
                                                for img in self.__Sprites[self.__name][name_state]
                                            ]
            
            self.__Sprites[self.__name][name_state] =    [   
                                                pygame.transform.flip(img, flip_x, flip_y)
                                                for img in self.__Sprites[self.__name][name_state]
                                            ]
            
            return (name_state, files)
        
        def Animate(self, name_state: str = "up"):
            
            self.__Velocity["value"] += self.__Velocity["speed"]    
            
            if int(self.__Velocity["value"]) >= len(self.__Sprites[self.__name][name_state]):
                self.__Velocity["value"] = 0
            
            return self.__Sprites[self.__name][name_state][int(self.__Velocity["value"])]
        
        def ReturnStates(self):
            return tuple(self.__Sprites[self.__name].keys())
        
        def Remove(self, state):    
            import traceback
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        
            if state in self.__Sprites[self.__name]:
                self.__Sprites[self.__name].pop(state)
            else:
                print(colored("#faf676", "\nline "+str(line_number)+" | "+state+" --> The State of Sprite ( "+self.__name+ ") doesn't already exist"))
    
        def Clear(self, state):
            self.__Sprites[state].clear()


Sprites = __Sprite()

class Player():
    def __init__(self, pos: tuple = (0, 0), speed: tuple = (5, 10), background_color: str = "Black", show_background: bool = True, Name_sprite: str = None, keyinput: classmethod = InputKeys(False), size: tuple = (0, 0), mesh_collision: str = "simple" or "advanced", hitbox: tuple = None,  show_mesh: bool = False):
        self.position = pygame.math.Vector2(pos)
        self.default_pos = self.position
        
        self.speed = speed
        self.default_speed = speed
        
        self.direction_movement = pygame.math.Vector2()
        
        self.default_size = size
        self.size = size
        self.width, self.height = size
        self.hitbox = hitbox
        
        self.__background_color = background_color
        self.__show_background = show_background
        
        self.__KeyInput = keyinput
                
        self.__typeofmesh = mesh_collision.lower()
        self.__name_of_sprite = Name_sprite
        self.__show_mesh = show_mesh
        
        self.__buttons = dict()
        
        self.meshIsActive = False
        
        self.__current_direction = list(Sprites.Name(self.__name_of_sprite).ReturnDict().keys())[1]
        self.setMesh()

    def setMesh(self):
        sprite = Sprites.Name(self.__name_of_sprite).ReturnDict()
        
        if self.default_size == (0, 0) and not self.meshIsActive:
            self.meshIsActive = True
            self.default_size = sprite[list(sprite.keys())[0]][0].get_size()
        
        self.size = tuple([val * GE.getScreenMolt() for val in self.default_size])
        self.width, self.height = self.size
        
        if self.hitbox == None: self.hitbox = (0, 0, *self.size)
        
        if self.__typeofmesh == "advanced":
            self.__rect =   {
                                "center": pygame.Rect(self.hitbox[0] + self.position.x, self.hitbox[1] + self.position.y, 
                                    self.hitbox[2], self.hitbox[3]), 
                            
                                "top": pygame.Rect(self.hitbox[0] + self.position.x, self.hitbox[1] - self.hitbox[3] + self.position.y, 
                                    self.hitbox[2], self.hitbox[3]),
                                
                                "bottom": pygame.Rect(self.hitbox[0] + self.position.x, self.hitbox[1] + self.hitbox[3] + self.position.y, 
                                    self.hitbox[2], self.hitbox[3]),
                                
                                "left": pygame.Rect(self.hitbox[0] - self.hitbox[2] + self.position.x, self.hitbox[1] + self.position.y, 
                                    self.hitbox[2], self.hitbox[3]),
                                
                                "right": pygame.Rect(self.hitbox[0] + self.hitbox[2] + self.position.x, self.hitbox[1] + self.position.y, 
                                    self.hitbox[2], self.hitbox[3])
                                
                            }  
        else:
            self.__rect =   {
                                "center": pygame.Rect(self.hitbox[0] + self.position.x, self.hitbox[1] + self.position.y, 
                                    self.hitbox[2], self.hitbox[3])
                            }
        
        if self.__name_of_sprite != None: 
            self.__Sprite = Sprites.Name(self.__name_of_sprite)
            self.__buttons = {key: False  for key in self.__Sprite.ReturnStates()}
        else: self.__Sprite = None
        
        self.Mesh = self.__rect
        
    
    def __MovementManagement(self, direction = None):
        
        if direction.get("up", False):
            self.direction_movement.y = -1
        elif direction.get("down", False):
            self.direction_movement.y =  1
        else:
            self.direction_movement.y =  0
            
        if direction.get("left", False):
            self.direction_movement.x = -1
        elif direction.get("right", False):
            self.direction_movement.x =  1
        else:
            self.direction_movement.x =  0
            
        if self.direction_movement.magnitude() != 0:
            self.direction_movement = self.direction_movement.normalize()
        
        self.position += self.direction_movement * self.speed[0]
    
    def update(self):
        self.setMesh()
        
        if self.__show_background:
            pygame.draw.rect(GE.getScreen(), self.__background_color, self.Mesh["center"], GE.getIntScreenMolt())
                
        if self.__Sprite != None:
            
            def player_comands():
                for key in self.__Sprite.ReturnStates():
                    if GE.Event.type == pygame.KEYDOWN:
                        if not self.__buttons.get(key, True):
                            self.__buttons[key] = self.__KeyInput.Check(key, GE.Event.key)
                        
                    if GE.Event.type == pygame.KEYUP:
                        if self.__buttons.get(key, None) == True:
                            self.__buttons[key] = False
                            
                    debug(self.__buttons)
                        
                        
            GE.CheckComands(player_comands)
            
            flag = False
            movement = None
            
            for value in list(self.__buttons.keys()):
                if value in self.__Sprite.ReturnStates() and self.__buttons[value]:
                    flag = True
                    movement = value
            
            c = self.__Sprite.Animate(movement) if flag else self.__Sprite.ReturnDict()[self.__current_direction][0]
            
            self.__MovementManagement(direction = self.__buttons)
            
            GE.getScreen().blit(c, self.position)
            
            if self.__show_mesh:
                if self.__typeofmesh != "advanced":
                    pygame.draw.rect(GE.getScreen(), self.__background_color, self.Mesh["center"], GE.getIntScreenMolt())
                    
                else:
                    for key in self.Mesh:
                        pygame.draw.rect(GE.getScreen(), "Red", self.Mesh[key], GE.getIntScreenMolt())
            


if __name__ != "__main__":
    print(colored(("#87CEEB"),"\r\nGameEngine 1.0 - Created by Senex03 || Welcome!!"))