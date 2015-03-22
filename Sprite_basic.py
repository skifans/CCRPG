#Map

#Imports
import pygame, random, time, os, ctypes
from pygame.locals import *
from tkinter import *

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
cellSize = 20
assert windowHeight % cellSize == 0
assert windowWidth % cellSize == 0
cellWidth = int(windowWidth / cellSize)
cellHeight = int(windowHeight / cellSize)


pygame.init()

#Initiate the window and the basic grid background when called.
def drawGrid():
    global window
    window = pygame.display.set_mode((windowWidth, windowHeight))
    for x in range(0, windowWidth, cellSize): # draw vertical lines
        pygame.draw.line(window, lineColour, (x, 0), (x, windowHeight))
    for y in range(0, windowHeight, cellSize): # draw horizontal lines
        pygame.draw.line(window, lineColour, (0, y), (windowWidth, y))
    pygame.display.update() #removing this will make grid and loading appear at the same time

class textures():

    waterCoords = []
    lavaCoords = []
    roadCoords = []

    def __init__(self):
        self.x = 0
        self.y = 0

    class playerTexture():

        x = 0
        y = 0

        def loadTextures(self, x, y):
            self.texture = pygame.image.load(os.path.join("textures","necromancer.png"))
            self.texturerect = self.texture.get_rect()
            self.coords = (x, y)
            self.texturerect.move_ip(self.coords)
            window.blit(self.texture, self.texturerect)

    #Class for General Grass Texture
    class grassTexture():
        def __init__(self):
            self.x = 0
            self.y = 0

        def loadTexture(self, x, y):
            self.texture = pygame.image.load(os.path.join("textures","map1.gif")) #this image (or the top left 20x20 pixels if bigger) will be your "tail" and will be what covers your tracks.
            self.texturerect = self.texture.get_rect()
            self.coords = (x, y)
            self.texturerect.move_ip(self.coords)
            window.blit(self.texture, self.texturerect)
            #pygame.display.flip()

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
            #pygame.display.flip()

playert = textures.playerTexture()

#Loads vertical line of texture - currently only way of rendering textures for most textures.
#Takes four arguments: 2 coords to print textures between MUST BE VERTICAL STRAIGHT LINE
def loadGrassVertLine(x, y, a, b):
    img = textures.grassTexture()
    while y < b:
        img.loadTexture(x, y)
        textures.waterCoords.append((x, y))
        y += 20

def loadWhiteVertLine(x, y, a, b):
    img = textures.loadigTexture()
    while y < b:
        img.loadTexture(x, y)
        #textures.loadCoords.append((x,y))
        y += 20

#Not very clever way of loading all the water textures for the main map...

def loadWhiteMap():
    #arial font used
    #l
    loadWhiteVertLine(40, 220, 60, 360)
    #o
    loadWhiteVertLine(80, 260, 80, 340)
    loadWhiteVertLine(100, 240, 100, 260)
    loadWhiteVertLine(100, 340, 100, 360)
    loadWhiteVertLine(120, 240, 120, 260)
    loadWhiteVertLine(120, 340, 120, 360)
    loadWhiteVertLine(140, 240, 140, 260)
    loadWhiteVertLine(140, 340, 140, 360)
    loadWhiteVertLine(160, 260, 160, 340)
    #a
    loadWhiteVertLine(200, 260, 200, 280)
    loadWhiteVertLine(200, 300, 200, 340)
    loadWhiteVertLine(220, 240, 220, 260)
    loadWhiteVertLine(220, 280, 220, 300)
    loadWhiteVertLine(220, 340, 220, 360)
    loadWhiteVertLine(240, 240, 240, 260)
    loadWhiteVertLine(240, 280, 240, 300)
    loadWhiteVertLine(240, 340, 240, 360)
    loadWhiteVertLine(260, 240, 260, 260)
    loadWhiteVertLine(260, 280, 260, 300)
    loadWhiteVertLine(260, 320, 260, 340)
    loadWhiteVertLine(280, 260, 280, 360)
    #d
    loadWhiteVertLine(320, 260, 320, 340)
    loadWhiteVertLine(340, 240, 340, 260)
    loadWhiteVertLine(340, 340, 340, 360)
    loadWhiteVertLine(360, 240, 360, 260)
    loadWhiteVertLine(360, 340, 360, 360)
    loadWhiteVertLine(380, 260, 380, 280)
    loadWhiteVertLine(380, 320, 380, 340)
    loadWhiteVertLine(400, 200, 400, 360)
    #i
    loadWhiteVertLine(440, 200, 440, 220)
    loadWhiteVertLine(440, 240, 440, 360)
    #n
    loadWhiteVertLine(480, 240, 480, 360)
    loadWhiteVertLine(500, 240, 500, 260)
    loadWhiteVertLine(520, 240, 520, 260)
    loadWhiteVertLine(540, 240, 540, 260)
    loadWhiteVertLine(560, 260, 560, 360)
    #g
    loadWhiteVertLine(600, 260, 600, 340)
    loadWhiteVertLine(600, 380, 600, 400)
    loadWhiteVertLine(620, 240, 620, 260)
    loadWhiteVertLine(620, 340, 620, 360)
    loadWhiteVertLine(620, 380, 620, 400)
    loadWhiteVertLine(640, 240, 640, 260)
    loadWhiteVertLine(640, 340, 640, 360)
    loadWhiteVertLine(640, 380, 640, 400)
    loadWhiteVertLine(660, 260, 660, 280)
    loadWhiteVertLine(660, 320, 660, 340)
    loadWhiteVertLine(660, 380, 660, 400)
    loadWhiteVertLine(680, 240, 660, 380)


