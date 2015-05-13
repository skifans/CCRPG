#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alex
#
# Created:     25/06/2014
# Copyright:   (c) Alex 2014
# Licence:     CC
#Not compatable with 2.7, use 3.2
#-------------------------------------------------------------------------------

#To do:
#Converter

#to use money_reset to change large: swap amount to others to change small/meduim and change large to money[2] and change type as required:
#Remerber system is not relative!! Use amount=money[2](1 for medium, 0 for small)-/+price change.
#type=L
#x_money=money[3]
#l_money=amount *set large to x* or "amount=money[2]-/+price change" *increase/decrease large by x"
#m_money=money[1]
#s_money=money[0]
# money_reset(s_money, m_money, l_money, x_money, money)

import os #used for file deleting
import pygame, time

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

cellSize=20

windowWidth = 800
windowHeight = 600
lineColour = WHITE
assert windowHeight % cellSize == 0
assert windowWidth % cellSize == 0
cellWidth = int(windowWidth / cellSize)
cellHeight = int(windowHeight / cellSize)

pygame.init()
screen=pygame.display.set_mode((0,0))
def drawGrid():
    global window
    window = pygame.display.set_mode((windowWidth, windowHeight))
    for x in range(0, windowWidth, cellSize): # draw vertical lines
        pygame.draw.line(window, lineColour, (x, 0), (x, windowHeight))
    for y in range(0, windowHeight, cellSize): # draw horizontal lines
        pygame.draw.line(window, lineColour, (0, y), (windowWidth, y))
    pygame.display.update()

def message_display(text, x, y, font_size, colour):
    largeText = pygame.font.Font('freesansbold.ttf',font_size) #load font
    TextSurf, TextRect = text_objects(text, largeText, colour) #render text
    TextRect.center = ((x),(y)) #place text
    #screen=pygame.display.set_mode((0,0))
    screen.blit(TextSurf, TextRect) #send to screen, needs to be updated/fliped to be worked

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour) #extact purpose unkown but seems to be needed
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,inactive_colour,active_colour,text_colour,name_of_function_to_call_when_clicked,veriable_in_function):
    #screen=pygame.display.set_mode((0,0))
    click = pygame.mouse.get_pressed() #get mouse state (clicked/not clicked)
    mouse = pygame.mouse.get_pos() #get mouse coords
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #check if mouse is on button
        pygame.draw.rect(screen, active_colour,(x,y,w,h)) #change to active colour
        if click[0] == 1: #check click (above if checks mouse is on button)
            name_of_function_to_call_when_clicked(veriable_in_function) #do this when clicked (veriable needs not to have brackets)
    else:
        pygame.draw.rect(screen, inactive_colour,(x,y,w,h)) #mouse not on button, switch to inactive colour

    smallText = pygame.font.Font("freesansbold.ttf",20) #load font
    textSurf, textRect = text_objects(msg, smallText,text_colour) #place text in button through text funtion
    textRect.center = ( (x+(w/2)), (y+(h/2)) ) #location of text
    screen.blit(textSurf, textRect) #send to screen (but not update)

drawGrid()
screen.fill(BLACK)
pygame.display.update()

#error checking
def is_number(to_check):
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
        print("Succsesful money change")
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

#loading money
money=[]
f = open("money_s.txt","r")
s_money=f.read()
f.close()
f = open("money_m.txt","r")
m_money=f.read()
f.close()
f = open("money_l.txt","r")
l_money=f.read()
f.close()
f = open("money_x.txt","r")
x_money=f.read()
f.close()
money.append(int(s_money))
money.append(int(m_money))
money.append(int(l_money))
money.append(int(x_money))

#global inventry
inventry=[]

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
#---------------------------------------------------------------------------------------------------
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

"""
Functions below for actions:
All functions start by finding the category of the item so that it is able to
deal with the appropriate part of the inventory (may be streamlined using a
second function at a later date.) <-- Not applicable to pickUpItem()
"""

