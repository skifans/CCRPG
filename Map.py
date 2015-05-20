#Imports
import pygame, random, time, os, ctypes, ast
from pygame.locals import *
from tkinter import *
import tkinter.tix as tix

#Read options from .ini
f = open("options.ini","r")
line1=f.readline() #options header
line2=f.readline() #cellsize line
line3=f.readline() #cellsize value
cellSize=int(line3)
line4=f.readline() #internal editor header
line5=f.readline() #internal editor value
line6=f.readline() #buttons header
line7=f.readline() #buttons value
line8=f.readline() #combat header
line9=f.readable() #combat value'
if int(line5)==1:
    print("Enternal editor enabled")
    internal_editor=TRUE
if int(line7)==1:
    buttons=TRUE
elif int(line7)==0:
    buttons=FALSE
else:
    print("There was an error reading the options file - buttons have been enabled.")
    buttons=FALSE
if int(line9)==0:
    combat_on=0 #off
elif int(line9)==1:
    combat_on=1 #on
else:
    print("There was an error reading the options file - combat has been enabled.")
    combat_on=1
f.close()

#Colour Grid
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
DARKPINK  = (255,  20, 147)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
ORANGE    = (255, 153,  18)
DARKGRAY  = ( 40,  40,  40)
YELLOW    = (255, 255,   0)
BLUE      = (  0,   0, 255)
KHAKI     = (139, 134,  78)

windowWidth = 800
windowHeight = 600
lineColour = WHITE
assert windowHeight % cellSize == 0
assert windowWidth % cellSize == 0
cellWidth = int(windowWidth / cellSize)
cellHeight = int(windowHeight / cellSize)

pygame.init()

class textures():

    class playerTexture():
        x = 0
        y = 0

    class loadigTexture():
        def __init__(self):
            self.x = 0
            self.y = 0

        def loadTexture(self, x, y):
            self.texture = pygame.image.load(os.path.join("textures","whiteTexture.gif"))
            self.texturerect = self.texture.get_rect()
            self.coords = (x, y)
            self.texturerect.move_ip(self.coords)
            window.blit(self.texture, self.texturerect)

playert = textures.playerTexture()

#Closes The Window & Game
def terminate():
    pygame.quit()

#anything in this function will be done each time the playert moves - regardless if direction
boss_list=[[20,40,60],[20,40,60],[0,1,1],[0,1,2]]
def after_movement(playert_x, playert_y, boss_list):
    #x of boss, y of boss, 0 = one time only (the first time playert lands of square) or 1 = repeate (repeate regarless of how many times playert lands on square), boss ID
    if playert_x in boss_list[0]: #check if x of playert is contaiend in x section of array
        location_in_array=boss_list[0].index(int(playert_x)) #if so then take the possition of that x value and save it
        if playert_y==boss_list[1][location_in_array]: #check the y value of the playert against the 2nd diminsion of the array to see if they match
            if boss_list[2][location_in_array]==1: #see if cordinates needs to be cleated
                del boss_list[0][location_in_array] #since only on first landing of sqaure does this need to happen then delete relevent parts of array
                del boss_list[1][location_in_array]
                del boss_list[2][location_in_array]
                del boss_list[3][location_in_array]
            print("boss square triggered")
            combat()
    espawn = random.randint(1,20)
    if espawn == 1:
        combat()

def collision_detection(playert_x, playert_y,player):
    playert_position = str((playert_x, playert_y,player[15]))
    cannot_go_onto = open("Blocked.txt").read().splitlines()
    print(cannot_go_onto)
    if playert_position in cannot_go_onto:
        print("collision detection")
        return False
    return True

#---------------------------------------------------------------------------------------------------------------------------------------------
#combat system
name = "x"
global combatover
class darkness:
    magnus = [100,25,15,30,20,["The sword of darkness",20],["The armour of despair",30],"Magnus, captain of despair",60,1,0,0,0]

