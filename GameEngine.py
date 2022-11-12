"""

--- Senex Module for Pygame ---

- Every Functions need to be setted in a cicle loop
- Thanks for dowloading this file!

"""

class Defaults():
    """ 
--------       
Defaults
--------        
Make an instance of this class to allow this module to work properly

----------------------------------------------------------------------------------------
- easy way to access a very common used function of pygame"""
    
    def __init__(self, game_window: classmethod, window_resolution: tuple, fps: int, screen_molt = 1, delta_time = 1):
        """ 
--------       
Defaults
--------        
Make an instance of this class to allow this module to work properly

----------------------------------------------------------------------------------------
- easy way to access a very common used function of pygame"""

        global GE
        GE = self
        

        try:
            a = screen_molt//1
        except:
            a = 1
        try:
            b = delta_time//1
        except:
            b = 1
        Error.Check(Defaults, "Defaults", 0)
        Error.Check(game_window, "Defaults", 1)
        
        if GE == self:
            print("\033[94m {}\033[00m" .format("\rDefault() class created correctly!"))
        
        self.setScreen(game_window)
        self.setScreenResolution(window_resolution)
        self.setFps(fps)
        self.setScreenMolt(a)
        self.setDelta_time(b)
        self.__Ticks = 0
        
    def getClock(self):
        import pygame
        return pygame.time.Clock()
    
    def update(self):
        """ 

Update
----------------------------------------------------------------------------------------
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

CheckTicks
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- It's a way to have an infinite counter and ripetitive
- Return True/False

        if Ticks / everyMillesec % 1 == 0 :
            return True
        return False


"""
        if round(self.getTicks()/milliseconds, 2) % 1 == 0:
            return True
        return False
        
    def setScreen(self, pygame_display_screen: classmethod):
        self.__game_window = pygame_display_screen
        
    def getScreen(self):
        return self.__game_window
        
    def setScreenResolution(self, pygame_display_screen_mode: tuple):
        self.__window_resolution = pygame_display_screen_mode
        
    def getScreenResolution(self):
        return self.__window_resolution
    
    def setFps(self, var):
        self.__fps = var
        
    def getFps(self):
        return self.__fps
    
    def setScreenMolt(self, screen_multiplayer: int):
        self.__screen_molt = screen_multiplayer
        
    def getScreenMolt(self):
        return self.__screen_molt
    
    def setDelta_time(self, delta_time: int):
        self.__delta_time = delta_time
        
    def getDelta_time(self):
        return self.__delta_time


class Do():
    """ 

DO
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Repeats a part of your code, tot times (specificated)
- You have before to make an istance "otside every cicles"

"""
    def __init__(self):
        """ 

DO
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Repeats a part of your code, tot times (specificated)
- You have before to make an istance "otside every cicles"

"""
        self.__min = 0

    def Once(self, myfunction = None):
        """ 

Once
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- One time per your entire code and then it stops

"""
        return self.Times(myfunction, 1)

    def Times(self, myfunction = None, times = 2):
        """ 

Times
----------------------------------------------------------------------------------------
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

Flip_Flop
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Repeats a part of your code, ON/OFF per times (specificated)
- You have before to make an istance "otside every cicles"

"""
    def __init__(self):
        """ 

Flip_Flop
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Repeats a part of your code, ON/OFF per times (specificated)
- You have before to make an istance "otside every cicles"

"""
        self.__min = 0
        
        
    def AfterOnce(self, myfunction = None):
        """ 

AfterOnce
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- One time is ON and then OFF

"""
        return self.AfterTimes(myfunction, 1)

    def AfterTimes(self, myfunction = None,  times = 2):
        """ 

AfterOnce
----------------------------------------------------------------------------------------
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

Delay
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To make events or recall function after tot time in a cicle
- You have before to make an istance "otside every cicles"

"""
    def __init__(self, sec, myfunction = None):
        """ 

Delay
----------------------------------------------------------------------------------------
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

Start
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To start the delay once it will be finished, it would be off

"""
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                if self.__function != None: self.__function()
                self.__flag = False

    def ReStart(self):
        """ 

Restart
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To Restart the delay once it would be off

"""
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    def Infinite(self):
        """ 

Infinite
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Once it is finished, it will restart again by 0
- Start --> Restart --> Start ...

"""
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/self.__FPS[1], self.__max/self.__FPS, self.__function))

