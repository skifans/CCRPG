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
#cellSize=int(line3)
cellSize=20
line4=f.readline() #internal editor header
line5=f.readline() #internal editor value
line6=f.readline() #buttons header
line7=f.readline() #buttons value
line8=f.readline() #combat header
line9=f.readable() #combat value'
if int(line5)==1:
    print("Enternal editor enabled")
    internal_editor=TRUE
else:
    internal_editor=FALSE
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
screen=pygame.display.set_mode((0,0))

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
    sys.exit()

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
#vitality, endurance dexterity, intelligence, strength, weapon, auramor, name, exp, small orb, medium orb, large orb, mega orb, x cor, y cor, area
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
    global map_number
    map_number=player[15]
    return image

def classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja):
    global player, player_class, mana, mana_use   #moved global from the if statments to the top to cut down on the ammount needed
    print("What is you're name?")
    name = str(input("my name is:"))
    print("Choose you're class " + name)
    print(classes)
    player_class = str(input())
    player_class = player_class.lower() #added .lower() to make sure that the input was lowercase so it wasn't case sensitvie
    image=type_select(player_class) #loads player array and image
    player[7]=name
    mana = player[3]*2
    mana_use = mana
    print(mana)
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
#-------------------------------------------------------------------------------
def spell_image_blue_puff():
    count = 1
    for i in range(10):
        battle_ground = pygame.image.load(os.path.join("Combat","spells","blue_puff","blue_puff_"+str(count)+".gif"))
        count += 1
        screen.blit(battle_ground, (300,150))
        pygame.display.flip()
        time.sleep(.1)
    battle_ground = pygame.image.load(os.path.join("combat","LargewhiteTexture.gif")) #blank image for normal load
    screen.blit(battle_ground, (300,150))
    pygame.display.flip()

def attack_image_sword():
    count = 1
    for i in range(20):
        battle_ground = pygame.image.load(os.path.join("Combat","attacks","sword","sword_"+str(count)+".png"))
        count += 1
        screen.blit(battle_ground, (300,150))
        pygame.display.flip()
        time.sleep(.02)
    battle_ground = pygame.image.load(os.path.join("combat","LargewhiteTexture.gif")) #blank image for normal load
    screen.blit(battle_ground, (300,150))
    pygame.display.flip()

def attackgif(weapons):
    if weapons == "sword":
        #attack_image_sword() uncomented as I dont have the sword.png file
        print("sword")

def spellgif(spell):
    if spell[1] == 1:
        spell_image_blue_puff()
#-------------------------------------------------------------------------------

#defining the players turn
def playerturn(player,darkness):
    global combatover
    global ehp,eend,edex,eint,estr,php,pend,pdex,pint,pstr,pw,pa
    global pchoice
#-------------------------------------------------------------------------------
    spell = ["Blue fire", 1, 40]
    weapons = "sword"
#-------------------------------------------------------------------------------
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
        attackgif(weapons)
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
#-------------------------------------------------------------------------------
        spellgif(spell)
#-------------------------------------------------------------------------------
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
    statsetup (darkness,sakaretsu_armour,simple_katanna)
    no_combat=[2,3] #maps where combat will not be triggered
    if player[15] not in no_combat and combat_on==1:
        combatover = False
        background = pygame.image.load(os.path.join("backgrounds","combat_area.gif")) #load image for combat background
        screen.blit(background, (0,0)) #place this at 0,0
        you = pygame.image.load(os.path.join("combat","you.gif")) #load image for you
        screen.blit(you, (100,200)) #place this at (100,200)
#------------------------------------------------------------------------------------------------------------------------------
#        battle_ground = pygame.image.load(os.path.join("combat","whiteTexture.gif")) #blank image for normal load
#        screen.blit(battle_ground, (300,150))
#------------------------------------------------------------------------------------------------------------------------------
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
    global player, map_number
    hight=3 #the amount of vertical maps
    pygame.display.flip() #suppost to update whole map
    if direction=="up":
        move=player[15]/hight
        player[15]=player[15]+1
        map_number += 1
        if str(map_number) == "1":
            player[15] = map_number
        else:
            player[15] = random.randint(2,9)
    elif direction=="down":
        move=(player[15]-1)/hight
        player[15]=player[15]-1
        map_number -= 1
        if str(map_number) == "1":
            player[15] = map_number
        else:
            player[15] = random.randint(2,9)
    elif direction=="right":
        player[15]=player[15]+hight
        map_number += hight
        move=hight**2-player[15]
        player[15]=player[15]-hight
        if str(map_number) == "1":
            player[15] = 1
        else:
            player[15] = random.randint(2,9)
    elif direction=="left":
        player[15]=player[15]-hight
        map_number -= hight
        if str(map_number) == "1":
            player[15] = 1
        else:
            player[15] = random.randint(2,9)
    image_path="map"+str(player[15])+".gif"
    if os.path.isfile(image_path)==FALSE: #check that a map file exisits, if not then display an error message. Changing this to TRUE and moving to a new map will show the error message if you want to see it.
        img=pygame.image.load("map_error.gif")
        #screen=pygame.display.set_mode((0,0))
        screen.blit(img,(0,0))
    else:
        img=pygame.image.load(image_path)
        #screen=pygame.display.set_mode((0,0))
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
    #screen=pygame.display.set_mode((0,0)) uncomenting this lets fixes the screen not defined bug - but also causes problems displaying text if let uncommented.
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

    smallText = pygame.font.SysFont("freesansbold.ttf", 30) #load font
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
    save() #save a base copy of the game so that the deafult money and locations to load the save is created

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
                button("options",300,300,150,50,GREEN,DARKGREEN,BLACK,options)
                button("credits",300,400,150,50,GREEN,DARKGREEN,BLACK,credit)
                button("quit to desktop",300,500,150,50,GREEN,DARKGREEN,BLACK,terminate)
                pygame.display.flip()
        time.sleep(0.1)
    map_name="map"+str(player[15])+".gif"
    background = pygame.image.load(os.path.join("textures",map_name))
    screen.blit(background, (0,0))
    pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------------------------------
def credit():
    while menu1==TRUE:
        for event in pygame.event.get():
            screen.fill(WHITE)
            message_display("me-stuff",400,40,16,BLACK)
            message_display("you-things",400,60,16,BLACK)
            button("back to menu",300,400,150,50,GREEN,DARKGREEN,BLACK,start_menu)
            pygame.display.flip()
        time.sleep(0.1)

def options():
    while menu1==TRUE:
        for event in pygame.event.get():
            screen.fill(WHITE)
            message_display("You want to change things?",400,40,16,BLACK)
            message_display("why on earth?",400,60,16,BLACK)
            button("Dont save changes",150,400,200,50,GREEN,DARKGREEN,BLACK,start_menu)
            button("Dont save changes",450,400,200,50,GREEN,DARKGREEN,BLACK,start_menu)
            pygame.display.flip()
        time.sleep(0.1)

def save():
    global player_class,mana,mana_use
    save_name=input("enter save name")
    filename = str(save_name)
    if not os.path.exists(os.path.join("Saves",filename)):
        os.makedirs(os.path.join("Saves",filename)) #create folder
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
    if not os.path.exists(os.path.join("Saves",filename,"money_s.txt")):
        f = open(os.path.join("Saves",filename,"money_s.txt"),"w")
        f.write("60")
        money.append(60)
        f.close
    if not os.path.exists(os.path.join("Saves",filename,"money_m.txt")):
        f = open(os.path.join("Saves",filename,"money_m.txt"),"w")
        f.write("40")
        money.append(40)
        f.close
    if not os.path.exists(os.path.join("Saves",filename,"money_l.txt")):
        f = open(os.path.join("Saves",filename,"money_l.txt"),"w")
        f.write("20")
        money.append(20)
        f.close
    if not os.path.exists(os.path.join("Saves",filename,"money_x.txt")):
        f = open(os.path.join("Saves",filename,"money_x.txt"),"w")
        f.write("10")
        money.append(10)
        f.close
    f = open(os.path.join("Saves",filename,"stats.txt"),"w")
    f.write(str(player[0]))
    f.write("\n")
    f.write(str(player[1]))
    f.write("\n")
    f.write(str(player[2]))
    f.write("\n")
    f.write(str(player[3]))
    f.write("\n")
    f.write(str(player[4]))
    f.write("\n")
    f.write(str(player[8][0]))
    f.write("\n")
    f.write(str(player[8][1]))
    f.write("\n")
    f.write(str(player[8][2]))
    f.write("\n")
    f.write(str(mana))
    f.write("\n")
    f.write(str(mana_use))