#list of classes and stats
#lancer is high attack, high dex, low defence, focused on killing the enemy very quickly
lancer = [40,30,80,10,90,["lance",35],["super_light_armour",2],name,[0,20,1],10,0,0,0,0,0,1]
#archeris a ranged high dex class, it has a wide range of abilities, like befriend and forage
archer = [30,30,100,40,50,["bow", 15],["furs",10],name,[0,20,1],10,0,0,0,0,0,1]
#necromancer summons minions to fight
necromancer = [70,40,40,60,40,["staff",5],["light_armour",5],name,[0,20,1],10,0,0,0,0,0,1]
#warriors are the balanced baseline, and ok at everything
warrior = [50,50,50,50,50,["sword",20],["medium_armour",20],name,[0,20,1],10,0,0,0,0,0,1]
#mages are a spell casters with basic damage spells
mage = [45,30,75,85,45,["wand",5],["light_armour",5],name,[0,20,1],10,0,0,0,0,0,1]
#paladins are endurance tanks, but don't have much attack
paladin = [70,95,40,20,25,["shield",5],["heavy_armour",35],name,[0,20,1],10,0,0,0,0,0,1]
#barbarian is a high attack and health tank
barbarian = [80,40,40,10,80,["great_sword",50],["Abs",30],name,[0,20,1],10,0,0,0,0,0,1]
#Samurai is a dexhealth  class
samurai = [70,30,90,20,40,["Katana",19],["Ancient armour",20],name,[0,20,1],10,0,0,0,0,0,1]
#ninja has high dex, but low everything else, they rely on using skills, like dodge and counter
ninja = [30,20,150,20,30,["Short sword",15],["Kimono",5],name,[0,20,1],10,0,0,0,0,0,1]

classes = ["Warrior","Mage","Paladin","Necromancer","Barbarian","Lancer","Archer","Samurai","Ninja"]
#Tester weapons
sakaretsu_armour = [50,30,20,0,"Sakaretsu armour",8,1,"Armour that increases offensive capability",0,0,10,0,0]
simple_katanna = [60,0,0,0,"Katanna",8,0,"In the right hands this weapon is as deadly as any blade",0,60,0,0,0]

def type_select(player_class):
    global player
    player_class=str(player_class)
    print(player_class)
    if player_class == "barbarian":
            player = barbarian
            image = pygame.image.load(os.path.join("textures","barbarian.gid"))
    elif player_class == "warrior": #changed the if to an elif to cut down lag
            player = warrior
            image = pygame.image.load(os.path.join("textures","necromancer.png"))
    elif player_class == "mage":    #changed the if to an elif to cut down lag
            player = mage
            image = pygame.image.load(os.path.join("textures","necromancer.png"))
    elif player_class == "paladin": #changed the if to an elif to cut down lag
            player = paladin
            image = pygame.image.load(os.path.join("textures","necromancer.png"))
    elif player_class == "necromancer": #changed the if to an elif to cut down lag
            player = necromancer
            image = pygame.image.load(os.path.join("textures","necromancer.gif"))
    elif player_class == "lancer":  #changed the if to an elif to cut down lag
            player = lancer
            image = pygame.image.load(os.path.join("textures","lancer.gif"))
    elif player_class == "archer":  #changed the if to an elif to cut down lag
            player = archer
            image = pygame.image.load(os.path.join("textures","archer.gif"))
    elif player_class == "samurai":#changed the if to an elif to cut down lag
            player = samurai
            image = pygame.image.load(os.path.join("textures","necromancer.png"))
    elif player_class == "ninja":   #changed the if to an elif to cut down lag
            player = ninja
            image = pygame.image.load(os.path.join("textures","necromancer.png"))
    else:
            ctypes.windll.user32.MessageBoxW(0, "Error - player class entered or loaded incorectly. You will now be promted to enter your name & player class", "error", 0)
            print("Error - player class entered incorectly")
            player = "error"
            while player == "error":
                classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja)
    return image

def classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja):
    global player, player_class   #moved global from the if statments to the top to cut down on the ammount needed
    print("What is you're name?")
    name = str(input("my name is:"))
    print("Choose you're class " + name)
    print(classes)
    player_class = str(input())
    player_class = player_class.lower() #added .lower() to make sure that the input was lowercase so it wasn't case sensitvie
    image=type_select(player_class) #loads player array and image
    player[7]=name
    print ("Are you ready?")
    return image