class Timer():
	""" 

Timer
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Timer in pygame
- Default state: countdown (change -> reversed value)
- You have before to make an istance "otside every cicles"

"""
	def __init__(self, time: tuple, molt_sec = 1, myfunction = None, color = 'Black', font = 'freesansbold.ttf', reversed: bool = True):
		""" 

Timer
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Timer in pygame
- Default state: countdown (change -> reversed value)
- You have before to make an istance "otside every cicles"

"""
		self.__max_min = time[0]
		self.__max_sec = time[1] * GE.getFps()

		if reversed:
			self.__minutes = time[0]
			self.__seconds = time[1] * GE.getFps()
		else:
			self.__minutes = 0
			self.__seconds = 0

		self.__decrement = molt_sec
		self.__function = myfunction
		self.__flag = True
		self.__color = color
		self.__font = font
		self.__size = 20 * int(GE.getScreenMolt())
		self.__reversed = reversed
		self.__do = Do()

		if self.__seconds/GE.getFps() < 10:
			self.__testo2 = ":0"
		else:
			self.__testo2 = ":"

		if self.__minutes < 10:
			self.__testo1 = "0"
		else:
			self.__testo1 = ""

    #print(self.min, self.max, self.increment, self.function)

	def Start(self):
		""" 

Start
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To start the timer once it will be finished, it would be off

"""
		if self.__flag and not self.IsOver():
			if self.__reversed:
				self.__seconds -= self.__decrement
    
				if self.__seconds <= 0:
					self.__seconds = 60 * GE.getFps()
					self.__minutes -= 1
			else:
       
				self.__seconds += self.__decrement
    
				if self.__seconds > 60 * GE.getFps():
					self.__seconds = 0
					self.__minutes += 1


			if self.__seconds/GE.getFps() < 10:
				self.__testo2 = ":0"
			else:
				self.__testo2 = ":"

			if self.__minutes < 10:
				self.__testo1 = "0"
			else:
				self.__testo1 = ""

		else:
			if self.__function != None: self.__do.Once(self.__function)
			self.Pause()

	def ReStart(self):
		""" 

Restart
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To Restart the timer once it would be off

"""
		if not self.__flag:
			self.__flag = True
			self.__minutes = self.__max_min

	def Pause(self):
		""" 

Pause
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To set it a pause mode

"""
		self.__flag = False

	def DePause(self):
		""" 

Depause
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To set it a depause mode, so to continue

"""
		self.__flag = True

	def AddSeconds(self, value):
		""" 

AddSeconds
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Function that allows to add seconds (+/-) on the timer
- Automatically converts seconds into minutes

"""
		if (self.__getSeconds() + value) >= 60 or (self.__getSeconds() + value) <= 0:

			self.__minutes += int(value/60)
			
			m =  value//GE.getFps()

			var = value - (m * 60)
			d = self.__getSeconds() + var - 60
			
			self.__seconds += var * GE.getFps()

			if self.__getSeconds() >= 59:
				self.__seconds = d * GE.getFps()

		else:
			self.__seconds += value * GE.getFps()

	def Stop(self):
		""" 

Stop
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To stop the timer, it will be start by the default value

"""
		self.__init__(self.__max_sec, self.__molt_sec, self.__function)

	def Show(self):
		""" 

Show
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- To show the timer as a pygame.font.render on game window

"""
		import pygame
		testo = pygame.font.Font(self.__font, self.__size).render((self.__testo1+str(self.__minutes)+str(self.__testo2)+str(int(self.__seconds/GE.getFps()))), True, self.__color)
		GE.getScreen().blit(testo, (GE.getScreen().get_width()/2 - testo.get_width()/2, 35 * GE.getScreenMolt()))
  
	def ChangeColor(self, v):
		self.__color = v
  
	def ChangeSize(self, v):
		self.__size = v * int(GE.getScreenMolt())
  
	def ChangeFont(self, v):
		self.__font = v

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

getTime
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Returns a tuple of the actual minutes and seconds
- (minutes: int, seconds: int)

"""
		return (int(self.__getMinutes()), int(self.__getSeconds()))

	def CheckTime(self, v: tuple = (0, 0)):
		""" 

CheckTime
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Checks a tuple of the actual minutes and seconds with the tuple passed as parametrer
- (Timer.minutes: int, Timer.seconds: int) == (Parametrer.minutes: int, Parametrer.seconds: int)
- Returns True/False

"""
		return True if self.getTime() == v else False

	def ActualState(self):
		if self.__flag:
			print("| Current Second: %d | Min Seconds: %d | Function: %s |" %(self.__getSeconds() * self.__getMinutes() * 60, 0, self.__function))

class PrintLine():
    """ 

PrintLine
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- it's a pygame.font.render but easier to set

"""
    def __init__(self, pos = None, defaultText = "default text", alignment = "center", size = 25, font = 'freesansbold.ttf', color = "Green", backgroundcolor = None, showborder = False, bordercolor = "Black", borderwidth = 1, showpoints=False, showcoords=False):
        """ 

