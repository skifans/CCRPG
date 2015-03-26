"""
        INVENTORY
TO DO:
    -USE  /
    -TAKE /
    -SORT /
    -MAX 1 ARMOUR + WEAPON /
    -UNEQUIP ITEM /
    -MAKE SHIT WORK (Half-done - Awaiting finished weapons list)
"""
"""
Update by Alex D (23.3.15)
Works with 3.2
Probably broke some bitts
"""
warrior_basic_armour = [10,15,5,0,"basic warrior armour",1,1,"basic armour for beginners",0,30,0,0,0]
warrior_medium_armour = [15,20,10,0,"medium warrior armour",1,1,"better armour for the more experienced",0,45,0,0,0]
warrior_strong_armour = [20,35,15,0,"strong warrior armour",1,1,"very good quality armour",0,70,0,0,0]
warrior_elite_armour = [30,45,25,0,"elite warrior armour",1,1,"elite armour of a great quality",0,0,10,0,0]
warrior_ultimate_armour = [150,225,125,0,"hero's tunic",1,1,"armour of a legendary warrior",0,0,0,5,0]

mage_basic_armour = [0,5,10,15,"basic mage armour",2,1,"basic armour for beginners",0,30,0,0,0]
mage_medium_armour = [0,10,15,20,"medium mage armour",2,1,"better armour for the more experienced",0,45,0,0,0]
mage_strong_armour = [0,15,25,30,"strong mage armour",2,1,"very good quality armour",0,70,0,0,0]
mage_elite_armour = [0,25,35,40,"elite mage armour",2,1,"elite armour of a great quality",0,0,10,0,0]
mage_ultimate_armour = [0,125,175,400,"archmage's cloak",2,1,"WE NEED MORE FIREBALLS",0,0,0,5,0]

paladin_basic_armour = [5,20,5,0,"basic paladin armour",3,1,"basic armour for beginners",0,30,0,0,0]
paladin_medium_armour = [10,25,10,0,"medium paladin armour",3,1,"better armour for the more experienced",0,45,0,0,0]
paladin_strong_armour = [15,40,15,0,"strong paladin armour",3,1,"very good quality armour",0,70,0,0,0]
paladin_elite_armour = [25,50,25,0,"elite paladin armour",3,1,"elite armour of a great quality",0,0,10,0,0]
paladin_ultimate_armour = [125,250,125,0,"armour of favor",3,1,"comes witha cool ring!",0,0,0,5,0]

necromancer_basic_armour = [0,10,0,20,"basic necromancer armour",4,1,"basic armour for beginners",0,30,0,0,0]
necromancer_medium_armour = [0,20,0,25,"medium necromancer armour",4,1,"better armour for the more experienced",0,45,0,0,0]
necromancer_strong_armour = [0,30,0,40,"strong necromancer armour",4,1,"very good quality armour",0,70,0,0,0]
necromancer_elite_armour = [0,40,0,60,"elite nceromancer armour",4,1,"elite armour of a gret quality",0,0,10,0,0]
necromancer_ultimate_armour = [0,200,0,300,"gravelord's cloak",4,1,"cloak of the first of the dead",0,0,0,5,0]

barbarian_basic_armour = [15,5,10,0,"basic barbarian armour",5,1,"basic armour for beginners",0,30,0,0,0]
barbarian_medium_armour = [20,10,15,0,"medium barbarian armour",5,1,"better armour for the more experienced",0,45,0,0,0]
barbarian_strong_armour = [35,15,20,0,"strong barbarian armour",5,1,"very good quality armour",0,70,0,0,0]
barbarian_elite_armour = [45,25,30,0,"elite barbarian armour",5,1,"elite armour of a great quality",0,0,10,0,0]
barbarian_ultimate_armour = [225,125,150,0,"enraging armour",5,1,"get angry and smash!",0,0,10,0,0]

lancer_basic_armour = [20,0,10,0,"basic lancer armour",6,1,"basic armour for beginners",0,30,0,0,0]
lancer_medium_armour = [25,5,15,0,"medium lancer armour",6,1,"better armour for the more experienced",0,45,0,0,0]
lancer_strong_armour = [40,10,20,0,"strong laancer armour",6,1,"very good quality armour",0,70,0,0,0]
lancer_elite_armour = [50,20,30,0,"elite lancer armour",6,1,"elite armour of a great quality",0,0,10,0,0]
lancer_ultimate_armour = [250,100,150,0,"lancelord armor",6,1,"ancient lancer armour imbued with fire",0,0,0,5,0]

archer_basic_armour = [5,10,15,0,"basic archer armour",7,1,"basic armour for beginners",0,30,0,0,0]
archer_medium_armour = [10,15,20,0,"medium archer armour",7,1,"better armour for the more expeienced",0,45,0,0,0]
archer_strong_armour = [15,20,35,0,"strong archer armour",7,1,"very good quality armour",0,70,0,0,0]
archer_elite_armour = [25,30,45,0,"elite archer armour",7,1,"elite armour of a great qualit",0,0,10,0,0]
archer_ultimate_armour = [125,150,225,0,"armour of retribution",7,1,"will have your enemies quivering with fear!",0,0,0,5,0]