#Function for putting an item into the inventory.
def pickUpItem(obj):
    global armour, weapons
    if obj[5] == "clothing":
        clothing.insert(obj[4])
        print(pickUpMessage+obj[4] + ".")
        return invent
    elif obj[5] == 1:
        armour.append(obj)
        print(pickUpMessage+obj[4] + ".")
        return armour
    elif obj[5] == 0:
        weapons.append(obj[4])
        print(pickUpMessage + obj[4] + ".")
        return weapons

#Function for removing an item from the inventory (& at the moment, removing said item from game)
def dropItem(obj):
    global armour, weapons
    if obj[5] == 0:
        weapons.remove(obj[4])
        print(dropItemMessage + obj[4] + ".")
        return weapons
    elif obj[5] == 1:
        armour.remove(obj[4])
        print(dropItemMessage + obj[4] + ".")
        return armour

#Function for equipping an item e.g Sword into your hand/Put on armour
def equipItem(obj, name, pequip):
    global armour, weapons
    if obj == 0:
        weapons = name
        #Enter Addition To Stats (Waiting for finished weapons)
        print(currentHandItemMessage + str(name) + ".")
        file = open("equip0.txt","w")
        file.write(str(pequip))
        file.close()
        return weapons
    elif obj == 1:
        armour = name
        print(currentArmourMessage + str(name) + ".")
        file = open("equip1.txt","w")
        file.write(str(pequip))
        file.close()
        return armour
    elif obj==2:
        print("clothing is not yet supported")
    else:
        print("error line 214")

#Function to unequip yet keep in inventory
def unEquipItem(obj):
    #not used
    global armour, weapons
    if obj == 1:
        #Resets name of current armour & resets the appropriate stats.
        armour = " "
        print(unEquipArmourMessage)

    elif obj == 0:
        weapon = " "
        #Enter Reverse Stats of Weapon (Waiting for finished weapons)
        print(unEquipWeaponMessage)

def equip(t):
    #t is needed as all functions when called by buttons are bassed a veriable. So it needs to have 1 when defined, even if unused.
    global decide, pdecide
    print("equip")
    pdecide = "equip"
    decide=1
    return decide, pdecide

def unequip(t):
    #t is needed as all functions when called by buttons are bassed a veriable. So it needs to have 1 when defined, even if unused.
    global decide, pdecide
    print("unequip")
    pdecide = "unequip"
    decide=1
    return decide, pdecide

def item_to_eqip(length):
    global decide
    print(length)
    equipItem(inventry[length][6],inventry[length][4],length)
    decide=1
    return decide

def pinventory():
    global inventry, decide, pdecide
    global armour, weapons
    print(currentHandItemMessage + str(weapons))
    screen.fill(BLACK)
    message_display("You are currently wearing: " + str(armour) + ". Your options are: unequip or equip",400,40,16,WHITE)
    pygame.display.flip()
    decide = 0
    while decide == 0:
        for event in pygame.event.get():
            button("equip",300,100,150,50,GREEN,DARKGREEN,BLACK,equip,"")
            button("unequip",300,200,150,50,GREEN,DARKGREEN,BLACK,unequip,"")
            pygame.display.flip()
            time.sleep(0.1)
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
            y=0
            screen.fill(BLACK)
            decide=0
            while decide==0:
                for event in pygame.event.get():
                    while length1<len(inventry):
                        button("Item number "+str(length1)+" is "+inventry[length1][4],150,y,500,50,GREEN,DARKGREEN,BLACK,item_to_eqip,length1)
                        pygame.display.flip()
                        length1 = length1 + 1
                        y=y+50
                    length1=0
                    y=0
                time.sleep(0.1)
    if pdecide == "unequip":
        armour = ""
        weapons = ""
