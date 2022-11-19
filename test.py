import GameEngine as ge
import pygame as py
import sys


Delta_Time = 1
MULT = 2

screen_resolution = (490, 270)
FPS = 60


DEF = ge.Defaults(

    window_resolution = screen_resolution,
    fps = FPS,
    screen_molt = MULT,
    delta_time = Delta_Time

)

def inizializza():
    global mainloop
    global showComands
    global timer, dialogo, testo
    
    mainloop = True

    showComands = True
    
    dialogo = ge.Dialogue(updateFunction=render, background="#f6412e", colorshadow="Black", shadowdistance=4, size_char=14, escapeFunction=exit)
    timer = ge.Timer(time = (0, 5), molt_sec = 1, myfunction=lambda: print("Vengo richiamato una volta sola"), color = "Red", reversed=True, removeEvents=True)
    testo = ge.PrintLine(size=20, color="Black")
    
    Myinputs()

def Myinputs():
    global mykeys
    mykeys = ge.InputKeys()
    
    mykeys.Add("Dialogo stampa", ["a", "b", "c"])
    mykeys.Add("Esci", ["escape"])
    mykeys.Add("Aumenta Molt", ["o"])
    mykeys.Add("Diminuisci Molt", ["p"])


def render():
    
    DEF.getScreen().fill((255, 255, 255))
    timer.Start()
    timer.Show()
    testo.Print()

def pre_conditions():
    timer.AddEvent((9, 55), lambda: dialogo.Print("Evento richiamato"))
    timer.AddEvent((9, 52), lambda: dialogo.Print("Evento richiamato 2"))
    timer.AddEvent((9, 50), lambda: dialogo.Print("Evento richiamato 3"))
    
    
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
                dialogo.Print("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi urna dolor, porta vitae fermentum malesuada, suscipit nec massa.")

            if mykeys.Check("Aumenta Molt", key, True):
                DEF.setMultipliers(screen_multiplier=DEF.getScreenMolt()+1, delta_time=DEF.getDelta_time()-1, defaultfunctionReload = inizializza)
                
            if mykeys.Check("Diminuisci Molt", key, True):
                DEF.setMultipliers(screen_multiplier=DEF.getScreenMolt()-1, delta_time=DEF.getDelta_time()+1, defaultfunctionReload = inizializza)

def exit():
    print(ge.colored(("#fb3f3f"),"\n--- Exit from the program ---"))
    py.quit()
    sys.exit()

def main():
    global mainloop
    
    pre_conditions()
    
    while mainloop:
        
        comands()
        
        render()
        conditions()
        
        
        py.display.set_caption("FPS: "+str(DEF.getActualFps(2)))
        DEF.update()
        
    exit()
    
if __name__ == "__main__":
    inizializza()
    main()