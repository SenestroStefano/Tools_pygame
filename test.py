from GameEngine import *
import pygame as py
import sys


Molt_Time = 1
Molt_Screen = 2

screen_resolution = (490, 270)
FPS = 60


DEF = Defaults(

    window_resolution = screen_resolution,
    fps = FPS,
    screen_molt = Molt_Screen,
    time_molt = Molt_Time

)

def inizializza():
    global mainloop
    global showComands
    global timer, dialogo, testo
    
    mainloop = True

    showComands = True
    
    dialogo = Dialogue(updateFunction=render, pos=(0, 0), wh=(210, 120), debug=False, background="#431638", colorshadow="Black", shadowdistance=6, size_char=90, wordsperline=9, escapeFunction=exit)
    timer = Timer(time = (0, 5), molt_sec = 1, myfunction=lambda: print("Vengo richiamato una volta sola"), color = "Red", reversed=True, removeEvents=True)
    testo = PrintLine(size=20, color="Black")
    
    Myinputs()

def Myinputs():
    global mykeys
    mykeys = InputKeys()
    
    mykeys.Add("Dialogo stampa", ["a", "b", "c"])
    mykeys.Add("Esci", ["escape"])
    mykeys.Add("Aumenta Molt", ["+"])
    mykeys.Add("Diminuisci Molt", ["-"])


def render():
    py.display.set_caption("FPS: "+str( int(DEF.getActualFps(2)) ))
    
    DEF.getScreen().fill((255, 255, 255))
    timer.Start()
    timer.Show()
    testo.Print("FPS: "+str( int((DEF.getActualFps(2) * DEF.getDeltaTime())) ))

def pre_conditions():
    timer.AddEvent((8, 55), lambda: dialogo.Print("Evento richiamato"))
    timer.AddEvent((8, 52), lambda: dialogo.Print("Evento richiamato 2"))
    timer.AddEvent((8, 50), lambda: timer.AddSeconds(40))
    


def conditions():
    
    if timer.IsOver():
        dialogo.Print("Esempio di testo")
        timer.AddSeconds(538)
        timer.DePause()

def comands():
    global mainloop
    
    for event in py.event.get():
            
        if event.type == py.QUIT:
            mainloop = not mainloop
            
        if event.type == py.KEYDOWN:
            key = event.key
            
            if mykeys.Check("Esci", key):
                mainloop = not mainloop
            
            if mykeys.Check("Dialogo stampa", key):
                text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Nunc purus nisl, ornare vitae quam et, rutrum egestas lorem.Aenean consectetur magna ut volutpat scelerisque.Nulla iaculis luctus elit at rhoncus.Aenean aliquam dignissim urna ut consectetur.Pellentesque et ante dui.Nam efficitur convallis enim, vitae pulvinar metus vulputate sed. Proin eget fringilla tellus. Suspendisse semper at ante ac malesuada."
                dialogo.Print(text)

            if mykeys.Check("Aumenta Molt", key, True):
                DEF.setMultipliers(screen_multiplier=DEF.getScreenMolt()+1, time_multiplier=DEF.getTimeMolt()-1, defaultfunctionReload = inizializza)
                
            if mykeys.Check("Diminuisci Molt", key, True):
                DEF.setMultipliers(screen_multiplier=DEF.getScreenMolt()-1, time_multiplier=DEF.getTimeMolt()+1, defaultfunctionReload = inizializza)

def exit():
    DEF.Quit()

def main():
    global mainloop
    
    pre_conditions()
    
    while mainloop:
        
        comands()
        
        render()
        conditions()
        
        DEF.Update()
        
    exit()
    
if __name__ == "__main__":
    inizializza()
    main()