def load():
    root = tix.Tk()

    def print_selected(args):
        global playert, player, image, player_class, money
        money=[]
        print('selected dir:', args) #print selected save
        folder=args.split("/")
        print("folder: ",folder[-1])

        f = open(os.path.join(args,"location.txt"),"r")
        location=f.readlines() #becomes an array, item 0 corosponds to line 1. Note that each item includes \n
        if len(location)==9: #.readlines seems to sometimes result in two different things, either ["x\n","\n","x\n","\n... or ["x\n","x\n",x\n"... by detecting the length we can work out which one, make sure to change this if you add new things to location.txt
            player_class=location[0]
            player_class = player_class[:-1] #clear the last charector (\n)
            image=type_select(str(player_class))
            location1=location[2]
            location1=location1[:-1]
            location1=int(location1)
            player[15]=location1

            playert.x=location[4] #get x cordinates dom
            playert.x=playert.x[:-1] #remove \n
            playert.x=int(playert.x)
            playert.y=location[6]
            playert.y=playert.y[:-1]
            playert.y=int(playert.y)
            player[7]=location[8] #name?
            player[7]=player[7][:-1]
        elif len(location)==5:
            player_class=location[0]
            player_class = player_class[:-1]
            image=type_select(str(player_class))
            location1=location[1]
            location1=location1[:-1]
            location1=int(location1)
            player[15]=location1

            playert.x=location[2] #get x cordinates dom
            playert.x=playert.x[:-1] #remove \n
            playert.x=int(playert.x)
            playert.y=location[3]
            playert.y=playert.y[:-1]
            playert.y=int(playert.y)
            player[7]=location[4] #name?
            player[7]=player[7][:-1]
        else:
            debug("data in array assitened from location.txt array is not 5 or 9 long")
            print("data in array assitened from location.txt array is not 5 or 9 long")

        f.close()
        f=open(os.path.join(args,"money_s.txt"),"r")
        money.append(int(f.readline()))
        f.close()
        f=open(os.path.join(args,"money_m.txt"),"r")
        money.append(int(f.readline()))
        f.close()
        f=open(os.path.join(args,"money_l.txt"),"r")
        money.append(int(f.readline()))
        f.close()
        f=open(os.path.join(args,"money_x.txt"),"r")
        money.append(int(f.readline()))
        f.close()

        f=open(os.path.join(args,"stats.txt"),"r")
        player[0]=int(f.readline())
        player[1]=int(f.readline())
        player[2]=int(f.readline())
        player[3]=int(f.readline())
        player[4]=int(f.readline())
        player[8][0]=int(f.readline())
        player[8][1]=int(f.readline())
        player[8][2]=int(f.readline())
        mana=int(f.readline())
        mana_use=int(f.readline())

        screen.fill(WHITE)
        map_name="map"+str(player[15])+".gif" #add back background after file is selected
        background = pygame.image.load(os.path.join("textures",map_name))
        screen.blit(background, (0,0))
        print(location)
        print("image",player_class)
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
#shop set up
#Arrays
global armour, weapons

clothing = []
armour = []
weapons = []

#Defalts
#Code Specific
currentHandItem = " "
currentArmour = " "

#Items - Examples for testing purposes. To be replaced with finished items.


#Messages
inventMessage = "You currently have " + str(weapons)
currentHandItemMessage = "You are currenty wielding a: " #+ str(weapons)
pickUpMessage = "You have picked up a "
dropItemMessage = "You have dropped a "
failedToEquipMessage = "Therefore you were unable to equip the item."
currentArmourMessage = "You are wearing: " #+ str(armour)
unEquipArmourMessage = "You have unequiped your armour."
unEquipWeaponMessage = "You have unequiped your weapon."

save_game_to_use="name-test2"
##money=[]
##f = open(os.path.join("Saves",save_game_to_use,"money_s.txt"),"r")
##s_money=f.read()
##f.close()
##f = open(os.path.join("Saves",save_game_to_use,"money_m.txt"),"r")
##m_money=f.read()
##f.close()
##f = open(os.path.join("Saves",save_game_to_use,"money_l.txt"),"r")
##l_money=f.read()
##f.close()
##f = open(os.path.join("Saves",save_game_to_use,"money_x.txt"),"r")
##x_money=f.read()
##f.close()
##money.append(int(s_money))
##money.append(int(m_money))
##money.append(int(l_money))
##money.append(int(x_money))

global inventry
inventry=[]
#------------------------------------------------------------------------------------------------------------------------------------------------
#shop functions
def is_number(to_check):
    if to_check.isdigit():
        is_number="TRUE"
    else:
        is_number="FALSE"
    return is_number

def is_text(to_check):
    #Not yet used-thought it might be useful
    if to_check.isdigit():
        is_number="TRUE"
    else:
        is_number="FALSE"
    return is_number

def money_reset(s_money, m_money, l_money, x_money, money):
        money.remove(money[3])
        money.remove(money[2])
        money.remove(money[1])
        money.remove(money[0])
        money.append(s_money)
        money.append(m_money)
        money.append(l_money)
        money.append(x_money)
        message_display("Your account has been sucsesfuly updated",400,40,16,WHITE)
        pygame.display.flip()
        return money

def change(money, type, amount):
    if type==("S"):
        x_money=money[3]
        l_money=money[2]
        m_money=money[1]
        s_money=amount
        money_reset(s_money, m_money, l_money, x_money, money)
    elif type==("M"):
        x_money=money[3]
        l_money=money[2]
        m_money=amount
        s_money=money[0]
        money_reset(s_money, m_money, l_money, x_money, money)
    elif type==("L"):
        x_money=money[3]
        l_money=amount
        m_money=money[1]
        s_money=money[0]
        money_reset(s_money, m_money, l_money, x_money, money)
    elif type==("X"):
        x_money=amount
        l_money=money[2]
        m_money=money[1]
        s_money=money[0]
        money_reset(s_money, m_money, l_money, x_money, money)
    else:
        print("Error - money type not recognised. Use capital S,M,L or X only for type veriable")
        return money

def amount(items, item_no):
    if  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][11]==0:
        ret=items[item_no][12]
    elif  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][12]==0:
        ret=items[item_no][11]
    elif  items[item_no][9]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        ret=items[item_no][10]
    elif  items[item_no][10]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        ret=items[item_no][9]
    else:
        place="error"
    return ret

def places(items, item_no):
    if  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][11]==0:
        place="X"
    elif  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][12]==0:
        place="L"
    elif  items[item_no][9]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        place="M"
    elif  items[item_no][10]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        place="S"
    else:
        place="error"
    return place

def equipItem(obj, name, pequip):
    global armour, weapons
    if obj == 0:
        weapons = name
        #Enter Addition To Stats (Waiting for finished weapons)
        screen.fill(BLACK)
        message_display(currentHandItemMessage + str(name) + ".",400,20,16,WHITE)
        pygame.display.flip()
        file = open(os.path.join("Saves",save_game_to_use,"equip0.txt"),"w")
        file.write(str(pequip))
        file.close()
        return weapons
    elif obj == 1:
        armour = name
        ##endurance += int(armour[1])
        #screen.fill(BLACK)
        message_display(currentArmourMessage + str(name) + ".",400,20,16,WHITE)
        pygame.display.flip()
        file=open(os.path.join("Saves",save_game_to_use,"equip1.txt"),"w")
        file.write(str(pequip))
        file.close()
        return armour
    elif obj==2:
        screen.fill(BLACK)
        message_display("clothing is not yet supported",400,20,16,WHITE)
        pygame.display.flip()

def pinventory():
    global inventry, decide, pdecide
    global armour, weapons
    screen.fill(BLACK)
    message_display("You are currently wearing: " + str(armour) + ". Your options are: unequip or equip",400,40,16,WHITE)
    pygame.display.flip()
    pdecide=input()
    if pdecide == "equip":
        if len(inventry)==0:
            screen.fill(BLACK)
            message_display("You havnt boughnt anything to equip",400,40,16,WHITE)
            pygame.display.flip()
        else:
            screen.fill(BLACK)
            message_display("Choose what you want to equip",400,40,16,WHITE)
            pygame.display.flip()
            length1=0
            y=20 #y position of first print
            screen.fill(BLACK)
            while length1<len(inventry):
                message_display("Item number "+str(length1)+" is "+inventry[length1][4],400,y,16,WHITE)
                pygame.display.flip()
                length1 = length1 + 1
                y=y+20 #gap inbetween each print
            pequip = input("Enter item number")
            try:
                pequip = int(pequip) #see if pequip is number
            except:
                pequip=len(inventry)+1 #if not make a number which will be found to trigger Item not found alert bellow
            if pequip<len(inventry):
                equipItem(inventry[pequip][6],inventry[pequip][4],pequip)
            else:
                screen.fill(BLACK)
                message_display("Item not found",400,40,16,WHITE)
                pygame.display.flip()
    elif pdecide == "unequip":
        armour = ""
        weapons = ""
        screen.fill(BLACK)
        message_display("Sucsess",400,40,16,WHITE)
        pygame.display.flip()

    else:
        screen.fill(BLACK)
        message_display("Didnt understand",400,40,16,WHITE)
        pygame.display.flip()

