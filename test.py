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

py.init()
dialogo = ge.Dialogue()
timer = ge.Timer(time = (0, 5), molt_sec = 1, myfunction = lambda: dialogo.Print("Bellaaaa"), color = "Red", reversed=False)

while True:
        
    for event in py.event.get():
        
        if event.type == py.QUIT:
            sys.exit()
            
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                sys.exit()
    
    DEF.getScreen().fill((255, 255, 255))
    timer.Start()
    timer.Show()
    
    DEF.update()