def levelupcheck():
    global player
    statmulti = player[8][2] + 10
    if player[8][0] >= player[8][1]:
        player[8][2] = player[8][2] + 1
        multi = player[8][2] + 1
        player[8][1] = player[8][1] + (40 * multi)

        print("You leveled up!")
        print("You are now level ",player[8][2] )
        if player == warrior:
            player[0] += statmulti+5
            player[4] += statmulti+5
            player[1] += statmulti+5
            player[3] += statmulti+1
            player[2] += statmulti+5
        if player == mage:
            player[0] += statmulti+1
            player[4] += statmulti+2
            player[1] += statmulti+1
            player[3] += statmulti+16
            player[2] += statmulti+2
        if player == paladin:
            player[0] += statmulti+9
            player[4] += statmulti+2
            player[1] += statmulti+8
            player[3] += statmulti+1
            player[2] += statmulti+1
        if player == necromancer:
            player[0] += statmulti+4
            player[4] += statmulti+1
            player[1] += statmulti+4
            player[3] += statmulti+7
            player[2] += statmulti+3
        if player == barbarian:
            player[0] += statmulti+7
            player[4] += statmulti+10
            player[1] += statmulti+1
            player[2] += statmulti+3
        if player == samurai:
            player[0] += statmulti+7
            player[4] += statmulti+3
            player[1] += statmulti+4
            player[3] += statmulti
            player[2] += statmulti+7
        if player == ninja:
            player[4] += statmulti+2
            player[3] += statmulti+1
            player[2] += statmulti+18
    print("Your stats are:")
    print("Vitality: " + str(player[0]))
    print("Endurance: " + str(player[1]))
    print("Dexterity: " + str(player[2]))
    print("Inteligence " + str(player[3]))
    print("Strength " + str(player[4]))
    return
# the enemy arrays
enemy1 = [darkness.magnus,darkness.magnus,darkness.magnus,darkness.magnus,darkness.magnus,darkness.magnus]
def statsetup (darkness,sakaretsu_armour,simple_katanna):
    global player
    if player[15] == 1:
        enemy = enemy1[random.randint(0,5)]
        global ehp,eend,edex,eint,estr,php,pend,pdex,pint,pstr,pw,pa,exp
        print("A new enemy approches \n")
        ehp = enemy[0]
        eend = enemy[1]
        edex = enemy[2]
        eint = enemy[3]
        estr = enemy[4]
        exp = enemy[8]
        php = player[0]
        pend = player[1]
        pdex = player[2]
        pint = player[3]
        pstr = player[4]
        pw = simple_katanna
        pa = sakaretsu_armour
        return ehp,eend,edex,eint,estr,php,pend,pdex,pint,pstr,pw,pa

# defining the function for the enemy turn
def enemyturn ():
    global combatover
    global ehp,eend,edex,eint,estr,php,pend,pdex,pint,pstr,pw,pa
    echoice = random.randint(1,2)
    if echoice == 1:
        print("The enemy attacks you")
        enemyhit = estr - (pend+pa[1])
        ehit = edex*random.randint(1,4) - pdex
        if ehit < 0:
            if enemyhit > 0:
                php = php - enemyhit
                print("the enemy hits you for "+ str(enemyhit))
                if php <= 0:
                    print("You died")
                    combatover = True
            if enemyhit <= 0:
                print("The enemy does no damage")
        else:
            print("the enemy misses")
    else:
        print("The enemy tries to cast a spell!")
        print("It fails!")

#defining the players turn
def playerturn(player,darkness):
    global combatover
    global ehp,eend,edex,eint,estr,php,pend,pdex,pint,pstr,pw,pa
    global pchoice
    print("Choose your action:")
    print("attack spell run")
    if buttons==TRUE:
        app = app_()
        #things before button is pressed
        app.mainloop()
        #things after button is pressed
    elif buttons==FALSE:
        pchoice=input()
    if pchoice == "attack":
        phit = pdex*random.randint(1,4) - edex
        if phit > 0:
            if player == lancer:
                playerhit = (pstr+pdex+pw[0]) - eend
            elif player == archer:
                playerhit = (pw[0]+pdex+pstr/2) - eend
            elif player == samurai:
                playerhit = (pw[0]+pdex) - eend
            elif player == ninja:
                playerhit = (pw[0]+pdex) - eend
            else:
                playerhit = pw[0]+pstr - eend
            if playerhit > 0:
                print("You hit the enemy for " + str(playerhit) + " damage")
                ehp = ehp-playerhit
            else:
                print("You do no damage")
        else:
            print("You miss")
    elif pchoice == "spell":
        print("You don't have any spells")
    elif pchoice == "run":
        print("You try to run")
        run = random.randint(1,10)
        if run < 3:
            print("You fail to run away")
        if run > 3 or run==3:
            print("You manage to run away")
            combatover = True
    else:
        print("Error - command not recognised")