def save_item(to_write):
    file=open(os.path.join("Saves",save_game_to_use,"items.txt"),"a")
    file.write(to_write)
    file.write("\n")
    file.close()
    file=open(os.path.join("Saves",save_game_to_use,"amount.txt"),"r")
    amount=int(file.readline())
    file.close()
    file=open(os.path.join("Saves",save_game_to_use,"amount.txt"),"w")
    amount=int(amount)+1
    file.write(str(amount))
    file.close()
#------------------------------------------------------------------------------------------------------------------------------------------------
#shop items
#strengthm(0),endurancem(1),dexm(2),spellm(3),name(4),class(5),type(6),description(7),range(8),costs(9),costm(10),costl(11),costx(12)
#possible items to buy
# Armour List
#classes: warrior(1) mage(2) paladin(3) necromancer(4) barbarian(5) lancer(6) archer(7)

#-------------------------------------------------------------------------------
#standard armour

warrior_basic_armour = [0,30,0,0,"basic warrior armour",1,1,"basic armour for beginners",0,30,0,0,0]
warrior_medium_armour = [0,45,0,0,"medium warrior armour",1,1,"better armour for the more experienced",0,45,0,0,0]
warrior_strong_armour = [0,70,0,0,"strong warrior armour",1,1,"very good quality armour",0,70,0,0,0]
warrior_elite_armour = [0,100,0,0,"elite warrior armour",1,1,"elite armour of a great quality",0,0,10,0,0]
warrior_ultimate_armour = [0,500,0,0,"hero's armour",1,1,"great armour of a legendary warrior",0,0,0,5,0]

mage_basic_armour = [0,20,0,10,"basic mage armour",2,1,"basic armour for beginners",0,30,0,0,0]
mage_medium_armour = [0,30,0,15,"medium mage armour",2,1,"better armour for the more experienced",0,45,0,0,0]
mage_strong_armour = [0,50,0,20,"strong mage armour",2,1,"very good quality armour",0,70,0,0,0]
mage_elite_armour = [0,70,0,30,"elite mage armour",2,1,"elite armour of a great quality",0,0,10,0,0]
mage_ultimate_armour = [0,300,0,200,"ethereal cloak",2,1,"cloak of a magical ethereal mage",0,0,0,5,0]

paladin_basic_armour = [0,50,0,0,"basic paladin armour",3,1,"basic armour for beginners",0,30,0,0,0]
paladin_medium_armour = [0,65,0,0,"medium paladin armour",3,1,"better armour for the more experienced",0,45,0,0,0]
paladin_strong_armour = [0,100,0,"strong paladin armour",3,1,"very good quality armour",0,70,0,0,0]
paladin_elite_armour = [0,150,0,0,"elite paladin armour",3,1,"elite armour of a great quality",0,0,10,0,0]
paladin_ultimate_armour = [0,600,0,0,"golden armour",3,1,"not really made of gold, that would be expensive an impractical",0,0,0,5,0]

necromancer_basic_armour = [0,25,0,5,"basic necromancer armour",4,1,"basic armour for beginners",0,30,0,0,0]
necromancer_medium_armour = [0,40,0,5,"medium necromancer armour",4,1,"better armour for the more experienced",0,45,0,0,0]
necromancer_strong_armour = [0,55,0,15,"strong necromancer armour",4,1,"very good quality armour",0,70,0,0,0]
necromancer_elite_armour = [0,75,0,25,"elite necromancer armour",4,1,"elite armour of a gret quality",0,0,10,0,0]
necromancer_ultimate_armour = [0,350,0,150,"reaper's cloak",4,1,"the cloak of the lord of the dead",0,0,0,5,0]

barbarian_basic_armour = [0,20,0,0,"basic barbarian armour",5,1,"basic armour for beginners",0,30,0,0,0]
barbarian_medium_armour = [0,35,0,0,"medium barbarian armour",5,1,"better armour for the more experienced",0,45,0,0,0]
barbarian_strong_armour = [0,50,0,0,"strong barbarian armour",5,1,"very good quality armour",0,70,0,0,0]
barbarian_elite_armour = [0,70,0,0,"elite barbarian armour",5,1,"elite armour of a great quality",0,0,10,0,0]
barbarian_ultimate_armour = [0,400,0,0,"enraging armour",5,1,"a piece of armour that seems to enrage the wearer",0,0,10,0,0]

lancer_basic_armour = [0,10,0,0,"basic lancer armour",6,1,"basic armour for beginners",0,30,0,0,0]
lancer_medium_armour = [0,25,0,0,"medium lancer armour",6,1,"better armour for the more experienced",0,45,0,0,0]
lancer_strong_armour = [0,40,0,0,"strong laancer armour",6,1,"very good quality armour",0,70,0,0,0]
lancer_elite_armour = [0,60,0,0,"elite lancer armour",6,1,"elite armour of a great quality",0,0,10,0,0]
lancer_ultimate_armour = [0,300,0,0,"lancelord armor",6,1,"ancient lancer armour imbued with fire",0,0,0,5,0]

archer_basic_armour = [0,25,5,0,"basic archer armour",7,1,"basic armour for beginners",0,30,0,0,0]
archer_medium_armour = [0,40,10,0,"medium archer armour",7,1,"better armour for the more expeienced",0,45,0,0,0]
archer_strong_armour = [0,55,15,0,"strong archer armour",7,1,"very good quality armour",0,70,0,0,0]
archer_elite_armour = [0,80,20,0,"elite archer armour",7,1,"elite armour of a great qualit",0,0,10,0,0]
archer_ultimate_armour = [0,400,100,0,"armour of retribution",7,1,"will have your enemies quivering with fear!",0,0,0,5,0]

samurai_basic_armour = [0,25,0,0,"basic samurai armour",8,1,"basic armour for beginnners",0,30,0,0,0]
samurai_medium_armour = [0,35,0,0,"medium samurai armour",8,1,"better armour for the more experienced",0,45,0,0,0]
samurai_strong_armour = [0,50,0,0,"strong samurai armour",8,1,"very good quality armour",0,70,0,0,0]
samurai_elite_armour = [0,70,0,0,"elite samurai armour",8,1,"elite armour of a great quality",0,0,10,0,0]
samurai_ultimate_armour = [100,200,100,0,"crimson winged armour",8,1,"winged armour of crimson, that once belonged to a legendary shogun",0,0,0,5,0]

ninja_basic_armour = [0,20,5,0,"basic ninja armour",9,1,"basic armour for beginners",0,30,0,0,0]
ninja_medium_armour = [0,30,10,0,"medium ninja armour",9,1,"better armour for the more experienced",0,45,0,0,0]
ninja_strong_armour = [0,40,20,0,"strong ninja armour",9,1,"very good quality armour",0,70,0,0,0]
ninja_elite_armour = [0,60,30,0,"elite ninja armour",9,1,"elite armour of a great quality",0,0,10,0,0]
ninja_ultimate_armour = [0,300,0,200,"suit of invisibility",9,1,"makes you super hard to hit",0,0,0,5,0]

#standard weapons

warrior_basic_weapon = [30,0,0,0,"basic warrior sword",1,0,"a basic sword for beginners",0,30,0,0,0]
warrior_medium_weapon = [45,0,0,0,"medium warrior sword",1,0,"a better sword for the more experienced",0,45,0,0,0]
warrior_strong_weapon = [70,0,0,0,"strong warrior sword",1,0,"a very good quality sword",0,70,0,0,0]
warrior_elite_weapon = [100,0,0,0,"elite warrior sword",1,0,"an elite sword of a great quality",0,0,10,0,0]
warrior_ultimate_weapon = [500,0,0,0,"claymore",1,0,"a sword so big only a select few can use it",0,0,0,5,0]

