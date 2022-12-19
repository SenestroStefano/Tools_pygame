from GameEngine import *
from GameEngine import pygame as py

Molt_Time = 1
Molt_Screen = 2

screen_resolution = (490, 270)
FPS = 60


DEF = GameManager(

    # window_resolution = screen_resolution,
    fps = FPS,
    screen_molt = Molt_Screen,
    time_molt = Molt_Time,
    screen_num = 4

)

def inizializza():
    global mainloop
    global showComands
    global timer, dialogo, testo
    
    mainloop = True

    showComands = True
    
    posy = 151
    div = 0.8
    
    dialogo = Dialogue  (
                            updateFunction=render, 
                            pos=(0, posy), 
                            offset_triangle=(-240, -10), 
                            triangle_size = 16*div, 
                            offset_text = (125, 10), offset = 4, 
                            charmax=5000, wordsperline = 5, 
                            debug=False, 
                            background=["Dialogues/Dialoghi.png", div], 
                            colorshadow="Black", 
                            shadowdistance=6, 
                            size_char= 10,
                            vel_text= 3,
                            escapeFunction=exit
                        )
    
    Name = "Senex"
    
    dialogo.AddImage("Dialogues/Speakers/Characters/"+Name+".png", (35 * DEF.getScreenMolt(), (posy + 10) * DEF.getScreenMolt()), 2*div)
    dialogo.AddLine(defaultText = Name, pos = (40 * DEF.getScreenMolt(), (posy + 53) * DEF.getScreenMolt()), alignment = "left", size = 10, color = "Black")
    
    
    timer = Timer(time = (10, 0), molt_sec = 1, myfunction=lambda: print("Ciao Mondo"), color = "Green", reversed=True, removeEvents=True)
    testo = PrintLine(size=20, color="Black")
    
    Myinputs()

def Myinputs():
    global mykeys
    mykeys = InputKeys(True)
    
    mykeys.Add("Debug", ["f1"], DEF.ShowDebug)
    mykeys.Add("Console", ["f3"], DEF.ShowConsole)
    mykeys.Add("Dialogo stampa", ["a", "b", "c"])
    mykeys.Add("Esci", ["escape"])
    mykeys.Add("Aumenta Molt", ["+"])
    mykeys.Add("Diminuisci Molt", ["-"])
    mykeys.Add("Aumenta Time", [","])
    mykeys.Add("Diminuisci Time", ["."])


def render():
    py.display.set_caption("FPS: "+str( int(DEF.getActualFps(2)) ))
    
    DEF.getScreen().fill((255, 255, 255))
    timer.Start()
    timer.Show()
    testo.Print("FPS: "+str( int((DEF.getActualFps(2) * DEF.getDeltaTime())) ))
    
    DEF.ConsoleLog(text= round(DEF.getActualFps(),2), timelife=20)
    DEF.ConsoleLog(text= round(DEF.getTicks(),2), timelife=20)
    

def pre_conditions():
    timer.AddEvent((8, 55), lambda: dialogo.Print("Evento richiamato"))
    timer.AddEvent((8, 52), lambda: dialogo.Print("Evento richiamato 2"))
    timer.AddEvent((8, 50), lambda: timer.AddSeconds(40))
    


def conditions():
    
    if timer.IsOver():
        dialogo.Print("Esempio di testo")
        timer.AddSeconds(538)
        timer.UnPause()

def comands():
    global mainloop
    
        
    if DEF.Event.type == py.QUIT:
        mainloop = not mainloop
        
    if DEF.Event.type == py.KEYDOWN:
        key = DEF.Event.key
        
        if mykeys.Check("Esci", key):
            mainloop = not mainloop
        
        if mykeys.Check("Dialogo stampa", key):
            text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Nunc purus nisl, ornare vitae quam et, rutrum egestas lorem.Aenean consectetur magna ut volutpat scelerisque.Nulla iaculis luctus elit at rhoncus.Aenean aliquam dignissim urna ut consectetur.Pellentesque et ante dui.Nam efficitur convallis enim, vitae pulvinar metus vulputate sed. Proin eget fringilla tellus. Suspendisse semper at ante ac malesuada."
            dialogo.Print(text)

        if mykeys.Check("Aumenta Molt", key, True):
            DEF.setMultipliers(screen_multiplier=DEF.getScreenMolt()+1, defaultfunctionReload = inizializza)
            
        if mykeys.Check("Diminuisci Molt", key, True):
            DEF.setMultipliers(screen_multiplier=DEF.getScreenMolt()-1, defaultfunctionReload = inizializza)

        if mykeys.Check("Aumenta Time", key, True):
            DEF.setMultipliers(time_multiplier=DEF.getTimeMolt()+1, defaultfunctionReload = inizializza)
            
        if mykeys.Check("Diminuisci Time", key, True):
            DEF.setMultipliers(time_multiplier=DEF.getTimeMolt()-1, defaultfunctionReload = inizializza)


def exit():
    DEF.Quit()

def main():
    global mainloop
    
    pre_conditions()
    
    while mainloop:
        
        DEF.CheckComands(comands)
        
        render()
        conditions()
        
        DEF.Update()
        
    exit()
    
if __name__ == "__main__":
    inizializza()
    main()