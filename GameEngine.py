"""

## Senex Module for Pygame

- Every Functions need to be setted in a cicle loop
- Thanks for dowloading this file!

"""

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

--------
### Returns:
    colored str
"""


    import matplotlib.colors as mcol
    
    rgb = mcol.to_hex(color) if color in mcol.cnames.keys() or type(color) != tuple else color
    if type(rgb) != tuple: rgb = hex2rgb(rgb)
    
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(rgb[0], rgb[1], rgb[2], text)

class Defaults():
    """       
# Defaults
--------        
### Make an instance of this class to allow this module to work properly

----------------------------------------------------------------------------------------
- easy way to access a very common used function of pygame"""
    
    def __init__(self, window_resolution: tuple, fps: int, screen_molt = 1, delta_time = 1):
        """       
# Defaults
--------        
### Make an instance of this class to allow this module to work properly

----------------------------------------------------------------------------------------
- easy way to access a very common used function of pygame"""

        global GE
        GE = self
        
        def_name = "Defaults"
        if GE == self:
            import traceback, pygame
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            print(colored(("#7ccbaa"), "\n"+str(GE.__class__.__name__)+"() --> "+str(def_name)+" | class created correctly!\n"))
            pygame.init()
            
            print(colored(("#53754d"), "____________\n"))
            print(colored(("#53754d"), "DEBUG: \n\n"))
            
        try:
            a = screen_molt//1
        except:
            a = 1
        try:
            b = delta_time//1
        except:
            b = 1
            
        # Errori
        GE.__CheckErrors(Defaults, def_name, 0)
        GE.__CheckErrors(window_resolution, def_name, 1)
        
        self.setScreenMolt(a)
        self.setDelta_time(b)
        self.setScreenResolution(window_resolution)
        self.setFps(fps)
        self.__Ticks = 0
        self.__dfWH = (0, 0)
        
    def getClock(self):
        import pygame
        return pygame.time.Clock()
    
    def getCenterScreen(self):
        return tuple(ris/2 for ris in self.getScreenResolution())
    
    def update(self):
        """ 

# Update
----------------------------------------------------------------------------------------
- Used to update the screen


"""
        self.__Ticks += 1 / self.getFps()
        if int(self.__Ticks) > 1000:
            self.__Ticks = 0
        import pygame
        pygame.display.flip()
        self.getClock().tick(self.getFps())
        
    def getTime(self):
        import pygame
        return pygame.time.get_ticks()
    
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
    
    def setScreen(self, resolution):
        import pygame
        self.__game_window = pygame.display.set_mode(resolution)
    
    def getScreen(self):
        return self.__game_window
        
    def setScreenResolution(self, pygame_display_screen_mode: tuple):
        import pygame
        
        self.__dfWH = pygame.display.Info().current_w, pygame.display.Info().current_h
        
        var = pygame_display_screen_mode
        
        if pygame_display_screen_mode <= self.__dfWH:
            var = self.__dfWH
            old_screen_res = (pygame_display_screen_mode[0] / self.getScreenMolt() + pygame_display_screen_mode[1] / self.getScreenMolt()) / 2
            screen_res = (self.__dfWH[0] / old_screen_res + self.__dfWH[1] / old_screen_res)//2
            self.setScreenMolt(screen_res)
        
        self.__window_resolution = var
        self.setScreen(self.__window_resolution)
        
    def getScreenResolution(self):
        return self.__window_resolution
    
    def setFps(self, var):
        self.__fps = var
        
    def getFps(self):
        return self.__fps
    
    def setScreenMolt(self, screen_multiplier: int):
        self.__screen_molt = screen_multiplier
        
    def getScreenMolt(self):
        return self.__screen_molt
    
    def setDelta_time(self, delta_time: int):
        self.__delta_time = delta_time
        
    def getDelta_time(self):
        return self.__delta_time
    
    
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

            if self.__reversed:

                self.__seconds -= self.__decrement
                self.__cicles -= self.__decrement

                if self.__seconds <= 0:
                    self.__seconds = 60 * GE.getFps()
                    self.__minutes -= 1
            else:

                self.__seconds += self.__decrement
                self.__cicles += self.__decrement
    
                if self.__seconds > 60 * GE.getFps():
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

            # (secondi passati * Delta_Time) / totaleFPS --> per ottenere il moltiplicatore
            molt = int((secs * GE.getDelta_time()) / GE.getFps())

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
        import pygame
        text = pygame.font.Font(self.__font, self.__size).render((self.__text1+str(self.__minutes)+str(self.__text2)+str(int(self.__seconds/GE.getFps()))), True, self.__color)
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
        self.__text = defaultText
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
        
    
    def setPos(self, pos: tuple = (0, 0)):
        self.__pos = pos
    
    def getPos(self):
        return self.__pos
    
    def setColor(self, color):
        self.__color = color
        
    def getColor(self):
        return self.__color

    def Print(self, text: str = None):
        """ 

# Print
----------------------------------------------------------------------------------------
- Pass every type of text
- ### No parametres = str "Default Value"

