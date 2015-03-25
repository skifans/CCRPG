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
neromancer_night_staff = [0,1000,0,2000,"night staff",4,0,"a staff only for the best of necromancers",0,0,0,30,0]

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

global inventry
inventry = [basic_halberd,ninja_darkness_armour]
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
    print(obj)
    print(obj)
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
    else:
        print("error line 347")



#Function to unequip yet keep in inventory
def unEquipItem(obj):
    global armour, weapons
    if obj[6] == 1:
        #Resets name of current armour & resets the appropriate stats.
        armour = " "
        ##endurance -= obj[1]
        ##dexterity -= obj[2]
        print(unEquipArmourMessage)

    elif obj[6] == 0:
        weapon = " "
        #Enter Reverse Stats of Weapon (Waiting for finished weapons)
        print(unEquipWeaponMessage)


#Testing... 1,2,3
def pinventory(currentHandItem,currentArmour):
    global inventry
    global armour, weapons
    length = 0
    while length<len(inventry):
        print(inventry[length][4])
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
        if pequip in str(inventry):
            pequip = int(pequip)
            equipItem(inventry[pequip][6],inventry[pequip][4])
        else:
            print("error")
pinventory(currentHandItem,currentArmour)
pinventory(currentHandItem,currentArmour)