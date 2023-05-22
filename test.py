from GameEngine import *
from GameEngine import pygame as py

Molt_Time = 2
Molt_Screen = 2

screen_resolution = (490, 270)
FPS = 30


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
    global player
    
    mainloop = True

    showComands = True
    
    dialogo = Dialogue  (
                            updateFunction=render, 
                            background="#3444d3",
                            size_char=12,
                            escapeFunction=exit
                        )
    
    # posy = 151
    # div = 0.8
    # Name = "Senex"
    
    # dialogo.AddImage("Dialogues/Speakers/Characters/"+Name+".png", (35 * DEF.getScreenMolt(), (posy + 10) * DEF.getScreenMolt()), 2*div)
    # dialogo.AddLine(defaultText = Name, pos = (40 * DEF.getScreenMolt(), (posy + 53) * DEF.getScreenMolt()), alignment = "left", size = 10, color = "Black")
    
    Sprites.newSprite("Senex")
    Sprites.Name("Senex").AddToSpriteStates(["up", "down", "right", "left"])
    Sprites.Name("Senex").LoadImages("up", "Animations/Senex/WalkVerticalU", True, 2)
    Sprites.Name("Senex").LoadImages("down", "Animations/Senex/WalkVerticalD", True, 2)
    Sprites.Name("Senex").LoadImages("right", "Animations/Senex/WalkOrizontal", True, 2)
    Sprites.Name("Senex").LoadImages("left", "Animations/Senex/WalkOrizontal", True, 2, True)
    
    Player_Input = InputKeys()
    
    Player_Input.Add("up", ["w", "up"])
    Player_Input.Add("down", ["s", "down"])
    Player_Input.Add("right", ["d", "right"])
    Player_Input.Add("left", ["a", "left"])
    
    player = Player(pos=(40, 40), show_mesh=True, mesh_collision="advanced", Name_sprite="Senex", keyinput = Player_Input)
    
    timer = Timer(time = (0, 5), molt_sec = 1, myfunction=lambda: print("Ciao Mondo"), color = "Green", reversed=True)
    testo = PrintLine(size=20, color="Black")
    
    Myinputs()

def Myinputs():
    global mykeys
    mykeys = InputKeys(True)
    
    mykeys.Add("Debug", ["f1"], DEF.ShowDebug)
    mykeys.Add("Console", ["f3"], DEF.ShowConsole)
    mykeys.Add("Dialogo stampa", ["c", "v", "b"])
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
    
    player.update()
    
    
def pre_conditions():
    timer.AddEvent((8, 55), lambda: dialogo.Print("Evento richiamato"))
    timer.AddEvent((8, 52), lambda: dialogo.Print("Evento richiamato 2"))
    timer.AddEvent((8, 50), lambda: timer.AddSeconds(40))
    


def conditions():
    
    if timer.IsOver():
        dialogo.Print("Esempio di testo")
        timer.AddSeconds(540)
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
            text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam"
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