mage_basic_weapon = [0,0,0,30,"basic mage wand",2,0,"a basic wand for beginners",0,30,0,0,0]
mage_medium_weapon = [0,0,0,45,"medium mage wand",2,0,"a better wand for the more experienced",0,45,0,0,0]
mage_strong_weapon = [0,0,0,70,"strong mage wand",2,0,"a very good quality wand",0,70,0,0,0]
mage_elite_weapon = [0,0,0,100,"elite mage wand",2,0,"an elite wand of a great quality",0,0,100,0,0]
mage_ultimate_weapon = [0,0,0,500,"darkness staff",2,0,"the power to command dark matter is pretty cool",0,0,0,5,0]

paladin_basic_weapon = [10,0,0,0,"basic paladin hammer",3,0,"a basic hammer for beginners",0,30,0,0,0]
paladin_medium_weapon = [25,0,0,0,"medium paladin hammer",3,0,"a better hammer for the more experienced",0,45,0,0,0]
paladin_strong_weapon = [40,0,0,0,"strong paladin hammer",3,0,"a very good quality hammer",0,70,0,0,0]
paladin_elite_weapon = [50,0,0,0,"elite paladin hammmer",3,0,"an elite hammer of great quality",0,0,10,0,0]
paladin_ultimate_weapon = [400,0,0,0,"light's fury",3,0,"shoots lightning. what more is needed?",0,0,0,10,0]

necromancer_basic_weapon = [0,5,0,25,"basic necromancer staff",4,0,"a basic staff for beginners",0,30,0,0,0]
necromancer_medium_weapon = [0,10,0,35,"medium necromancer staff",4,0,"a better staff for the more experienced",0,45,0,0,0]
necromancer_strong_weapon = [0,15,0,55,"strong necromancer staff",4,0,"a very good quality staff",0,70,0,0,0]
necromancer_elite_weapon = [0,20,0,80,"elite necromancer staff",4,0,"an elite staff of a great quality",0,0,10,0,0]
necromancer_ultimate_weapon = [0,100,0,400,"demon scythe",4,0,"a weapon that holds the secret to summoning chaos demons",0,0,0,5,0]

barbarian_basic_weapon = [40,0,0,0,"basic barbarian axe",5,0,"a basic axe for beginners",0,30,0,0,0]
barbarian_medium_weapon = [55,0,0,0,"medium barbarian axe",5,0,"a better axe for the more experienced",0,45,0,0,0]
barbarian_strong_weapon = [90,0,0,0,"strong barbarian axe",5,0,"a very good quality axe",0,70,0,0,0]
barbarian_elite_weapon = [130,0,0,0,"elite barbarian axe",5,0,"an elite axe of a great quality",0,0,10,0,0]
barbarian_ultimate_weapon = [600,0,0,0,"axe of the dragon king",5,0,"an ancient axe from ages past",0,0,0,5,0]

lancer_basic_weapon = [30,0,20,0,"basic lancer lance",6,0,"a basic lance for beginners",0,30,0,0,0]
lancer_medium_weapon = [40,0,25,0,"medium lancer lance",6,0,"a better lance for the more experienced",0,45,0,0,0]
lancer_strong_weapon = [55,0,45,0,"strong lancer lance",6,0,"a very good quality lance",0,70,0,0,0]
lancer_elite_weapon = [80,0,60,0,"elite lancer lance",6,0,"an elite lance of a great quality",0,0,10,0,0]
lancer_ultimate_weapon = [500,0,200,0,"spear of the piercer",6,0,"belonged to a titan in ages past",0,0,0,5,0]

archer_basic_weapon = [10,5,15,0,"basic archer bow",7,0,"a basic bow for beginners",0,30,0,0,0]
archer_medium_weapon = [15,10,20,0,"medium archer bow",7,0,"a better bow for the more experienced",0,45,0,0,0]
archer_strong_weapon = [20,15,35,0,"strong archer bow",7,0,"a very good quality bow",0,70,0,0,0]
archer_elite_weapon = [30,25,45,0,"elite archer bow",7,0,"an elite bow of a great quality",0,0,10,0,0]
archer_ultimate_weapon = [150,125,225,0,"elven bow",7,0,"always the best bows in any movie or game",0,0,0,5,0]

samurai_basic_weapon = [20,0,15,0,"basic samurai katana",8,0,"a basic katana for beginners",0,30,0,0,0]
samurai_medium_weapon = [30,0,25,0,"medium samurai katana",8,0,"a better katana for the more experienced",0,45,0,0,0]
samurai_strong_weapon = [50,0,40,0,"strong samurai katana",8,0,"a very good quality katana",0,70,0,0,0]
samurai_elite_weapon = [70,0,60,0,"elite samurai katana",8,0,"an elite katana of a great quality",0,0,10,0,0]
samurai_ultimate_weapon = [300,0,300,0,"two handed katana",8,0,"a katana that is specially designed to be wielded with both hands",0,0,0,5,0]

ninja_basic_weapon = [10,0,35,0,"basic ninja kama",9,0,"a basic kama for beginners",0,30,0,0,0]
ninja_medium_weapon = [20,0,30,0,"medium ninja kama",9,0,"a better kama for the more experienced",0,45,0,0,0]
ninja_strong_weapon = [30,0,50,0,"strong ninja kama",9,0,"a very good quality kama",0,70,0,0,0]
ninja_elite_weapon = [45,0,65,0,"elite ninja kama",9,0,"an elite kama of a great quality",0,0,10,0,0]
ninja_ultimate_weapon = [250,0,350,0,"karma kama",9,0,"a weapon imbued with a spirit of justice",0,0,0,5,0]

#custom armour

warrior_spiked_armour = [75,100,25,0,"spiked armour",1,1,"damages everything that touches you",0,0,20,0,0]
warrior_enchanted_armour = [50,100,0,0,"enchanted armour",1,1,"armour that stops a lot of damage",0,150,0,0,0]
warrior_stone_armour = [-50,700,-150,0,"stone armour",1,1,"it's heavy but it works",0,0,0,70,0]
warrior_simple_armour = [0,50,0,0,"simple armour",1,1,"cheap, yet still effective armour",0,50,0,0,0]
warrior_old_iron_armour = [0,100,0,0,"old iron armour",1,1,"armour taken from an ancient kingdom",0,100,0,0,0]

mage_magic_armour = [0,200,0,0,"magic armour",2,1,"enchanted armour designed to stop most damage",0,0,20,0,0]
mage_power_armour = [0,300,0,100,"one shot armour",2,1,"armour that helps increase magic power",0,0,40,0,0]
mage_dex_armour = [0,100,100,100,"magic armour of dexterity",2,1,"armour that supports magic and speed",0,0,30,0,0]
mage_oneshotarmour = [0,0,0,750,"one shot armour",2,1,"armour designed to help kill enemies quickly",0,0,75,0,0]
mage_chaos_armour = [0,60,0,60,"chaos armour",2,1,"armour of an ancient sorcerer, but most of it's power has faded",0,0,120,0,0]

paladin_grace_armour = [25,75,100,0,"armour of grace",3,1,"paladin armour that supports fast movement and graceful strikes",0,0,20,0,0]
paladin_blessed_armour = [150,150,100,0,"armour of the blessed",3,1,"armour that supports heavy defense and strikes",0,0,40,0,0]
paladin_the_wall = [0,1000,0,0,"the wall",3,1,"the best protection",0,0,0,10,0]
paladin_steel_armour = [0,200,0,0,"steel armour",3,1,"simple armour that simply works",0,200,0,0,0]
paladin_shield_armour = [0,300,0,0,"shield armour",3,1,"made of shields, but not so practical",0,0,30,0,0]

necromancer_dark_cloak = [0,100,200,100,"dark cloak",4,1,"a lightweight shroud that allows the wearer to avoid attacks",0,0,20,0,0]
necromancer_wraith_armour = [100,200,0,100,"wraith armour",4,1,"extremly powerful armour of the dark lords",0,0,40,0,0]
necromancer_black_armour = [0,500,0,0,"black armour",4,1,"armour to nullify most damage",0,0,0,5,0]
necromancer_black_steel_armour = [0,80,0,0,"black steel armour",4,1,"simple steel armour for necromancers",0,80,0,0,0]
necromancer_ghost_armour = [0,30,0,0,"ghost armour",4,1,"armour of a ghost, that isn't too useful",0,30,0,0,0]