#--------------------------------------------------------------------------------------------------------------------------
def save_item(to_write):
    file=open("items.txt","a")
    file.write(to_write)
    file.write("\n")
    file.close()
    file=open("amount.txt","r")
    amount=int(file.readline())
    file.close()
    file=open("amount.txt","w")
    amount=int(amount)+1
    file.write(str(amount))
    file.close()
#strengthm(0),endurancem(1),dexm(2),spellm(3),name(4),class(5),type(6),description(7),range(8),costs(9),costm(10),costl(11),costx(12)
#possible items to buy
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
mage_power_armour = [0,300,0,100,"one shot armour",2,1,"armoua that helps increase magic power",0,0,40,0,0]
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
mage_twilight_wand = [200,150,150,0,"twilight wand",2,0,"a wand taken from a blue eyed beast",0,0,0,5,0,]
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
necomancer_night_staff = [0,1000,0,2000,"night staff",4,0,"a staff only for the best of necromancers",0,0,0,30,0]

barbarian_dragon_sword = [50,50,100,0,"dragon sword",5,0,"a lightweight sword taken from a dragon's treasure",0,0,20,0,0]
barbarian_bloodaxe = [600,0,0,0,"blood axe",5,0,"a huge axe owned by a very strong warrior",0,0,60,0,0]
barbarian_battle_axe = [40,20,0,0,"battle axe",5,0,"a simple battle axe",0,60,0,0,0]
barbarian_twin_axe = [200,0,200,0,"twin axe",5,0,"a pole arm with an axe blade at each end",0,0,40,0,0]
barbarian_hammer = [600,0,-100,0,"barbarian's hammer",5,0,"a hammer large and heavy enough to crush foes",0,0,50,0,0]
barbarian_dragon_blade = [2000,0,2000,0,"dragonslayer blade",5,0,"a curved sword of a barbarian who busted many a dragon",0,0,0,40,0]

lancer_trident = [70,70,60,0,"the trident",6,0,"protects the user with a shield of water",1,0,20,0,0]
lancer_glaive = [200,0,200,0,"the glaive",6,0,"a pole-arm designed to be slashed rather than thrusted",1,0,40,0,0]
lancer_conquest_lance = [350,300,350,0,"conquest lance",6,0,"lance of a rider who rode a white horse",1,0,0,10,0]
lancer_war_lance = [500,0,500,0,"war lance",6,0,"lance of a rider who rode a red horse",1,0,0,10,0]
lancer_famine_lance = [250,500,250,0,"famine lance",6,0,"lance of a rider who rode a black horse",1,0,0,10,0]
lancer_death_lance = [1000,0,0,0,"death lance",6,0,"lance of a rider who rode a pale green horse",1,0,0,10,0]
lancer_oni_lance = [4000,0,1000,0,"oni's lance",6,0,"the lance of one of four riders, but not the four you're thinking of",1,0,0,50,0]

archer_crossbow = [200,0,0,0,"crossbow",7,0,"similar to a bow, but more mechanical and requires less skill",1,0,20,0,0]
archer_hermes_bow = [50,-20,30,0,"bow of hermes",7,0,"a bow that delivers a message, a painful message",1,0,40,0,0]
archer_explosive_bow = [500,0,60,0,"explosive bow",7,0,"a bow that fires arrows that explode upon hitting their target",1,0,56,0,0]
archer_black_bow = [100,0,700,0,"black bow",7,0,"a bow made of a very srong wood that lets it hit from miles away",1,0,80,0,0]
archer_greatbow = [600,0,0,0,"greatbow",7,0,"an extremly heavy bow that fires extremly heavy arrows that pack a huge punch",1,0,60,0,0]
archer_shotgun = [2000,0,0,0,"the shotgun",7,0,"not really a shotgun, just a crossbow that fires 6 bolts at once",1,0,0,20,0]