PrintLine
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- it's a pygame.font.render but easier to set

"""
        self.__pos = pos
        self.__text = defaultText
        self.__size = size * GE.getScreenMolt()
        self.__alignment = alignment
        self.__font = font
        self.__color = color
        self.__bg = backgroundcolor
        self.__showborder = showborder
        self.__bordercolor = bordercolor
        self.__borderwidth = borderwidth * GE.getScreenMolt()
        self.__showpoints = showpoints
        self.__showcoords = showcoords
        
        if self.__pos == None: 
            self.__pos = GE.getScreenResolution()
            
        Error.Check(self.__pos, "PrintLine", 2)
        Error.Check(self.__pos, "PrintLine", 3)
        
    def getPos(self):
        return self.__pos

    def Print(self, text = None):
        
        if text != None and type(text) == str: self.__text = text
        self.__Print()

    def __Print(self):
        import pygame
        text = pygame.font.Font(self.__font, self.__size).render((self.__text), True, self.__color, self.__bg)
        
        point = self.__pos
        if self.__alignment == "center":
            self.__pos = (self.__pos[0]/2 - text.get_width()/2, self.__pos[1]/2 - text.get_height()/2)
            point = (self.__pos[0] + text.get_width()/2, self.__pos[1] + text.get_height()/2)
        elif self.__alignment == "end":
            self.__pos = (self.__pos[0] + text.get_width()/2, self.__pos[1])
            point = (self.__pos[0] + text.get_width(), self.__pos[1])
            
        GE.getScreen().blit(text, self.__pos)
        
        if self.__showborder:            
            pygame.draw.rect(GE.getScreen(), self.__bordercolor, pygame.Rect(self.__pos[0], self.__pos[1], text.get_width(), text.get_height()), self.__borderwidth)

        if self.__showpoints:
            pygame.draw.circle(GE.getScreen(), "Green", self.__pos, 5 * GE.getScreenMolt() * self.__size/36)
            pygame.draw.circle(GE.getScreen(), "Blue", (self.__pos[0] + text.get_width(), self.__pos[1] + text.get_height()), 5 * GE.getScreenMolt() * self.__size/36)
            pygame.draw.circle(GE.getScreen(), "Red", point, 3 * GE.getScreenMolt() * self.__size/36)
            
        if self.__showcoords:
            
            diff = 2
            size = self.__size//diff
            
            coords = pygame.font.Font('freesansbold.ttf', size).render((str(self.getPos())), True, "Black")
            GE.getScreen().blit(coords, (self.__pos[0] + text.get_width()/2 - coords.get_width()/2, self.__pos[1] - text.get_height()/1.6))
        
# DA RIVEDERE
class Dialogue():
    """ 

Dialogue
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- It's a interface bar created for dialogues
- It's a sync class (so until it's not dead the other components won't update), but it allows you to pass a function that realoads itself
- You have before to make an istance "otside every cicles" and then set your preferences on the instance
- You are free to change text when you want with Print() method

"""
    def __init__(self, background: tuple = (180, 192, 212), pos: tuple = None, wh: tuple = None, show_flashing = True, size_char = 14, default_text = "This is an example of Dialogue", text_color = "White", offset = 5, update = None):
        import pygame        
        """ 

Dialogue
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- It's a interface bar created for dialogues
- It's a sync class (so until it's not dead the other components won't update), but it allows you to pass a function that realoads itself
- You have before to make an istance "otside every cicles" and then set your preferences on the instance
- You are free to change text when you want with Print() method

"""
        self.__ot = offset * GE.getScreenMolt()
        
        if wh == None: self.__wh = (GE.getScreenResolution()[0] - self.__ot * 2, 100 * GE.getScreenMolt())
        else: self.__wh = wh[0] * GE.getScreenMolt(), wh[1] * GE.getScreenMolt()
        
        if pos == None: self.__pos = (0 * GE.getScreenMolt() + self.__ot, GE.getScreenResolution()[1] - self.__wh[1])
        else: self.__pos = pos[0] * GE.getScreenMolt(), pos[1] * GE.getScreenMolt()
        
        self.__text = default_text
        self.__text_color = text_color
        self.__background = background
        self.__descr = ""
        self.__incr = 100
        self.__delay = 0
        self.__charmin = 20
        self.__charlimit = 0
        self.__update_funct = update
        self.__finished = False
        self.__flag = False
        self.__sizechar = size_char
        self.__show_flashing = show_flashing
        self.__flag_flash = False
        
        Error.Check(self.__pos, "Dialogue", 2)
        Error.Check(self.__wh, "Dialogue", 3)
        Error.Check(self.__text_color, "Dialogue", 3)
        
        self.__distancex, self.__distancey = 25 * GE.getScreenMolt(), 5 * GE.getScreenMolt()



        self.__rect = pygame.Rect(self.__pos[0], self.__pos[1], self.__wh[0], self.__wh[1])
       
    def Print(self, text: str):
        """ 

