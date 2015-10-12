# This is the file with all the enemies and their stats
"""
0.Vitality
1.Endurance
2.Dexterity
3.Intelligence
4.Strength
5.Weapon
6.Armour
7.Name
8.Exp
8.5. exp required for level up (player only)
9.level
10.inventory
11.small_orbs
11.1.medium_orbs
11.2.large_orbs
11.3.mega_orbs
"""
class darkness:
	magnus = [10,25,15,30,20,["The sword of darkness",20],["The armour of despair",30],"Magnus, captain of despair",20,1,0,0,0]
class water:
	sea_horse = [15,10,60,9001,0,["splash",0],["sea_weed",10],"Sea Horse",10,0,1,0,0]
	dolphin = [20,50,30,80,40,["tail",30],["fish bone exoskeleton",20],"Dolphin",40,0,1,0,0]
	fish = [10,25,15,30,20,["flipper",15],["scales",10],"Fish",20,1,0,0,0]
	shark = [40,60,30,10,80,["Teeth",50],["Dolphin bone exoskeleton",40],"Shark",80,0,2,0,0]
	whale = [80,70,30,40,90,["shark", 80],["Shark bone exoskeleton",60],"Whale",120,0,0,1,0]
	water_wizard = [30,30,40,60,10,["Staff of water", 20],["shark bone exoskeleton",30],"Water wizard",100,0,3,0,0]
class earth:
	tree = [80,80,20,10,50,["Branch",20],["Bark",40],"Tree",70,0,3,0,0]
	earth_wizard = [60,60,80,120,20,["Staff of earth", 40],["Rocks",30],"Earth wizard",200,0,6,0,0]
class fire:
	fire_bat = [30,20,60,10,40,["fire wings",30],["Fire!!!",20],"Fire bat",40,0,5,0,0]
	fire_wizard = [90,90,120,180,30,["Staff of fire", 20],["magma",50],"Fire wizard",300,0,9,0,0]
class air:
	air_wizard = [120,120,160,240,40,["Staff of winds", 20],["Air currents",30],"Air wizard",400,0,12,0,0]
class heaven:
	priest = [150,150,200,300,40,["Staff of light", 20],["Holy light",30],"Priest",500,0,15,0,0]