# Running the actual turn
def turn (player,darkness):
    global combatover
    global ehp,eend,edex,eint,estr,php,pend,pdex,pint,pstr,pw,pa
    if pw[8] == 1:
        print("You have " + str(php) + " health")
        print("The enemy has " + str(ehp) + "health")
        print("Choose your action:")
        print("attack spell run")
        pchoice = str(input())
        if pchoice == "attack":
            phit = pdex*random.randint(1,4) - edex
            if phit > 0:
                if player == lancer:
                    playerhit = (pstr+pdex+pw[0]) - eend
                elif player == archer:
                    playerhit = (pw[0]+pdex+pstr/2) - eend
                elif player == samurai:
                    playerhit = (pw[0]+pdex) - eend
                elif player == ninja:
                    playerhit = (pw[0]+pdex) - eend
                else:
                    playerhit = pw[0]+pstr - eend
                if playerhit > 0:
                    print("You hit the enemy for " + str(playerhit) + " damage")
                    ehp = ehp-playerhit
                    if ehp > 0:
                        enemyturn()
                    else:
                        print("The enemy is slain")
                        player[8][1] = player[8][1] + exp
                        levelupcheck()
                        combatover = True
                else:
                    print("you deal no damage")
            else:
                print("You miss")
                enemyturn()
        elif pchoice == "spell":
            print("You don't have any spells")
        elif pchoice == "run":
            print("You try to run")
            run = random.randint(1,10)
            if run < 3:
                print("You fail to run away")
            if run > 3:
                print("You manage to run away")
                combatover = True
    else:
        enemyturn()
        if php > 0:
            playerturn(player,darkness)
            if ehp <= 0:
                print("The enemy is slain")
                player[8][0] = player[8][0] + exp
                levelupcheck()
                combatover = True
        else:
            print("You died")
            combatover = True
#image=classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja) #un comment tp start set up (class ect. each time the game starts (before the menu))

def combat():
    global combatover
    global player
    no_combat=[2,3] #maps where combat will not be triggered
    if player[15] not in no_combat and combat_on==1:
        combatover = False
        background = pygame.image.load(os.path.join("backgrounds","combat_area.gif")) #load image for combat background
        screen.blit(background, (0,0)) #place this at 0,0
        you = pygame.image.load(os.path.join("combat","you.gif")) #load image for you
        screen.blit(you, (100,200)) #place this at (100,200)
        enemy = pygame.image.load(os.path.join("combat","enemy.gif")) #load image for enemy
        screen.blit(enemy, (500,100)) #place this at (500,100)
        pygame.display.flip() #update screen
        statsetup(darkness, sakaretsu_armour,simple_katanna)
        while combatover == False:
            turn (player,darkness)
        map_name="map"+str(player[15])+".gif"
        background = pygame.image.load(os.path.join("textures",map_name)) #when combat is finnished, load previous background
        screen.blit(background, (0,0))

def app_():
    root = Tk()
    root.attributes("-topmost", True)
    root.focus_set()
    global pchoice
    class Application(Frame):
        def say_hi(self):
            global pchoice
            print("Run")
            pchoice="run"
            root.destroy()

        def say_hi1(self):
            global pchoice
            print("Spell")
            pchoice="spell"
            root.destroy()

        def say_hi2(self):
            global pchoice
            print("Attack")
            pchoice="attack"
            root.destroy()
        def createWidgets(self):
            self.run = Button(self)
            self.run["text"] = "Run",
            self.run["command"] = self.say_hi

            self.run.pack({"side": "left"})

            self.spell = Button(self)
            self.spell["text"] = "Spell",
            self.spell["command"] = self.say_hi1

            self.spell.pack({"side": "left"})

            self.attack = Button(self)
            self.attack["text"] = "Attack",
            self.attack["command"] = self.say_hi2

            self.attack.pack({"side": "left"})

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()
    root.attributes("-topmost", False)
    return Application(master=root)

    #root = Tk()
    #end of combat system

#-----------------------------------------------------------------------------------
#debug function
def debug(message,player):
    debug=open("log.txt","a")
    debug.write(str(time.strftime('%X %x %Z')))
    debug.write(" ")
    debug.write(str(player))
    debug.write(" ")
    debug.write(str(message))
    debug.write("\n")
    debug.close()