Print
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
- Pass every type of text
- Char limit 400

"""
        import pygame
        
        if text != "":
            self.__text = text
        
        while not self.__finished:
                        
            if self.__update_funct != None: self.__update_funct()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    import sys
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
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
        
        if GE.CheckTicks(26):
            self.__flag_flash = False
        else:
            self.__flag_flash = True
        
        if int(self.__delay) < len(self.__text): 
            self.__descr = self.__text[:int(self.__delay)+1]
        else:
            self.__descr = self.__text
        
        self.__delay += 0.1 / GE.getFps() * self.__incr
            
        # print(int(self.__delay), GE.getFps())

    def __PrintBG(self):
        import pygame
        pygame.draw.rect(GE.getScreen(), self.__background, self.__rect, 0, 4 * GE.getScreenMolt())
        pygame.draw.rect(GE.getScreen(), tuple(map(lambda i, j: abs(i - j), self.__background, self.__dark)), self.__rect, 2 * GE.getScreenMolt(), 4 * GE.getScreenMolt())
        
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
            pygame.draw.polygon(GE.getScreen(), tuple(map(lambda i, j: i + j//1.6, chiaro_tri, chiaro)), pos, 2 * GE.getScreenMolt())
        
        self.__PrintTX()

    def __PrintIM(self):
        pass

    def __PrintTX(self):
        
        g = len(self.__text.split(" "))
        val = len(self.__text)//self.__charmin+1
        pr = g//val
        
        self.__charlimit = self.__charmin * pr
        
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
            PrintLine(text=text_passed, pos = (self.__pos[0] + self.__ot*2 + self.__distancex*4, self.__pos[1] + self.__ot*2 + space_line * i + self.__distancey*2), alignment = "start", size = self.__sizechar, showborder=False, color=self.__text_color)
        
            if len(text_passed) == len(self.__text):
                self.__flag = True


# CLASSI PUBBLICHE
def __classi():
    global Error
    Error = __Errors()


class __Errors():
    def Check(self, var, nameclass: str, type: int):
        import sys, pygame
        # ERRORS
        
        if type == 0:
            try:
                var
            except ValueError:
                sys.exit("\n"+"GameEngine | ValueRequired: You have to before make an istance of Defaults() to use correctly the engine")
                
        elif type == 1:
            if not "Surface" in str(var):
                sys.exit("\n"+str(nameclass)+" | ValueRequired: You have to set the Screen in Defaults() method")
        
        elif type == 2:
            if len(var) < 1:
                sys.exit("\n"+str(nameclass)+" | ValueError: invalid argument! it must be a "+str(tuple)+", you put a "+str(var))
                
        elif type == 3:
            if len(var) < 2:
                sys.exit("\n"+str(nameclass)+" | IndexError: invalid argument! it must be long 3, you put "+str(len(var)))
                
        elif type == 4:
            if len(var) == 2:
                sys.exit("\n"+str(nameclass)+" | IndexError: invalid argument! it must be long 2, you put "+str(len(var)))
                
        elif type == 5:
            if type(var) != int:
                sys.exit("\n"+str(nameclass)+" | ValueError: invalid argument! it must be a "+str(int)+", you put a "+str(type(var)))



__classi()



def __testa():
    import pygame, sys
    pygame.init()

    Delta_Time = 1
    MULT = 2

    screen_resolution = (600 * MULT, 400 * MULT)
    screen = pygame.display.set_mode(screen_resolution)
    FPS = 60 * Delta_Time


    DEF = Defaults(

    game_window = screen,
    window_resolution = screen_resolution,
    fps = FPS,
    screen_molt = MULT,
    delta_time = Delta_Time

    )
   
    
    c = Do()
    def __stampaOggetti():
        x = 255
        GE.getScreen().fill((x, x, x))
        
        timer.Start()
        timer.Show()
        
        # c.Once(lambda: dialogo.Print(""))
        
    
    timer = Timer(time= (0, 3), molt_sec = 1, myfunction = lambda: dialogo.Print("Ma renditi conto che figata"), reversed=False)
    dialogo = Dialogue(update=__stampaOggetti, pos=(10, 300), wh=(580, 100), background=(10, 20, 40))
    
   
    
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        
        __stampaOggetti()
        
        GE.update()
        

print("\033[96m {}\033[00m" .format("\r\nGameEngine 1.0 - Created by Senex03 || Welcome!!"))
if __name__ == "__main__":
    __testa()