samurai_dark_katana = [100,0,100,0,"dark katana",8,0,"a katana that emits a dark aura",0,0,20,0,0]
samurai_light_katana = [200,100,100,0,"light katana",8,0,"a katana that emits a holy aura",0,0,40,0,0]
samurai_gold_katana = [30,10,30,0,"golden katana",8,0,"a katana made of gold",0,70,0,0,0]
samurai_scimitar = [90,0,60,0,"scimitar",8,0,"a curved sword for samurai warriors",0,150,0,0,0]
samurai_twinblade = [70,0,80,0,"twinblade",8,0,"a strange weapon with a blade at both ends",0,150,0,0,0]
samurai_wakizashi = [250,0,250,0,"wakizashi",8,0,"a shortened katana for quicker strikes",0,0,50,0,0]
samurai_aluminium_katana = [1000,500,1500,0,"aluminium katana",8,0,"a katana made from magically enhanced aluminium, in respect to a famed samurai",0,0,0,30,0]

ninja_jo_staff = [50,50,100,0,"jo staff",9,0,"a short staff for ninjas",0,0,20,0,0]
ninja_bo_staff = [100,100,200,0,"bo staff",9,0,"a long staff for ninjas",0,0,40,0,0]
ninja_extended_bo_staff = [400,0,100,0,"extended bo staff",9,0,"a staff that is good at range but bad up close",1,0,50,0,0]
ninja_surikens = [300,0,300,0,"surikens",9,0,"surikens for ninjas",1,0,60,0,0]
ninja_kunai = [500,0,500,0,"kunai",9,0,"can be used up close or at range",1,0,0,1,0]
ninja_dagger = [20,0,80,0,"dagger",9,0,"a dagger for sneaky ninjas",0,100,0,0,0]
ninja_tashi = [40,0,160,0,"tashi",9,0,"a short katana for ninjas rather than samurais",0,200,0,0,0]

#weapons that multiple classes can use

basic_crossbow = [50,0,0,0,"basic crossbow",0,0,"a basic crossbow for beginners",1,50,0,0,0]
medium_crossbow = [150,0,0,0,"medium crossbow",0,0,"a better crossbow for the more experienced",1,150,0,0,0]
strong_crossbow = [350,0,0,0,"strong crossbow",0,0,"a very good quality crossbow",1,0,35,0,0]