#-----------------------------------------------------------------------------------
def new_map(direction, playert):
    global player
    hight=3 #the amount of vertical maps
    pygame.display.flip() #suppost to update whole map
    if direction=="up":
        move=player[15]/hight
        if move.is_integer():
            print("off edge of map")
        else:
             player[15]=player[15]+1
    elif direction=="down":
        move=(player[15]-1)/hight
        if move.is_integer():
            print("off edge of map")
        else:
            player[15]=player[15]-1
    elif direction=="right":
        player[15]=player[15]+hight
        move=hight**2-player[15]
        if move<hight**2:
            print("on map")
        else:
            print("off edge of map")
            player[15]=player[15]-hight
    elif direction=="left":
        if player[15]<=hight:
            print("off edge of map")
        else:
            player[15]=player[15]-hight
    image_path="map"+str(player[15])+".gif"
    if os.path.isfile(image_path)==FALSE: #check that a map file exisits, if not then display an error message. Changing this to TRUE and moving to a new map will show the error message if you want to see it.
        img=pygame.image.load("map_error.gif")
        screen=pygame.display.set_mode((0,0))
        screen.blit(img,(0,0))
    else:
        img=pygame.image.load(image_path)
        screen=pygame.display.set_mode((0,0))
        screen.blit(img,(0,0))
    print("area",str(player[15]))
#-----------------------------------------------------------------------------------------------------------------------------------------------
#funtion to display text
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour) #extact purpose unkown but seems to be needed
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, font_size, colour):
    largeText = pygame.font.Font('freesansbold.ttf',font_size) #load font
    TextSurf, TextRect = text_objects(text, largeText, colour) #render text
    TextRect.center = ((x),(y)) #place text
    screen.blit(TextSurf, TextRect) #send to screen, needs to be updated/fliped to be worked

#function for buttoms
#example syntax to call button("return",150,450,100,50,DARKGREEN,GREEN,BLACK,action) note the lack of brackets on action function.
def button(msg,x,y,w,h,inactive_colour,active_colour,text_colour,name_of_function_to_call_when_clicked):
    click = pygame.mouse.get_pressed() #get mouse state (clicked/not clicked)
    mouse = pygame.mouse.get_pos() #get mouse coords
    print("mouse2",mouse)
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #check if mouse is on button
        pygame.draw.rect(screen, active_colour,(x,y,w,h)) #change to active colour
        if click[0] == 1: #check click (above if checks mouse is on button)
            name_of_function_to_call_when_clicked() #do this when clicked (veriable needs not to have brackets)
    else:
        pygame.draw.rect(screen, inactive_colour,(x,y,w,h)) #mouse not on button, switch to inactive colour

    smallText = pygame.font.Font("freesansbold.ttf",20) #load font
    textSurf, textRect = text_objects(msg, smallText,text_colour) #place text in button through text funtion
    textRect.center = ( (x+(w/2)), (y+(h/2)) ) #location of text
    screen.blit(textSurf, textRect) #send to screen (but not update)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#pause function
def pause():
    pause=TRUE
    screen.fill(WHITE) #fill background
    font = pygame.font.SysFont("comicsansm", 115) #font (yes thats right :p)
    text = font.render("Paused", 1, (10, 10, 10)) #text to display
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx #position text
    screen.blit(text, textpos)
    pygame.display.flip() #update display
    while pause==TRUE:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                terminate()
                pygame.display.quit
                break
            elif event.type==KEYDOWN:
                if key[pygame.K_p]:
                    pause=FALSE
                    print("unpasued")
#-----------------------------------------------------------------------------------------------------------------------------------------------
#menu function
global menu
def menu_close():
    global menu1
    print("menu removed")
    menu1=FALSE

def new_game():
    global menu1, image
    print("menu removed")
    menu1=FALSE
    image=classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja)

def menu():
    global menu1
    menu1=TRUE
    screen.fill(WHITE) #fill screen white
    while menu1==TRUE:
        for event in pygame.event.get():
                button("return to game",300,100,150,50,GREEN,DARKGREEN,BLACK,menu_close)
                button("save game",300,200,150,50,GREEN,DARKGREEN,BLACK,save)
                button("load game",300,300,150,50,GREEN,DARKGREEN,BLACK,load)
                button("quit to desktop",300,400,150,50,GREEN,DARKGREEN,BLACK,terminate)
                pygame.display.flip()
        time.sleep(0.1)

def start_menu():
    global menu1, player
    menu1=TRUE
    screen.fill(WHITE) #fill screen white
    while menu1==TRUE:
        for event in pygame.event.get():
                button("new game",300,100,150,50,GREEN,DARKGREEN,BLACK,new_game)
                button("load game",300,200,150,50,GREEN,DARKGREEN,BLACK,load)
                button("quit to desktop",300,300,150,50,GREEN,DARKGREEN,BLACK,terminate)
                pygame.display.flip()
        time.sleep(0.1)
    map_name="map"+str(player[15])+".gif"
    background = pygame.image.load(os.path.join("textures",map_name))
    screen.blit(background, (0,0))
    pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------------------------------
