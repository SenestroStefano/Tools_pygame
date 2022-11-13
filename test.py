import GameEngine as ge
import pygame as py
import sys


Delta_Time = 1
MULT = 2

screen_resolution = (600 * MULT, 400 * MULT)
screen = py.display.set_mode(screen_resolution)
FPS = 60 * Delta_Time


DEF = ge.Defaults(

game_window = screen,
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
    
    
    dialogo = ge.Dialogue(updateFunction=render, background="#f6412e", colorshadow="Black", shadowdistance=4, size_char=20)
    timer = ge.Timer(time = (0, 0), molt_sec = 1, color = "Red", reversed=True)
    testo = ge.PrintLine(defaultText="Mammamia", size=20, color="Black")


def render():
    
    DEF.getScreen().fill((255, 255, 255))
    timer.Start()
    timer.Show()
    testo.Print()
    
    
def conditions():
    timer.AddEvent((9, 55), lambda: dialogo.Print("Nulla troppo figo per essere vero"))
    
    if timer.IsOver():
        dialogo.Print("The big bang theory the best sitcom of the entire world... I love Sheldon Cooper")
        timer.AddSeconds(538)
        timer.DePause()

def comands():
    global mainloop
    
    def clicked(bool, key):
        global showComands
        key_holded = py.key.get_pressed().count(1)
        key_pressed = py.key.name(key)
        
        # bool --> alzato/abbassato
        if bool:
            color = "Green"
        else:
            color = "Red"
        
        if showComands: testo.Print(key_pressed.upper()), testo.setColor(color)
        
        if key_pressed == "escape":
            mainloop = not mainloop
            
        if key_pressed == "tab" and key_holded:
            showComands = not showComands
            testo.Print("Eh la madonna"), testo.setColor("Black")
            
        if key_pressed == "u" and key_holded:
            dialogo.Print("Bella veramente")
    
    for event in py.event.get():
            
        if event.type == py.QUIT:
            mainloop = not mainloop
            
        if event.type == py.KEYDOWN:
            clicked(True, event.key)
                
        if event.type == py.KEYUP:
            clicked(False, event.key)
    

def main():
    global mainloop
    
    while mainloop:
            
        comands()
        
        render()
        conditions()
        
                
        DEF.update()
        
    sys.exit("\nSei uscito")
    
if __name__ == "__main__":
    py.init()
    inizializza()
    main()