basic_halberd = [30,0,30,0,"basic halberd",1568,0,"a basic halberd for beginners",0,60,0,0,0]

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
items_accsesorys=[berserkers_band,priest_band,Fire_gem_circlet,major_ring,ring_of_random_change,blinding_cranium_crab,swiss_army_claymore,arrow_target,blight_sludge,overpowered_stick,boss_shield,sleepy_stick,lol,necrotic_bone,mr_tiddles,paladin_basic_weapon,paladin_medium_weapon,paladin_strong_weapon,paladin_elite_weapon,paladin_ultimate_weapon,necromancer_basic_weapon,necromancer_medium_weapon,necromancer_strong_weapon,necromancer_elite_weapon,necromancer_ultimate_weapon,barbarian_basic_weapon,barbarian_medium_weapon,barbarian_strong_weapon,barbarian_elite_weapon,barbarian_ultimate_weapon,lancer_basic_weapon,lancer_medium_weapon,lancer_strong_weapon,lancer_elite_weapon,lancer_ultimate_weapon,archer_basic_weapon,archer_medium_weapon,archer_strong_weapon,archer_elite_weapon,archer_ultimate_weapon,samurai_basic_weapon,samurai_medium_weapon,samurai_strong_weapon,samurai_elite_weapon,samurai_ultimate_weapon,ninja_basic_weapon,ninja_medium_weapon]    #adds to arary
items.extend(items_accsesorys) #add accsesorys to end of items array
items1=[ninja_strong_weapon,ninja_elite_weapon,ninja_ultimate_weapon,warrior_spiked_armour,warrior_enchanted_armour,warrior_stone_armour,warrior_simple_armour,warrior_old_iron_armour,mage_magic_armour,mage_power_armour,mage_dex_armour,mage_oneshotarmour,mage_chaos_armour,paladin_grace_armour,paladin_blessed_armour,paladin_the_wall,paladin_steel_armour,paladin_shield_armour,necromancer_dark_cloak,necromancer_wraith_armour,necromancer_black_armour,necromancer_black_steel_armour,necromancer_ghost_armour,barbarian_endurance_armour,barbarian_flame_armour,barbarian_hard_leather_armour,barbarian_white_steel_armour,barbarian_brass_armour,lancer_speed_armour,lancer_protection_armour,lancer_woven_armour,lancer_ice_armour,lancer_white_iron_armour,archer_frost_armour,archer_agility_armour,archer_ash_armour,archer_black_leather_armour,samurai_daredevil_armour,samurai_sakaretsu_armour,samurai_emperor_armour,samurai_ronin_armour,samurai_ebon_armour] #add acsessorys to new array
items.extend(items1)
items2=[samurai_blue_armour,samurai_orange_armour,samurai_yellow_armour,samurai_green_armour,samurai_red_armour,samurai_battle_worn_armour,ninja_light_dan_gi,ninja_light_kyu_gi,ninja_heavy_kyu_gi,ninja_heavy_dan_gi,ninja_darkness_armour,warrior_cleaver,warrior_voltsword,warrior_balanced_sword,warrior_goddess_sword,warrior_sword_of_winds,warrior_sword_of_ages,warrior_silver_sword,mage_weaving_wand,mage_dragon_wand,mage_serpent_wand,mage_one_shot_wand,mage_twilight_wand,mage_corrupted_wand,mage_apocalypse_wand,paladin_light_hammer,paladin_lightbringer,paladin_hammer_of_dawn,paladin_holy_axe,paladin_life_hammer,paladin_heavy_hammer,paladin_hammer_of_judgement,necromancer_dark_shield,necromancer_shadow_blade,necromancer_crystal_ball,necromancer_black_staff,necromancer_dimension_blade,necromancer_bone_staff,necomancer_night_staff,barbarian_dragon_sword,barbarian_bloodaxe,barbarian_battle_axe,barbarian_twin_axe,barbarian_hammer]   #adds items to the array
items.extend(items2)
items3=[barbarian_dragon_blade,lancer_trident,lancer_glaive,lancer_conquest_lance,lancer_war_lance,lancer_famine_lance,lancer_death_lance,lancer_oni_lance,archer_crossbow,archer_hermes_bow,archer_explosive_bow,archer_black_bow,archer_greatbow,archer_shotgun,samurai_dark_katana,samurai_light_katana,samurai_gold_katana,samurai_scimitar,samurai_twinblade,samurai_wakizashi,samurai_aluminium_katana,ninja_jo_staff,ninja_bo_staff,ninja_extended_bo_staff,ninja_surikens,ninja_kunai,ninja_dagger,ninja_tashi,basic_crossbow,medium_crossbow,strong_crossbow,basic_halberd]
items.extend(items3)

#load items
file=open("amount.txt","r")
amount1=int(file.readline())
file.close()
f = open("items.txt","r")
amount1=amount1-1
for i in range (amount1):
    item=f.readline()
    inventry.append(items[int(item)])
f.close()

item_no=0
while item_no < len(items):
    shop.append(str(items[item_no]))
    item_no=item_no+1

file=open("equip0.txt","r")
pequip=int(file.readline())
equipItem(inventry[pequip][6],inventry[pequip][4],pequip)
file.close()
file=open("equip1.txt","r")
pequip=int(file.readline())
equipItem(inventry[pequip][6],inventry[pequip][4],pequip)
file.close()

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
#print(store)