#Fills Background With Grass
def fillGrass(playert_x, playert_y):
    x=0
    #while x < windowWidth:
    loadGrassVertLine(playert_x-20,playert_y-20,playert_x-20,playert_y+20) #refresh 1 collum to the left, from playert y -20 to playert y +20
    loadGrassVertLine(playert_x,playert_y-20,playert_x,playert_y+40) #not sure way this needs to be 40, but dosnt work otherwise, refreshes collum you are in
    loadGrassVertLine(playert_x+20,playert_y-20,playert_x+20,playert_y+20) #refresh 1 collum to the right, same range as top
        #x += 20

#Refresh Textures Will Take Current Logged Appropriate Coords For Each Texture & Re-Render It (Pre-".flip")
def refreshTextures(texture, coords):
    img = texture()
    for i in coords:
        img.loadTexture(i[0], i[1])

def refreshAllTextures():
    playert.loadTextures(playert.x, playert.y)

#General "Main-loop" equivalent for testing.
def loadTextures():
    drawGrid()
    loadWhiteMap()
    pygame.display.flip()
    #time.sleep(3) #this will keep the loading screen on for an extra 3 seconds
    img=pygame.image.load("map1.gif")
    screen=pygame.display.set_mode((0,0))
    screen.blit(img,(0,0))
    pygame.display.flip()

#Closes The Window & Game
def terminate():
    pygame.quit()

#anything in this function will be done each time the playert moves - regardless if direction
boss_list=[[20,40,60],[20,40,60],[0,1,1],[0,1,2]]
def after_movement(playert_x, playert_y, boss_list):
    #x of boss, y of boss, 0 = one time only (the first time playert lands of square) or 1 = repeate (repeate regarless of how many times playert lands on square), boss ID
    refreshAllTextures()
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

def collision_detection(playert_x, playert_y):
    playert_position = (playert_x, playert_y)
    cannot_go_onto=[(760,560), (780,560)] #needs to be in format [(x position,y position), (x position,y position), ...
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
lancer = [40,30,80,10,90,["lance",35],["super_light_armour",2],name,[0,20,1],10,0,0,0]
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

def classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja):
    global player   #moved global from the if statments to the top to cut down on the ammount needed
    print("What is you're name?")
    name = str(input("my name is:"))
    print("Choose you're class " + name)
    print(classes)
    player_class = str(input())
    player_class = player_class.lower() #added .lower() to make sure that the input was lowercase so it wasn't case sensitvie
    if player_class == "barbarian":
            player = barbarian
    elif player_class == "warrior": #changed the if to an elif to cut down lag
            player = warrior
    elif player_class == "mage":    #changed the if to an elif to cut down lag
            player = mage
    elif player_class == "paladin": #changed the if to an elif to cut down lag
            player = paladin
    elif player_class == "necromancer": #changed the if to an elif to cut down lag
            player = necromancer
    elif player_class == "lancer":  #changed the if to an elif to cut down lag
            player = lancer
    elif player_class == "archer":  #changed the if to an elif to cut down lag
            player = archer
    elif player_class == "samurai":#changed the if to an elif to cut down lag
            player = samurai
    elif player_class == "ninja":   #changed the if to an elif to cut down lag
            player = ninja

    else:
            ctypes.windll.user32.MessageBoxW(0, "Error - player class entered incorectly", "error", 0)
            print("Error - player class entered incorectly")
            player = "error"
            while player == "error":
                classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja)

    print ("Are you ready?")

"""
This is the level up system
It is ready to go into the game (I think)
"""

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
def statsetup (player,darkness,sakaretsu_armour,simple_katanna):
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
    app = Application(master=root)
    #thigns before button is pressed
    app.mainloop()
    #things after button is pressed
    ##pchoice="run"
    root.quit()
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
classselect(classes,lancer,archer,necromancer,warrior,mage,paladin,barbarian,samurai,ninja)
statsetup (player,darkness,sakaretsu_armour,simple_katanna)

def combat():
    global combatover
    combatover = False
    while combatover == False:
        turn (player,darkness)
    combatover = False
    statsetup (player,darkness,sakaretsu_armour,simple_katanna)
    while combatover == False:
        turn (player,darkness)