"""
        if text != None and type(text) == str: self.__text = text
        self.__Print()

    def __Print(self):
        import pygame
        text = pygame.font.Font(self.__font, self.__size).render((self.__text), True, self.__color, self.__bg)
        
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
            
            GE.getScreen().blit(shadow, (position[0], position[1] + self.__size*distance/100))
        
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
    def __init__(self, background: tuple = (180, 192, 212), pos: tuple = None, wh: tuple = None, show_flashing = True, size_char = 14, default_text = "This is an example of Dialogue", text_color = "White", colorshadow = None, shadowdistance = 2, offset = 5, debug = False, updateFunction = None, escapeFunction = None):
        import pygame        
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
        self.__incr = 220
        self.__delay = 0
        self.__charmin = 20
        self.__charlimit = 0
        self.__update_funct = updateFunction
        self.__escape_funct = escapeFunction
        self.__finished = False
        self.__flag = False
        self.__sizechar = size_char
        self.__show_flashing = show_flashing
        self.__flag_flash = False
        self.__shadows = (colorshadow, shadowdistance)
        self.__debug = debug
        self.__distancex, self.__distancey = 25 * GE.getScreenMolt(), 5 * GE.getScreenMolt()
        
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
        import pygame
        
        self.__delay = 0
        self.__flag = False
        
        if text != "":
            self.__text = text
        
        while not self.__finished:
            
            try:
                if self.__update_funct != None: self.__update_funct()
            except RecursionError:
                import sys
                print(colored("#ff0000", "\nRecursionError: You need to call Dialogue() class in another function to work properly!"))
                sys.exit()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    import sys
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.__escape_funct != None: self.__escape_funct()
                    
                    if event.key == pygame.K_SPACE:
                        if self.__flag or self.__finished:
                            self.__finished = True
                        
                        self.__flag = not self.__flag
                        self.__incr = 1000
                        
            self.__appendText()
        
            if not "." in self.__background and self.__background != None: 
                self.__dark = 20; self.__dark = (self.__dark, self.__dark, self.__dark); 
                self.__PrintBG()
            else: self.__PrintIM()
            
            GE.update()
            
        self.__finished = False
            
        
    def __appendText(self):
        
        if GE.CheckTicks(22):
            self.__flag_flash = False
        else:
            self.__flag_flash = True
        
        if int(self.__delay) < len(self.__text): 
            self.__descr = self.__text[:int(self.__delay)+1]
        else:
            self.__descr = self.__text
        
        self.__delay += 0.1 / GE.getFps() * GE.getDelta_time() * self.__incr

    def __PrintBG(self):
        import pygame
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
        
        g = len(self.__text.split(" "))
        val = len(self.__text)//self.__charmin+1
        pr = g//val
        
        self.__charlimit = (self.__charmin * pr)
        
        val = len(self.__text)//self.__charlimit+1
        pr = (g//val) + 4
        
        for i in range(val):
            lim = self.__charlimit
            
            text_passed = self.__descr
            if val > 1:
                if i > 0 and i < val - 1:
                    text_passed = self.__descr[(lim*i)-pr:(((lim)*(i+1))-pr)]
                elif not i and i < val - 1:
                    text_passed = self.__descr[(lim*i):(((lim)*(i+1))-pr)]
                else:
                    text_passed = self.__descr[(lim*i)-pr:((lim*(i+1)))]
                
            
            
            space_line = (90 / val) * GE.getScreenMolt()
            PrintLine(
                
                    defaultText=text_passed,
                    pos = (self.__pos[0] + self.__ot*2 + self.__distancex*4, self.__pos[1] + self.__ot*2 + space_line * i + self.__distancey*2), 
                    alignment = "start", size = self.__sizechar, 
                    color=self.__text_color, 
                    colorshadow=self.__shadows[0],
                    shadowdistance=self.__shadows[1],
                    showborder=self.__debug,
                    showpoints=self.__debug,
                    showcoords=self.__debug
                    
                ).Print()
        
            if len(text_passed) == len(self.__text):
                self.__flag = True

class InputKeys():
    """
# InputKeys
----------------------------------------------------------------------------------------
- A way to set InputKeys and assign them with a custom name
- #### You have before to make an istance "otside every cicles"

    """
    
    def __init__(self):
        """
# InputKeys
----------------------------------------------------------------------------------------
- A way to set InputKeys and assign them with a custom name
- #### You have before to make an istance "otside every cicles"

        """
        self.__dict = {}
        self.__do = Do()
        self.__NotfoundValues = []

    
    def Add(self, name: str = "default", commandlist : list = []):
        """
# Add
----------------------------------------------------------------------------------------
- Add new InputKeys with a name
- ### Parametres -->  name: str = "default", commandlist : list = []

        """
        self.__dict[name.lower()] = commandlist
    
    def Check(self, name: str, key : classmethod):
        """
# Check
----------------------------------------------------------------------------------------
- Check the inputs with the name passed
- ### Parametres -->  name: str, key : classmethod
- #### Returns: True/False

        """
        import pygame
        key_pressed = pygame.key.name(key)
        
        if not name.lower() in self.__NotfoundValues:
            self.__do = Do()
        
        if name.lower() in self.__dict.keys():
            return (True if key_pressed in self.__dict[name.lower()] else False)
        else:
            import traceback
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            self.__do.Once(lambda: print(colored(("#faf676"),"\nline "+str(line_number)+" | "+str(def_name)+".Check("+name+") --> Note: name \""+name+"\" has not been registered!")))
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
        



if __name__ != "__main__":
    print(colored(("#87CEEB"),"\r\nGameEngine 1.0 - Created by Senex03 || Welcome!!"))