warrior_basic_weapon = [15,5,10,0,"basic warrior sword",1,0,"a basic sword for beginners",0,30,0,0,0]
warrior_medium_weapon = [20,10,15,0,"medium warrior sword",1,0,"a better sword for the more experienced",0,45,0,0,0]
warrior_strong_weapon = [35,15,20,0,"strong warrior sword",1,0,"a very good quality sword",0,70,0,0,0]
warrior_elite_weapon = [45,25,30,0,"elite warrior sword",1,0,"an elite sword of a great quality",0,0,10,0,0]
warrior_ultimate_weapon = [225,125,150,0,"the master sword",1,0,"we all know what this is",0,0,0,5,0]

mage_basic_weapon = [0,5,5,20,"basic mage wand",2,0,"a basic wand for beginners",0,30,0,0,0]
mage_medium_weapon = [0,10,10,25,"medium mage wand",2,0,"a better wand for the more experienced",0,45,0,0,0]
mage_strong_weapon = [0,15,15,40,"strong mage wand",2,0,"a very good quality wand",0,70,0,0,0]
mage_elite_weapon = [0,25,25,50,"elite mage wand",2,0,"an elite wand of a great quality",0,0,100,0,0]
mage_ultimate_weapon = [0,125,125,250,"veigar's staff",2,0,"the power to command dark matter is cool",0,0,0,5,0]

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

inventry=[warrior_basic_armour,warrior_medium_armour,warrior_strong_armour,warrior_elite_armour,warrior_ultimate_armour,mage_basic_armour,mage_medium_armour,mage_strong_armour,mage_ultimate_armour,paladin_basic_armour,paladin_medium_armour,paladin_strong_armour,paladin_elite_armour,paladin_ultimate_armour,necromancer_basic_armour,necromancer_medium_armour,necromancer_strong_armour,necromancer_elite_armour,necromancer_ultimate_armour,barbarian_basic_armour,barbarian_medium_armour,barbarian_strong_armour,barbarian_elite_armour,barbarian_ultimate_armour,lancer_basic_armour,lancer_medium_armour,lancer_strong_armour,lancer_elite_armour,lancer_ultimate_armour,archer_basic_armour,archer_medium_armour,archer_strong_armour,archer_elite_armour,archer_ultimate_armour,warrior_basic_weapon,warrior_medium_weapon,warrior_strong_weapon,warrior_elite_weapon,warrior_ultimate_weapon,mage_basic_weapon,mage_medium_weapon,mage_strong_weapon,mage_elite_weapon,mage_ultimate_weapon] #maximum defininf length
inventry_accsesorys=[berserkers_band,priest_band,Fire_gem_circlet,major_ring,ring_of_random_change,blinding_cranium_crab,swiss_army_claymore,arrow_target,blight_sludge,overpowered_stick,boss_shield,sleepy_stick,lol,necrotic_bone,mr_tiddles] #add acsessorys to new array
inventry.extend(inventry_accsesorys) #add accsesorys to end of items array

global inventry
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
currentHandItemMessage = "You are currenty wielding a" + str(weapons)
pickUpMessage = "You have picked up a "
dropItemMessage = "You have dropped a "
failedToEquipMessage = "Therefore you were unable to equip the item."
currentArmourMessage = "You are wearing " + str(armour)
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
def equipItem(obj, name):
    global armour, weapons
    print("obj =",obj)
    if obj == 0:
        weapon = name
        #Enter Addition To Stats (Waiting for finished weapons)
        print(currentHandItemMessage + str(name) + ".")
        return weapon
    elif obj == 1:
        armour = name
        ##endurance += int(armour[1])
        print(currentArmourMessage + str(name) + ".")
        return armour
    elif obj==2:
        print("clothing is not yet supported")
    else:
        print("error line 184")



#Function to unequip yet keep in inventory
def unEquipItem(obj):
    #not used
    global armour, weapons
    if obj == 1:
        #Resets name of current armour & resets the appropriate stats.
        armour = " "
        ##endurance -= obj[1]
        ##dexterity -= obj[2]
        print(unEquipArmourMessage)

    elif obj == 0:
        weapon = " "
        #Enter Reverse Stats of Weapon (Waiting for finished weapons)
        print(unEquipWeaponMessage)


#Testing... 1,2,3
def pinventory(currentHandItem,currentArmour):
    global inventry
    global armour, weapons
    length = 0
    while length<len(inventry):
        #print(inventry[length][4])
        length = length + 1
    print("You are currently holding:",weapons)
    print("You are currently wearing:",armour)
    print("Your options are:")
    print("unequip equip")
    pdecide = input()
    if pdecide == "equip":
        print("Choose what you want to equip")
        length=0
        while length<len(inventry):
            print("item number",length,"is",inventry[length][4])
            length = length + 1
        pequip = input("Enter item number")
        pequip = int(pequip)
        if pequip<=len(inventry):
            equipItem(inventry[pequip][6],inventry[pequip][4])
        else:
            print("item not found")
    if pdecide == "unequip":
        armour = ""
        weapn = ""
pinventory(currentHandItem,currentArmour)
pinventory(currentHandItem,currentArmour)
pinventory(currentHandItem,currentArmour)