global pchoice
class Application(Frame):
    def say_hi(self):
        global pchoice
        print("Run")
        pchoice="run"
        root.quit()

    def say_hi1(self):
        global pchoice
        print("Spell")
        pchoice="spell"
        root.quit()

    def say_hi2(self):
        global pchoice
        print("Attack")
        pchoice="attack"
        root.quit()

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
root = Tk()
#end of combat system
#-----------------------------------------------------------------------------------
def new_map(direction, playert):
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
    pygame.display.flip()
#-----------------------------------------------------------------------------------------------------------------------------------------------

print("Movement enabled, use arrow keys or WASD keys")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
loadTextures()
x=0###
y=0###
image = pygame.image.load(os.path.join("textures","necromancer.png"))###
running=True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
                terminate()
                pygame.display.quit()
                running=False
                break
##        elif event.type == KEYDOWN:
##            if event.key == K_ESCAPE:
##                terminate()
##            elif (event.key == K_LEFT or event.key == K_a):
##                if playert.x!=0:
##                    #playert.x = playert.x-20
##                    movment_ok=collision_detection(playert.x,playert.y)
##                    #if movment_ok==False:
##                        #playert.x=playert.x+20
##                    print("placeholder for left code")
##                    print("now at, (" ,playert.x,",", playert.y,")")
##                    fillGrass(playert.x, playert.y)
##                    after_movement(playert.x, playert.y, boss_list)
##                    to_update=(playert.x, playert.y, 40, 20) #left, top, width, hight
##                    pygame.display.update(to_update)
##                else:
##                    to_update=(playert.x, playert.y, 20, 40) #left, top, width, hight
##                    pygame.display.update(to_update)
##                    #playert.x=780
##                    new_map("left",playert)
##
##            elif (event.key == K_RIGHT or event.key == K_d):
##                if playert.x != 780:
##                    #playert.x = playert.x+20
##                    movment_ok=collision_detection(playert.x,playert.y)
##                    #if movment_ok==False:
##                        #playert.x=playert.x-20
##                    print("placeholder for right code")
##                    print("now at, (" ,playert.x,",", playert.y,")")
##                    fillGrass(playert.x, playert.y)
##                    after_movement(playert.x, playert.y, boss_list)
##                    to_update=(playert.x-20, playert.y, 40, 20) #left, top, width, hight
##                    pygame.display.update(to_update)
##                else:
##                    to_update=(playert.x, playert.y, 20, 40) #left, top, width, hight
##                    pygame.display.update(to_update)
##                    #playert.x=0
##                    new_map("right",playert)
##
##            elif (event.key == K_UP or event.key == K_w):
##                if playert.y != 0:
##                    #playert.y -= cellSize
##                    movment_ok=collision_detection(playert.x,playert.y)
##                    #if movment_ok==False:
##                        #playert.y += cellSize
##                    print("placeholder for up code")
##                    print("now at, (" ,playert.x,",", playert.y,")")
##                    fillGrass(playert.x, playert.y)
##                    after_movement(playert.x, playert.y, boss_list)
##                    to_update=(playert.x, playert.y, 20, 40) #left, top, width, hight
##                    pygame.display.update(to_update)
##                else:
##                    to_update=(playert.x, playert.y, 20, 40) #left, top, width, hight
##                    pygame.display.update(to_update)
##                    #playert.y=580
##                    new_map("up",playert)
##
##            elif (event.key == K_DOWN or event.key == K_s):
##                if playert.y!=(windowHeight-20):
##                    #playert.y += 20
##                    movment_ok=collision_detection(playert.x,playert.y)
##                    #if movment_ok==False:
##                        #playert.y -= 20
##                    print("placeholder for down code")
##                    print("now at, (" ,playert.x,",", playert.y,")")
##                    fillGrass(playert.x, playert.y)
##                    after_movement(playert.x, playert.y, boss_list)
##                    to_update=(playert.x, playert.y-20, 20, 40) #left, top, width, hight
##                    pygame.display.update(to_update)
##                else:
##                    to_update=(playert.x, playert.y, 20, 40) #left, top, width, hight
##                    pygame.display.update(to_update)
##                    #playert.y=0
##                    new_map("down",playert)
        elif event.type == KEYDOWN:
            background = pygame.image.load(os.path.join("textures","map1.gif"))
            screen.blit(background, (0,0))
            pygame.display.update()
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                playert.y += cellSize
            elif key[pygame.K_UP]:
                playert.y -= cellSize
            if key[pygame.K_RIGHT]:
                playert.x += cellSize
            elif key[pygame.K_LEFT]:
                playert.x -= cellSize
    ##            Player.handle_keys()
    ##            Player.draw(screen)
    ##            pygame.display.update()
            clock.tick(10)
            screen.blit(image, (playert.x, playert.y))
            print(playert.x)
            print(playert.y)
            pygame.display.update()