#length of shop
length=len(store[1])
while 1>0:
    instruction=input("What would you like to do?")
    if instruction==("\money"):
        screen.fill(BLACK)
        message_display("small orbs " + str(money[0]) + ", medium orbs " + str(money[1]) + ", large orbs " + str(money[2]) + ", special orbs " +str(money[3]),300,30,16,WHITE)
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
        while loop<length:
            print("Item "+str(loop)+" - "+items[loop][4]+" costs "+str(store[1][loop])+" from obrb type "+str(store[2][loop]))
            loop=loop+1
        print("Type \"leave\" to leave shop")
        to_buy=input("Input item number to buy")
        check=is_number(to_buy) #check user has entered a number
        #check="TRUE" #uncomment to accept letters
        if check=="TRUE":
            if int(to_buy)<=int(length): #check number isnt too big
                print("You have attempted to buy "+str(items[int(to_buy)][4]))
                price=(store[1][int(to_buy)])
                type=store[2][int(to_buy)]
                if store[2][int(to_buy)]=="S":
                    amount=money[0]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        save_item(to_buy)
                        file=open("money_s.txt","w")
                        file.write(str(money[0]))
                        file.close()
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
                elif store[2][int(to_buy)]=="M":
                    amount=money[1]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        save_item(to_buy)
                        file=open("money_m.txt","w")
                        file.write(str(money[1]))
                        file.close()
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
                elif store[2][int(to_buy)]=="L":
                    amount=money[2]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        save_item(to_buy)
                        file=open("money_l.txt","w")
                        file.write(str(money[2]))
                        file.close()
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
                elif store[2][int(to_buy)]=="X":
                    amount=money[3]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        save_item(to_buy)
                        file=open("money_x.txt","w")
                        file.write(str(money[3]))
                        file.close()
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
            else:
                print("Error - item not recognised")
        else:
            print("Error - please enter a number, you have been returned to the main menu")
    elif instruction==("\data"):
        loop=0
        option=input(print("Weapons (1), armour (2) or cloths (3)"))
        option=int(option)-1
        while loop<length:
            if items[int(loop)][6]==int(option):
                print("Item "+str(loop)+" - "+store[0][loop])
            loop=loop+1
        to_buy=input("Input item number to get data on")
        check=is_number(to_buy) #check user has entered a number
        #check="TRUE" #uncomment to accept letters
        if check=="TRUE":
            print("item number not found")
            print("You have requested data on ",store[0][int(to_buy)])
            print("Strength = ",items[int(to_buy)][0])
            print("Endurance = ",items[int(to_buy)][1])
            print("Dexterity = ",items[int(to_buy)][2])
            print("Spell = ",items[int(to_buy)][3])
            #4 is used for name
            print("Class = ",items[int(to_buy)][5])
            print("Type = ",items[int(to_buy)][6])
            #7 used for description, placed at end
            print("Range = ",items[int(to_buy)][8])
            print("Bellow is a description of the item: \n,",items[int(to_buy)][7])
        else:
            print("please enter numeric numbers only")
    elif instruction==("\convert"):
        convert_f=input("Convert from (S,M or L)")
        if convert_f=="S":
            print("You can only convert downwards.")
        elif convert_f=="M":
            amount=int(input("How many medium orbs would you like to convert?"))
            if money[1]>=amount:
                print("Ok")
                #Convert code to go here
            else:
                print("You don't have that many")
        elif convert_f=="L":
            amount=int(input("How many large orbs would you like to convert?"))
            if money[2]>=amount:
                print("Ok")
                #Convert code to go here
            else:
                print("You don't have that many")
        else:
            print("Error - use capital S, M and L only")
    elif instruction==("\help"):
        print("Availbe commands: \n \shop = shop \n \money = see availbe orbs \n \+money = change current money \n \management = manage your inventory & equip items. New way to see what you own. \n \data = find out the statistics of an item")
    elif instruction==("\management"):
        pinventory()
    else:
        print("Error - command not recognised - uses \"\help\" for a list of instructions.")