barbarian_endurance_armour = [50,150,0,0,"endurance armour",5,1,"for the fighter who wishes to survive",0,0,20,0,0]
barbarian_flame_armour = [150,200,50,0,"flame armour",1,1,"damages everything every turn",0,0,40,0,0]
barbarian_hard_leather_armour = [10,30,10,0,"hard leather armour",5,1,"simple light armour",0,50,0,0,0]
barbarian_white_steel_armour = [20,80,0,0,"white steel armour",5,1,"simple armour for barbarians",0,100,0,0,0]
barbarian_brass_armour = [0,70,0,0,"brass armour",5,1,"armour sacred to the lamest god ever",0,70,0,0,0]

lancer_speed_armour = [50,0,150,0,"armour of speed",6,1,"gotta go fast",0,0,20,0,0]
lancer_protection_armour = [100,200,100,0,"protecting armour",6,1,"for the lancer who doesn't wish to die",0,0,40,0,0]
lancer_woven_armour = [20,20,20,0,"woven armour",6,1,"armour made of leather woven with steel",0,60,0,0,0]
lancer_ice_armour = [0,200,0,0,"ice armour",6,1,"good solid armour made of ice (but useless against fire)",0,0,20,0,0]
lancer_white_iron_armour = [0,250,50,0,"white iron armour",6,1,"white armour is rare, so this armour is too",0,300,0,0,0]

archer_frost_armour = [25,150,25,0,"frost armour",7,1,"armour that provides a shield of unbreaking ice for it's wearer",0,0,20,0,0]
archer_agility_armour = [0,0,0,400,"armour of agility",7,1,"armour for the archer who wishes to inflict critical damage",0,0,40,0,0]
archer_ash_armour = [0,20,20,0,"ash armour",7,1,"tattered armour of one who escaped a volcano",0,40,0,0,0]
archer_frost_armour = [0,100,0,900,"frost armour",7,1,"this armour is imbued with magical frost with a strange power",0,0,0,10,0]
archer_black_leather_armour = [0,150,150,0,"black leather armour",7,1,"designed for thieves, loved by archers",0,0,30,0,0]

samurai_daredevil_armour = [600,0,100,0,"daredevil armour",8,1,"armour the imbues the wearer with an ancient madness",0,0,0,8,0]
samurai_sakaretsu_armour = [50,30,20,0,"sakaretsu armour",8,1,"armour that increases offensive capability",0,0,10,0,0]
samurai_emperor_armour = [0,80,0,0,"ermour of an emperor",8,1,"armour of an emperor that united an ancient kingdom, designed purely for personal defence",0,80,0,0,0]
samurai_ronin_armour = [50,30,0,0,"ronin armour",8,1,"armour of an outcast samurai, this armour is designed for offensive power",0,80,0,0,0]
samurai_ebon_armour = [0,50,50,0,"purple armour",8,1,"an ancient set of purple armour that once belonged to a strong samurai",0,0,10,0,0]
samurai_blue_armour = [50,0,50,0,"blue armour",8,1,"an ancient set of blue armour that once belonged to an agile samurai",0,0,10,0,0]
samurai_orange_armour = [100,0,0,0,"orange armour",8,1,"an ancient set of orange armour that once belonged to a dangerous samurai",0,0,10,0,0]
samurai_green_armour = [10,0,90,0,"green armour",8,1,"an ancient set of green armour that once belonged to a skilled samurai",0,0,10,0,0]
samurai_yellow_armour = [55,0,45,0,"yellow armour",8,1,"an ancient set of yellow armour that once belonged to a visionary samurai",0,0,10,0,0]
samurai_red_armour = [0,30,0,70,"red armour",8,1,"an ancient set of red armour that once belonged to a crazy samurai",0,0,10,0,0]
samurai_battle_worn_armour = [50,50,50,50,"old samurai armour",8,1,"battle-worn armour of deepest green, that once belonged to a legenadary samurai chancellor",0,0,20,0,0]

ninja_light_kyu_gi = [0,150,50,0,"light kyu gi",9,1,"a light gi for ninjas",0,0,20,0,0]
ninja_heavy_kyu_gi = [0,200,0,0,"heavy kyu gi",9,1,"a heavy gi for ninjas",0,0,20,0,0]
ninja_light_dan_gi = [0,300,100,0,"light dan gi",9,1,"a light gi for elite ninjas",0,0,40,0,0]
ninja_heavy_dan_gi = [0,400,0,0,"heavy dan gi",9,1,"a heavy gi for elite ninjas",0,0,40,0,0]
ninja_darkness_armour = [0,0,600,0,"armour of darkness",9,1,"armour that stealths the user",0,0,0,6,0]
ninja_cloth_armour = [0,60,40,0,"cloth armour",9,1,"light armour for ease of movement",0,100,0,0,0]

#custom weapons

warrior_cleaver = [100,40,60,0,"the cleaver",1,0,"a giant meat cleaver",0,0,20,0,0]
warrior_voltsword = [240,0,160,0,"the voltblade",1,0,"a sword imbued with electricity",0,0,40,0,0]
warrior_balanced_sword = [30,30,30,30,"balanced blade",1,0,"this blade is made with perfect balance in all things",0,120,0,0,0]
warrior_goddess_sword = [35,15,0,0,"goddess blade",1,0,"a sword of a goddess who sacrificed her powers to become human",0,50,0,0,0]
warrior_sword_of_winds = [15,35,0,0,"sword of winds",1,0,"an ancient sword with a faint airy power",0,50,0,0,0]
warrior_sword_of_ages = [15,0,0,35,"sword of ages",1,0,"a sword from a land warped by time",0,50,0,0,0,]
warrior_silver_sword = [1000,0,1000,0,"silver sword",1,0,"a sword that once belonged to a knight who could defend his city against anyone",0,0,0,20,0]

mage_weaving_wand = [70,0,30,100,"weaving wand",2,0,"for the mage who wishes to weave in attacks between spells",0,0,20,0,0]
mage_dragon_wand = [0,0,100,300,"dragon wand",2,0,"a wand made from dragon bones",0,0,40,0,0]
mage_serpent_wand = [0,0,200,500,"serpent wand",2,0,"a wand the fires spells as fast as a viper, and has the deadliness to match",1,0,70,0,0]
mage_one_shot_wand = [0,0,0,750,"one shot wand",2,0,"a wand that is designed to kill an enemy quickly",0,0,75,0,0]
mage_blue_wand = [200,150,150,0,"blue wand",2,0,"a wand taken from a blue eyed monster",0,0,0,5,0,]
mage_corrupted_wand = [0,0,50,100,"corrupted wand",2,0,"a wand touched by a strange power",0,150,0,0,0]
mage_apocalypse_wand = [0,0,500,1500,"apocalypse wand",2,0,"a wand with insane power",0,0,0,20,0]

paladin_light_hammer = [80,120,0,0,"light hammer",3,0,"a hammer with a holy aura",0,0,20,0,0]
paladin_lightbringer = [200,100,100,0,"the lightbringer",3,0,"a sword imbued with a holy light that rips through enemies",0,0,40,0,0]
paladin_hammer_of_dawn = [40,0,0,0,"the hammer of dawn",3,0,"this hammer hits like the first rays of dawn, on a planet with 3 suns",0,0,4,0,0]
paladin_holy_axe = [100,0,0,0,"holy axe",3,0,"an axe imbued with holy light",0,0,10,0,0]
paladin_life_hammer = [200,200,0,0,"life hammer",3,0,"the power of this hammer can bring poeple back from the dead",0,0,0,4,0]
paladin_heavy_hammer = [200,0,0,0,"heavy hammer",3,0,"a big hammer for paladins",0,150,0,0,0]
paladin_hammer_of_judgement = [1000,1000,0,0,"hammer of judgement",3,0,"the best hammer around",0,0,0,20,0]

necromancer_dark_shield = [0,150,0,50,"dark shield",4,0,"for the necromancer who wishes to be hard to kill",0,0,20,0,0]
necromancer_shadow_blade = [200,100,0,100,"shadow blade",4,0,"a blade tainted by darkness",0,0,40,0,0]
necromancer_crystal_ball = [0,50,0,50,"crystal ball",4,0,"a simple crystal ball that increases magic power",0,0,10,0,0]
necromancer_black_staff = [0,0,0,150,"black staff",4,0,"a necromancer staff made of black iron",0,0,15,0,0]
necromancer_dimension_blade = [35,45,0,0,"dimension blade",4,0,"a sword from a different dimension with an eerie power",0,80,0,0,0]
necromancer_bone_staff = [0,0,0,200,"bone staff",4,0,"a staff made from a demon's bone",0,0,20,0,0]
necromancer_night_staff = [0,1000,0,2000,"night staff",4,0,"a staff only for the best of necromancers",0,0,0,30,0]