def save():
    global player_class
    save_name=input("enter save name")
    filename = str(save_name)
    if not os.path.exists(os.path.join("Saves",filename)):
        os.makedirs(os.path.join("Saves",filename))
        f = open(os.path.join("Saves",filename,"location.txt"),"w")
        f.write(str(player_class))
        f.write('\n')
        f.write(str(player[15]))
        f.write("\n")
        f.write(str(playert.x))
        f.write("\n")
        f.write(str(playert.y))
        f.write("\n")
        f.write(str(player[7]))
        f.close()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Save not completed - a save already exists with this name", "error", 0)

def load():
    root = tix.Tk()

    def print_selected(args):
        global playert, player, image
        print('selected dir:', args) #print selected save
        f = open(os.path.join(args,"location.txt"),"r")
        class_type=f.readline()
        class_type = class_type[:-1]
        image=type_select(str(class_type))
        player[15]=int(f.readline())
        map_name="map"+str(player[15])+".gif" #add back background after file is selected
        background = pygame.image.load(os.path.join("textures",map_name))
        screen.blit(background, (0,0))
        playert.x=int(f.readline())
        playert.y=int(f.readline())
        player[7]=str(f.readline())
        print("image",class_type)
        f.close()
        menu_close()
        pygame.display.flip()
        root.destroy()

    def pathSelect():
        d = tix.DirSelectDialog(master=root, command=print_selected)
        d.popup()

    button = Button(root, text="select file", command=pathSelect)
    button.pack()

    root.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
hight=3
running=True
start_menu()
debug("game started",player)
print(player)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
                terminate()
                pygame.display.quit()
                running=False
                debug("game closed",player)
                break
        elif event.type == KEYDOWN:
            map_name="map"+str(player[15])+".gif"
            print(map_name)
            background = pygame.image.load(os.path.join("textures",map_name))
            screen.blit(background, (0,0))
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                movment_ok=collision_detection(playert.x,playert.y+cellSize,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.y!=580: #if play isnt at top of level
                        playert.y += cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        if ((player[15]-1)/hight).is_integer(): #is player at very top
                            print("cannot move off map")
                        else:
                            new_map("down",playert) #load new map
                            playert.y=0 #move player to top for new map

            elif key[pygame.K_UP]:
                movment_ok=collision_detection(playert.x,playert.y-cellSize,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.y!=0: #if play isnt at top of level
                        playert.y -= cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        if (player[15]/hight).is_integer(): #is player at very top
                            print("cannot move off map")
                        else:
                            new_map("up",playert) #load new map
                            playert.y=580 #move player to buttom for new map

            elif key[pygame.K_RIGHT]:
                movment_ok=collision_detection(playert.x+cellSize,playert.y,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.x!=780: #if play isnt on the right most map
                        playert.x += cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        if player[15]>hight**2-hight: #is player at very top
                            print( "cannot move off map")
                        else:
                            new_map("right",playert) #load new map
                            playert.x=0 #move player to left for new map

            elif key[pygame.K_LEFT]:
                movment_ok=collision_detection(playert.x-cellSize,playert.y,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.x!=0: #if play isnt on the left most map
                        playert.x -= cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        if player[15]<=hight: #is player at far left
                            print( "cannot move off map")
                        else:
                            new_map("left",playert) #load new map
                            playert.x=780 #move player to right for new map
            elif key[pygame.K_p]:
                print("paused")
                pause()
                map_name="map"+str(player[15])+".gif" #add back background after unpaused
                background = pygame.image.load(os.path.join("textures",map_name))
                screen.blit(background, (0,0))
            elif key[pygame.K_m]:
                menu()
                map_name="map"+str(player[15])+".gif" #add back background after unpaused
                background = pygame.image.load(os.path.join("textures",map_name))
                screen.blit(background, (0,0))
            clock.tick(10)
            screen.blit(image, (playert.x, playert.y))
            print(playert.x)
            print(playert.y)
            pygame.display.update()
            if internal_editor == TRUE:
                if key[pygame.K_b]:
                    f=open("blocked.txt","a")
                    to_write=str((playert.x, playert.y,player[15]))
                    f.write(str(to_write))
                    f.write("\n")
                    f.close()
                    print("added to blakced square list")
