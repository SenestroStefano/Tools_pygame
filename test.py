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

var = "center"
timer = ge.Timer(time = (5, 0), molt_sec = 1, color = "Red", reversed=False)

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

    if timer.CheckTime((0, 0)):
        var = "center"
    
    if timer.CheckTime((0, 5)):
        var = "start"
        
    if timer.CheckTime((0, 10)):
        var = "end"
        
    if timer.CheckTime((0, 15)):
        timer.AddSeconds(-15)
    
    ge.PrintLine(defaultText="Figataaa", alignment=var, size=120, color="Blue", colorshadow="Black", shadowdistance=4, showcoords=True).Print()
    
    
    if timer.IsOver():
        dialogo.Print("Bellaaaa")
        timer.AddSeconds(536)
    
    DEF.update()