barbarian_dragon_sword = [50,50,100,0,"dragon sword",5,0,"a lightweight sword taken from a dragon's treasure",0,0,20,0,0]
barbarian_bloodaxe = [600,0,0,0,"blood axe",5,0,"a huge axe owned by a very strong warrior",0,0,60,0,0]
barbarian_battle_axe = [40,20,0,0,"battle axe",5,0,"a simple battle axe",0,60,0,0,0]
barbarian_twin_axe = [200,0,200,0,"twin axe",5,0,"a pole arm with an axe blade at each end",0,0,40,0,0]
barbarian_hammer = [600,0,-100,0,"barbarian's hammer",5,0,"a hammer large and heavy enough to crush foes",0,0,50,0,0]
barbarian_dragon_blade = [2000,0,2000,0,"dragonslayer blade",5,0,"a curved sword of a barbarian who busted many a dragon",0,0,0,40,0]
barbarian_hatchets = [200,0,0,0,"hatchets",5,0,"two hatchets for barbarians",0,0,20,0,0]

lancer_trident = [70,70,60,0,"the trident",6,0,"protects the user with a shield of water",1,0,20,0,0]
lancer_glaive = [300,0,300,0,"the glaive",6,0,"a pole-arm designed to be slashed rather than thrusted",1,0,60,0,0]
lancer_spear = [200,50,150,0,"spear",6,0,"spears are less damaging than lances, but safer",0,0,40,0,0]
lancer_sting = [50,0,250,0,"the sting",6,0,"a curved spear with a wickedly sharp blade",0,0,30,0,0]
lancer_conquest_lance = [350,300,350,0,"conquest lance",6,0,"lance of a rider who rode a white horse",1,0,0,10,0]
lancer_war_lance = [500,0,500,0,"war lance",6,0,"lance of a rider who rode a red horse",1,0,0,10,0]
lancer_famine_lance = [250,500,250,0,"famine lance",6,0,"lance of a rider who rode a black horse",1,0,0,10,0]
lancer_death_lance = [1000,0,0,0,"death lance",6,0,"lance of a rider who rode a pale green horse",1,0,0,10,0]
lancer_oni_lance = [4000,0,1000,0,"oni's lance",6,0,"the lance of one of four riders, but not the four you're thinking of",1,0,0,50,0]

archer_crossbow = [200,0,0,0,"crossbow",7,0,"similar to a bow, but more mechanical and requires less skill",1,0,20,0,0]
archer_strong_bow = [500,0,-200,0,"strong bow",7,0,"fires heavy shots that knock targets back",1,0,30,0,0]
archer_hunters_bow = [100,0,350,0,"hunter's bow",7,0,"a bow built for dexterity",1,0,45,0,0]
archer_hermes_bow = [50,-20,30,0,"bow of hermes",7,0,"a bow that delivers a message, a painful message",1,0,40,0,0]
archer_explosive_bow = [500,0,60,0,"explosive bow",7,0,"a bow that fires arrows that explode upon hitting their target",1,0,56,0,0]
archer_black_bow = [100,0,700,0,"black bow",7,0,"a bow made of a very srong wood that lets it hit from miles away",1,0,80,0,0]
archer_greatbow = [600,0,0,0,"greatbow",7,0,"an extremely heavy bow that fires extremely heavy arrows that pack a huge punch",1,0,60,0,0]
archer_shotgun = [2000,0,0,0,"the shotgun",7,0,"not really a shotgun, just a crossbow that fires 6 bolts at once",1,0,0,20,0]

samurai_dark_katana = [100,0,100,0,"dark katana",8,0,"a katana that emits a dark aura",0,0,20,0,0]
samurai_light_katana = [200,100,100,0,"light katana",8,0,"a katana that emits a holy aura",0,0,40,0,0]
samurai_gold_katana = [30,10,30,0,"golden katana",8,0,"a katana made of gold",0,70,0,0,0]
samurai_yari = [90,0,60,0,"yari",8,0,"a spear with a larger balde, for samurais",0,150,0,0,0]
samurai_wakizashi = [250,0,250,0,"wakizashi",8,0,"a shortened katana for quicker strikes",0,0,50,0,0]
samurai_naginata = [200,0,200,"naginata",8,0,"a curved blade on a polearm, for samurais",0,0,40,0,0]
samurai_aluminium_katana = [1000,500,1500,0,"aluminium katana",8,0,"a katana made from magically enhanced aluminium, in respect to a famed samurai",0,0,0,30,0]

ninja_jo_staff = [50,50,100,0,"jo staff",9,0,"a short staff for ninjas",0,0,20,0,0]
ninja_bo_staff = [100,100,200,0,"bo staff",9,0,"a long staff for ninjas",0,0,40,0,0]
ninja_extended_bo_staff = [400,0,100,0,"extended bo staff",9,0,"a staff that is good at range but bad up close",1,0,50,0,0]
ninja_surikens = [300,0,300,0,"surikens",9,0,"surikens for ninjas",1,0,60,0,0]
ninja_kunai = [500,0,500,0,"kunai",9,0,"can be used up close or at range",1,0,0,1,0]
ninja_dagger = [20,0,80,0,"dagger",9,0,"a dagger for sneaky ninjas",0,100,0,0,0]
ninja_tashi = [40,0,160,0,"tashi",9,0,"a short katana for ninjas rather than samurais",0,200,0,0,0]

berserkers_band = [250,-50,0,0,"Beserkers band of destruction",0,2,"A long dead berserkers band that was enchanted with the power of satan",0,0,0,0,1]
priest_band = [0,100,0,50,"Priests saintly miracle band",0,2,"A saintly clerics lost wedding band",0,0,0,0,1]
#this needs to heal you for 25
Fire_gem_circlet = [0,0,50,150,"Fire gem circlet",0,2,"A gem formed in the fires of hell mounted onto a malachite circlet",0,0,0,0,1]
major_ring = [50,50,50,50,"Major ring of stat boosting",0,2,"A ring to make your power level over 9000",0,0,0,0,1]
ring_of_random_change = [0,0,0,0,"Ring of random change",0,2,"A ring that causes abnormalities in the atmosphere like hats coming out of rabbits",0,0,0,0,1]
#should do random things in battle like kill you or the enemy instantly
blinding_cranium_crab = [0,0,0,0,"Blinding cranium crab",0,2,"A crab for your cranium that jumps and blinds your foe lowering dexterity",0,0,0,0,1]
#should lower enemy dexterity
swiss_army_claymore = [50,0,50,0,"Swiss army claymore",0,2,"A fold out sword application for a strange swiss army knife",0,0,0,0,1]
#needs to make you go second every second turn and then give a strength boost of 200
arrow_target = [0,0,100,0,"Archery circlet of the pure archer",0,2,"An elven kings son once owned this crown and went on to defeat a dark lord",0,0,0,0,1]
#Should give a random chance to mean that all attacks by the player that turn become critical
blight_sludge = [0,0,0,0,"Blight sludge",0,2,"Some sludge taken from a poison riddled place that emanates death",0,0,0,0,1]
#Should deal poison damage over time to the enemy
overpowered_stick = [1000,1000,1000,1000,"The overpowered stick of doom",0,2,"A stick blessed with the power of bad coding",0,0,0,0,1]
#can only be used in one battle then it breaks and can't be used in boss battles
boss_shield = [0,200,0,0,"Boss shield of death",0,2,"A shield that is so big we didn't want to code it so here's a buckler",0,0,0,0,1]
#should protect from all damage for one turn once per battle (doesn't defend against magic)
sleepy_stick = [0,0,0,0,"sleepy stick",0,2,"a cursed squirrel on a stick",0,0,0,0,1]
#gives a chance to send enemies to sleep on a basic attack
lol = [50,50,50,50,"LOL",0,2,"An annoying snail because snails",0,0,0,0,1]
#should say lol at random points in battle
necrotic_bone = [0,0,100,50,"Necrotic bone",0,2,"A bone that was forced into a reverse body",0,0,0,0,1]
#should mean that your healing spells deal damage to the enemy instead.
mr_tiddles = [0,0,50,0,"Mr Tiddles",0,2,"A cat that is so buff that he buffs you!!!",0,0,0,0,1]
#should give you attack buffs based on your endurance

shop = []

items=[warrior_basic_armour,warrior_medium_armour,warrior_strong_armour,warrior_elite_armour,warrior_ultimate_armour,mage_basic_armour,mage_medium_armour,mage_strong_armour,mage_ultimate_armour,paladin_basic_armour,paladin_medium_armour,paladin_strong_armour,paladin_elite_armour,paladin_ultimate_armour,necromancer_basic_armour,necromancer_medium_armour,necromancer_strong_armour,necromancer_elite_armour,necromancer_ultimate_armour,barbarian_basic_armour,barbarian_medium_armour,barbarian_strong_armour,barbarian_elite_armour,barbarian_ultimate_armour,lancer_basic_armour,lancer_medium_armour,lancer_strong_armour,lancer_elite_armour,lancer_ultimate_armour,archer_basic_armour,archer_medium_armour,archer_strong_armour,archer_elite_armour,archer_ultimate_armour,warrior_basic_weapon,warrior_medium_weapon,warrior_strong_weapon,warrior_elite_weapon,warrior_ultimate_weapon,mage_basic_weapon,mage_medium_weapon,mage_strong_weapon,mage_elite_weapon,mage_ultimate_weapon] #maximum defininf length
items2=[warrior_spiked_armour,warrior_enchanted_armour,warrior_stone_armour,warrior_simple_armour,warrior_old_iron_armour,mage_magic_armour,mage_power_armour,mage_dex_armour,mage_oneshotarmour,mage_chaos_armour,paladin_grace_armour,paladin_blessed_armour,paladin_the_wall,paladin_steel_armour,paladin_shield_armour,necromancer_dark_cloak,necromancer_wraith_armour,necromancer_black_armour,necromancer_black_steel_armour,necromancer_ghost_armour,barbarian_endurance_armour,barbarian_flame_armour,barbarian_hard_leather_armour,barbarian_white_steel_armour,barbarian_brass_armour,lancer_speed_armour,lancer_protection_armour,lancer_woven_armour,lancer_ice_armour,lancer_white_iron_armour,archer_frost_armour,archer_agility_armour,archer_ash_armour,archer_frost_armour,archer_black_leather_armour,samurai_daredevil_armour,samurai_sakaretsu_armour,samurai_emperor_armour,samurai_ronin_armour,samurai_ebon_armour,samurai_blue_armour,samurai_orange_armour,samurai_green_armour]
items3=[samurai_yellow_armour,samurai_red_armour,samurai_battle_worn_armour,ninja_light_kyu_gi,ninja_heavy_kyu_gi,ninja_light_dan_gi,ninja_heavy_dan_gi,ninja_darkness_armour,ninja_cloth_armour,warrior_cleaver,warrior_voltsword,warrior_balanced_sword,warrior_goddess_sword,warrior_sword_of_winds,warrior_sword_of_ages,warrior_silver_sword,mage_weaving_wand,mage_dragon_wand,mage_serpent_wand,mage_one_shot_wand,mage_blue_wand,mage_corrupted_wand,mage_apocalypse_wand,paladin_light_hammer,paladin_lightbringer,paladin_hammer_of_dawn,paladin_holy_axe,paladin_life_hammer,paladin_heavy_hammer,paladin_hammer_of_judgement,necromancer_dark_shield,necromancer_shadow_blade,necromancer_crystal_ball,necromancer_black_staff,necromancer_dimension_blade,necromancer_bone_staff,necromancer_night_staff,barbarian_dragon_sword,barbarian_bloodaxe,barbarian_battle_axe,barbarian_twin_axe,barbarian_hammer,barbarian_dragon_blade,barbarian_hatchets,lancer_trident,lancer_glaive]
items4=[lancer_spear,lancer_sting,lancer_conquest_lance,lancer_war_lance,lancer_famine_lance,lancer_death_lance,lancer_oni_lance,archer_crossbow,archer_strong_bow,archer_hunters_bow,archer_hermes_bow,archer_explosive_bow,archer_black_bow,archer_greatbow,archer_shotgun,samurai_dark_katana,samurai_light_katanai,samurai_gold_katana,samurai_yari,samurai_wakizashi,samurai_naginata,samurai_aluminium_katana,ninja_jo_staff,ninja_bo_staff,ninja_extended_bo_staff,ninja_surikens,ninja_kunai,ninja_dagger,ninja_tashi]
items.extend(items2)
items.extend(items3)
items.extend(items4)

items_accsesorys=[berserkers_band,priest_band,Fire_gem_circlet,major_ring,ring_of_random_change,blinding_cranium_crab,swiss_army_claymore,arrow_target,blight_sludge,overpowered_stick,boss_shield,sleepy_stick,lol,necrotic_bone,mr_tiddles] #add acsessorys to new array
items.extend(items_accsesorys) #add accsesorys to end of items array


file=open(os.path.join("Saves",save_game_to_use,"amount.txt"),"r")
amount1=int(file.readline())
file.close()
f=open(os.path.join("Saves",save_game_to_use,"items.txt"),"r")
amount1=amount1-1
for i in range (amount1):
    item=f.readline()
    inventry.append(items[int(item)])
f.close()

item_no=0
while item_no < len(items):
    shop.append(str(items[item_no]))
    item_no=item_no+1

##file=open(os.path.join("Saves",save_game_to_use,"equip0.txt"),"r")
##pequip=int(file.readline())
##equipItem(inventry[pequip][6],inventry[pequip][4],pequip)
##file.close()
##file=open(os.path.join("Saves",save_game_to_use,"equip0.txt"),"r")
##pequip=int(file.readline())
##equipItem(inventry[pequip][6],inventry[pequip][4],pequip)
##file.close()

prices=[]

item_no=0
while item_no < len(items):
    place=amount(items, item_no)
    item_no=item_no+1
    prices.append(place)

place=[]

item_no=0
while item_no < len(items):
    places1=places(items, item_no)
    item_no=item_no+1
    place.append(places1)

store=[]
store.append(shop)
store.append(prices)
store.append(place)

#length of shop
length=len(store[1])
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
            if key[pygame.K_DOWN] or key[pygame.K_s]:
                movment_ok=collision_detection(playert.x,playert.y+cellSize,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.y!=580: #if play isnt at top of level
                        playert.y += cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        new_map("down",playert) #load new map
                        playert.y=0 #move player to top for new map

            elif key[pygame.K_UP] or key[pygame.K_w]:
                movment_ok=collision_detection(playert.x,playert.y-cellSize,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.y!=0: #if play isnt at top of level
                        playert.y -= cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        new_map("up",playert) #load new map
                        playert.y=580 #move player to buttom for new map

            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                movment_ok=collision_detection(playert.x+cellSize,playert.y,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.x!=780: #if play isnt on the right most map
                        playert.x += cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        new_map("right",playert) #load new map
                        playert.x=0 #move player to left for new map

            elif key[pygame.K_LEFT] or key[pygame.K_a]:
                movment_ok=collision_detection(playert.x-cellSize,playert.y,player)
                if movment_ok==False:
                    print("collision")
                else:
                    if playert.x!=0: #if play isnt on the left most map
                        playert.x -= cellSize
                        after_movement(playert.x,playert.y,boss_list)
                    else:
                        new_map("left",playert) #load new map
                        playert.x=780 #move player to right for new map
            elif key[pygame.K_p]:
                print("paused")
                pause()
                map_name="map"+str(player[15])+".gif" #add back background after unpaused
                background = pygame.image.load(os.path.join("textures",map_name))
                screen.blit(background, (0,0))
            elif key[pygame.K_m] or key[pygame.K_ESCAPE]:
                menu()
                map_name="map"+str(player[15])+".gif" #add back background after menu
                background = pygame.image.load(os.path.join("textures",map_name))
                screen.blit(background, (0,0))
            elif key[pygame.K_b]:
                shop = 1
                while shop==1:
                    instruction=input("What would you like to do?")
                    if instruction==("\money"):
                        screen.fill(BLACK)
                        message_display("small orbs " + str(money[0]) + ", medium orbs " + str(money[1]) + ", large orbs " + str(money[2]) + ", special orbs " +str(money[3]),400,30,16,WHITE)
                        pygame.display.flip()

                    elif instruction==("\+money"):
                        type=input("Small, Medium, Large or Special")
                        amount=int(input("How much?"))
                        if type=="S" or type=="M" or type=="L" or type=="X":
                            change(money, type, amount)
                        else:
                            print("Enter capital: S,M,L or X only")
                    elif instruction==("\shop"):
                        loop=0
                        y=20
                        screen.fill(BLACK)
                        message_display("Please wait, loading",400,20,16,WHITE)
                        pygame.display.flip()
                        screen.fill(BLACK)
                        player_class=input("enter player class number (1-7)")
                        y=20
                        while loop<length:
                            if items[loop][5]==0 or items[loop][5]==int(player_class):
                                message_display("Item "+str(loop)+" - "+items[loop][4]+" costs "+str(store[1][loop])+" from obrb type "+str(store[2][loop]),400,y,16,WHITE)
                                y=y+20
                            loop=loop+1
                        message_display("Type \"leave\" to leave shop",400,y,16,WHITE)
                        pygame.display.flip()
                        to_buy=input("Input item number to buy")
                        check=is_number(to_buy) #check user has entered a number
                        #check="TRUE" #uncomment to accept letters
                        if check=="TRUE":
                            if int(to_buy)<=int(length): #check number isnt too big
                                if items[int(to_buy)][5]==0 or items[int(to_buy)][5]==int(player_class):
                                    screen.fill(BLACK)
                                    message_display("You have attempted to buy "+str(items[int(to_buy)][4]),400,20,16,WHITE)
                                    pygame.display.flip()
                                    price=(store[1][int(to_buy)])
                                    type=store[2][int(to_buy)]
                                    if store[2][int(to_buy)]=="S":
                                        amount=money[0]-int(price)
                                        if amount<0:
                                            message_display("You cannot afford that",400,60,16,WHITE)
                                            pygame.display.flip()
                                        else:
                                            change(money,type,amount)
                                            inventry.append(items[int(to_buy)])
                                            save_item(to_buy)
                                            file = open(os.path.join("Saves",save_game_to_use,"money_s.txt"),"w")
                                            file.write(str(money[0]))
                                            file.close()
                                            message_display("You have sucssesfully bought "+str(items[int(to_buy)][4]),400,60,16,WHITE)
                                            pygame.display.flip()
                                    elif store[2][int(to_buy)]=="M":
                                        amount=money[1]-int(price)
                                        if amount<0:
                                            message_display("You cannot afford that",400,60,16,WHITE)
                                            pygame.display.flip()
                                        else:
                                            change(money,type,amount)
                                            inventry.append(items[int(to_buy)])
                                            save_item(to_buy)
                                            file = open(os.path.join("Saves",save_game_to_use,"money_m.txt"),"w")
                                            file.write(str(money[1]))
                                            file.close()
                                            message_display("You have sucssesfully bought "+str(items[int(to_buy)][4]),400,60,16,WHITE)
                                            pygame.display.flip()
                                    elif store[2][int(to_buy)]=="L":
                                        amount=money[2]-int(price)
                                        if amount<0:
                                            message_display("You cannot afford that",400,60,16,WHITE)
                                            pygame.display.flip()
                                        else:
                                            change(money,type,amount)
                                            inventry.append(items[int(to_buy)])
                                            save_item(to_buy)
                                            file = open(os.path.join("Saves",save_game_to_use,"money_l.txt"),"w")
                                            file.write(str(money[2]))
                                            file.close()
                                            message_display("You have sucssesfully bought "+str(items[int(to_buy)][4]),400,60,16,WHITE)
                                            pygame.display.flip()
                                    elif store[2][int(to_buy)]=="X":
                                        amount=money[3]-int(price)
                                        if amount<0:
                                            message_display("You cannot afford that",400,60,16,WHITE)
                                            pygame.display.flip()
                                        else:
                                            change(money,type,amount)
                                            inventry.append(items[int(to_buy)])
                                            save_item(to_buy)
                                            file = open(os.path.join("Saves",save_game_to_use,"money_x.txt"),"w")
                                            file.write(str(money[3]))
                                            file.close()
                                            message_display("You have sucssesfully bought "+str(items[int(to_buy)][4]),400,60,16,WHITE)
                                            pygame.display.flip()
                                else:
                                    screen.fill(BLACK)
                                    message_display("Your class cannot buy that item",400,20,16,WHITE)
                                    pygame.display.flip()
                            else:
                                screen.fill(BLACK)
                                message_display("Error - item not recongised",400,20,16,WHITE)
                                pygame.display.flip()
                        else:
                            screen.fill(BLACK)
                            message_display("Please enter a number",400,20,16,WHITE)
                            pygame.display.flip()
                    elif instruction==("\data"):
                        loop=0
                        option=input("Weapons (1), armour (2) or cloths (3)")
                        option=int(option)-1
                        screen.fill(BLACK)
                        message_display("Please wait, loading",400,16,16,WHITE)
                        pygame.display.flip()
                        screen.fill(BLACK)
                        y=16
                        while loop<length:
                            if items[int(loop)][6]==int(option):
                                message_display("Item "+str(loop)+" - "+items[loop][4],400,y,16,WHITE)
                                y=y+16
                            loop=loop+1
                        pygame.display.flip()
                        to_buy=input("Input item number to get data on")
                        check=is_number(to_buy) #check user has entered a number
                        #check="TRUE" #uncomment to accept letters
                        if check=="TRUE":
                ##            if int(to_buy)>len(item): #check item exists
                ##                print("Item number not found")
                ##            else:
                            screen.fill(BLACK)
                            message_display("You have requested data on: "+items[int(to_buy)][4],400,20,16,WHITE)
                            message_display("Strength = "+str(items[int(to_buy)][0]),400,40,16,WHITE)
                            message_display("Endurance = "+str(items[int(to_buy)][1]),400,60,16,WHITE)
                            message_display("Dexterity = "+str(items[int(to_buy)][2]),400,80,16,WHITE)
                            message_display("Spell = "+str(items[int(to_buy)][3]),400,100,16,WHITE)
                            #4 is used for name
                            message_display("Class = "+str(items[int(to_buy)][5]),400,120,16,WHITE)
                            message_display("Type = "+str(items[int(to_buy)][6]),400,140,16,WHITE)
                            #7 used for description, placed at end
                            message_display("Range = "+str(items[int(to_buy)][8]),400,160,16,WHITE)
                            message_display("Bellow is a description of the item:",400,180,16,WHITE)
                            message_display(str(items[int(to_buy)][7]),400,200,16,WHITE)
                            pygame.display.flip()
                        else:
                            screen.fill(BLACK)
                            message_display("Please enter numeric numbers only",400,20,16,WHITE)
                            pygame.display.flip()
                    elif instruction==("\help"):
                        screen.fill(BLACK)
                        message_display("Availbe commands:",400,40,16,WHITE)
                        message_display("\shop = shop",400,60,16,WHITE)
                        message_display("\money = see availbe orbs",400,80,16,WHITE)
                        message_display("\+money = change current money",400,100,16,WHITE)
                        message_display("\management = manage your inventory & equip items",400,120,16,WHITE)
                        message_display("\data = find out the statistics of an item",400,140,16,WHITE)
                        message_display("\exit = leave the shop",400,160,16,WHITE)
                        pygame.display.flip()
                    elif instruction==("\management"):
                        pinventory()
                    elif instruction==("\exit"):
                        shop=0
                    else:
                        screen.fill(BLACK)
                        message_display("Error - command not recognised - uses \"\help\" for a list of instructions",400,40,16,WHITE)
                        pygame.display.flip()
                map_name="map"+str(player[15])+".gif" #add back background after menu
                background = pygame.image.load(os.path.join("textures",map_name))
                screen.blit(background, (0,0))
            elif key[pygame.K_r]:
                return_home = input("Would you like to return to the home base. Enter Y or N")
                return_home = return_home.lower()
                if return_home == "y":
                    if mana_use >= 10:
                        print(mana_use)
                        mana_use -= 10
                        global player, map_number, mana, mana_use
                        map_number = 1
                        player[15] = 1
                        image_path="map"+str(player[15])+".gif"
                        if os.path.isfile(image_path)==FALSE: #check that a map file exisits, if not then display an error message. Changing this to TRUE and moving to a new map will show the error message if you want to see it.
                            img=pygame.image.load("map_error.gif")
                            #screen=pygame.display.set_mode((0,0))
                            screen.blit(img,(0,0))
                        else:
                            img=pygame.image.load(image_path)
                            #screen=pygame.display.set_mode((0,0))
                            screen.blit(img,(0,0))
            clock.tick(10)
            screen.blit(image, (playert.x, playert.y))
            print(playert.x)
            print(playert.y)
            pygame.display.update()
            if internal_editor == TRUE:
                if key[pygame.K_n]:
                    f=open("blocked.txt","a")
                    to_write=str((playert.x, playert.y,player[15]))
                    f.write(str(to_write))
                    f.write("\n")
                    f.close()
                    print("added to blakced square list")
