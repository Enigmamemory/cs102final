import pygame, sys, math, random
from pygame.locals import *

class GameCursor: #cursor class
    
    def __init__(self, x, y, thing):
        self.x = x
        self.y = y
        self.thing = thing

    def display(self): #draws GameCursor on screen
        if self.thing == 'None':
            pass
        if self.thing == 'Tower1': #if thing is Tower1, cursor will be this
            pygame.draw.circle(screen,
                               (0,0,255),
                               (self.x, self.y),
                               10,
                               1)
            pygame.draw.circle(screen,
                               (255,0,0),
                               (self.x,self.y),
                               60,
                               2)
        if self.thing == 'Tower2': #ditto if thing is Tower2
            pygame.draw.circle(screen,
                               (0,255,255),
                               (self.x, self.y),
                               10,
                               1)
            pygame.draw.circle(screen,
                               (255,0,0),
                               (self.x,self.y),
                               90,
                               2)
        if self.thing == 'Tower3':
            pygame.draw.circle(screen,
                               (0,255,108),
                               (self.x, self.y),
                               10,
                               1)
            pygame.draw.circle(screen,
                               (0,255,0),
                               (self.x,self.y),
                               60,
                               2)

class Tower1: #Tower1 functions

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,0,255)
        self.thickness = 1
        self.target = None
        self.damage = 30
        self.frange = 60
        self.cd = 20
        self.count = 0
        self.burnout = False
        self.name = 'Standard Turret'
        self.cost = 50

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower1U1:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,0,255)
        self.thickness = 1
        self.target = None
        self.damage = 45
        self.frange = 60
        self.cd = 20
        self.count = 0
        self.burnout = False
        self.name = 'Upgraded Turret'
        self.cost = 200

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower1U2:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,0,255)
        self.thickness = 1
        self.target = None
        self.damage = 15
        self.frange = 45
        self.cd = 5
        self.count = 0
        self.burnout = False
        self.name = 'Vulcan Turret'
        self.cost = 350

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower1U3:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,0,255)
        self.thickness = 1
        self.target = None
        self.damage = 80
        self.frange = 120
        self.cd = 40
        self.count = 0
        self.burnout = False
        self.name = 'Upgraded Turret'
        self.cost = 250

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)



class Tower2: #Tower2 functions

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,255)
        self.thickness = 1
        self.field = []
        self.damage = 0
        self.frange = 90
        self.cd = 15
        self.count = 0
        self.burnout = False
        self.name = 'Gravity Field'
        self.cost = 75

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower2U1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,255)
        self.thickness = 1
        self.field = []
        self.damage = 0
        self.frange = 90
        self.cd = 15
        self.count = 0
        self.burnout = False
        self.name = 'Dense Gravity Field'
        self.cost = 400

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower2U2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,255)
        self.thickness = 1
        self.field = []
        self.damage = 12
        self.frange = 60
        self.cd = 15
        self.count = 0
        self.burnout = False
        self.name = 'Quake Field'
        self.cost = 500

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower2U3:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,255)
        self.thickness = 1
        self.field = []
        self.damage = 5
        self.frange = 150
        self.cd = 15
        self.count = 0
        self.burnout = False
        self.name = 'Plasma Field'
        self.cost = 500

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower3:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,108)
        self.thickness = 1
        self.damage = 5
        self.frange = 60
        self.name = 'Support Tower'
        self.cost = 300

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower3U1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,108)
        self.thickness = 1
        self.damage = 10
        self.frange = 80
        self.name = 'Tech Tower'
        self.cost = 600

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower3U2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,108)
        self.thickness = 1
        self.frange = 50
        self.name = 'Weapon Facility'
        self.cost = 750

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Tower3U3:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.colour = (0,255,108)
        self.thickness = 1
        self.damage = 5
        self.frange = 125
        self.name = 'Radio Tower'
        self.cost = 750

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (self.x, self.y),
                           self.size,
                           self.thickness)

class Enemy1: #Enemy1 stuff

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 7
        self.colour = (200,0,0)
        self.thickness = 3
        self.move = 1
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 50
        self.cost = 10
        self.name = 'Redshirt'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy1A:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 7
        self.colour = (0,0,200)
        self.thickness = 3
        self.move = 1.2
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 80
        self.cost = 30
        self.name = 'Blueshirt'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy1B:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 7
        self.colour = (0,200,0)
        self.thickness = 3
        self.move = 1.4
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 120
        self.cost = 60
        self.name = 'Greenshirt'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy2:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 13
        self.colour = (200,200,200)
        self.thickness = 3
        self.move = 0.8
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 90
        self.cost = 20
        self.name = 'Brute'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy2A:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 16
        self.colour = (150,150,150)
        self.thickness = 3
        self.move = 0.7
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 120
        self.cost = 70
        self.name = 'Pack'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy2B:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 20
        self.colour = (100,100,100)
        self.thickness = 3
        self.move = 0.6
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 150
        self.cost = 120
        self.name = 'Horde'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy3:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 5
        self.colour = (255,0,255)
        self.thickness = 0
        self.move = 1.3
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 40
        self.cost = 20
        self.name = 'Speedling'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy3A:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 5
        self.colour = (200,0,255)
        self.thickness = 0
        self.move = 1.6
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 65
        self.cost = 60
        self.name = 'Quickling'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy3B:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 5
        self.colour = (150,0,255)
        self.thickness = 0
        self.move = 2
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 110
        self.cost = 100
        self.name = 'Barreling'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

class Enemy4:

    def __init__ (self, start):
        self.x = 0
        self.y = 0
        self.start = start
        self.size = 14
        self.colour = (255,108,0)
        self.thickness = 3
        self.move = 1
        self.angle = 0
        self.mileage = 0
        self.corner = 0
        self.cornermax = 0
        self.hp = 200
        self.cost = 150
        self.name = 'Honcho'

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)



class Roadmark: #Roadmark functions

    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.size = 4
        self.colour = colour
        self.thickness = 0

    def display(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)



background_colour = (255,255,255)
screen = pygame.display.set_mode((800,600), DOUBLEBUF)
clock = pygame.time.Clock()
gameticks = 0
spawn_over = False
current_level = 1
grace_period = True
show_range = False
q_upgrade = False
w_upgrade = False
e_upgrade = False
gold = 100
playerhp = 20
gameover = False
winner = False

selected = []

tower1_list = []
tower1u1_list = []
tower1u2_list = []
tower1u3_list = []
tower2_list = []
tower2u1_list = []
tower2u2_list = []
tower2u3_list = []
tower3_list = []
tower3u1_list = []
tower3u2_list = []
tower3u3_list = []

left_mark = []
right_mark = []
up_mark = []
down_mark = []

left_path = []
right_path = []
up_path = []
down_path = []

enemy1_list = []
enemy2_list = []
enemy3_list = []
enemy4_list = []
enemy1a_list = []
enemy2a_list = []
enemy3a_list = []
enemy1b_list = []
enemy2b_list = []
enemy3b_list = []


def reset():

    global background_colour
    global screen
    global clock
    global gameticks
    global spawn_over
    global current_level
    global grace_period
    global show_range
    global q_upgrade
    global w_upgrade
    global e_upgrade
    global gold
    global playerhp
    global gameover
    global winner
    
    global selected
    
    global tower1_list
    global tower1u1_list
    global tower1u2_list
    global tower1u3_list
    global tower2_list
    global tower2u1_list
    global tower2u2_list
    global tower2u3_list 
    global tower3_list
    global tower3u1_list
    global tower3u2_list
    global tower3u3_list

    global left_mark 
    global right_mark
    global up_mark
    global down_mark

    global left_path
    global right_path
    global up_path
    global down_path

    global enemy1_list
    global enemy2_list
    global enemy3_list
    global enemy4_list
    global enemy1a_list
    global enemy2a_list
    global enemy3a_list
    global enemy1b_list
    global enemy2b_list
    global enemy3b_list

background_colour = (255,255,255)
screen = pygame.display.set_mode((800,600), DOUBLEBUF)
clock = pygame.time.Clock()
gameticks = 0
spawn_over = False
current_level = 1
grace_period = True
show_range = False
q_upgrade = False
w_upgrade = False
e_upgrade = False
gold = 100
playerhp = 20
gameover = False
winner = False

selected = []

tower1_list = []
tower1u1_list = []
tower1u2_list = []
tower1u3_list = []
tower2_list = []
tower2u1_list = []
tower2u2_list = []
tower2u3_list = []
tower3_list = []
tower3u1_list = []
tower3u2_list = []
tower3u3_list = []

left_mark = []
right_mark = []
up_mark = []
down_mark = []

left_path = []
right_path = []
up_path = []
down_path = []

enemy1_list = []
enemy2_list = []
enemy3_list = []
enemy4_list = []
enemy1a_list = []
enemy2a_list = []
enemy3a_list = []
enemy1b_list = []
enemy2b_list = []
enemy3b_list = []




def can_purchase(cost):
    global gold
    return ((gold - cost) >= 0)

def purchase(cost):
    global gold
    if can_purchase(cost):
        gold -=  cost
        print ('Purchase Successful')
    else:
        print ('You need more gold to purchase this')
    print ('Gold: ' + str(gold))

def redeem(cost):
    global gold
    gold += cost
    print ('Return Successful')
    print ('Gold: ' + str(gold))

def print_tower(tower):
    print (tower.name)

def remove_tower(tower):
    if tower1_list.count(tower) > 0:
        tower1_list.remove(tower)
    elif tower1u1_list.count(tower) > 0:
        tower1u1_list.remove(tower)
    elif tower1u2_list.count(tower) > 0:
        tower1u2_list.remove(tower)
    elif tower1u3_list.count(tower) > 0:
        tower1u3_list.remove(tower)
    elif tower2_list.count(tower) > 0:
        tower2_list.remove(tower)
    elif tower2u1_list.count(tower) > 0:
        tower2u1_list.remove(tower)
    elif tower2u2_list.count(tower) > 0:
        tower2u2_list.remove(tower)
    elif tower2u3_list.count(tower) > 0:
        tower2u3_list.remove(tower)
    elif tower3_list.count(tower) > 0:
        tower3_list.remove(tower)
    elif tower3u1_list.count(tower) > 0:
        tower3u1_list.remove(tower)
    elif tower3u2_list.count(tower) > 0:
        tower3u2_list.remove(tower)
    elif tower3u3_list.count(tower) > 0:
        tower3u3_list.remove(tower)
    redeem(tower.cost)
    selected.remove(tower)


def towerAI():
    cooldown()
    tower1_shoot()
    tower1u1_shoot()
    tower1u2_shoot()
    tower1u3_shoot()
    tower2_shoot()
    tower2u1_shoot()
    tower2u2_shoot()
    tower2u3_shoot()
    

def damage(tower,enemy):
    damage = tower.damage
    for stuff in tower3_list:
        #print (inrange(stuff,tower))
        if inrange(stuff,tower):
            damage += stuff.damage
            break
    for stuff in tower3u1_list:
        if inrange(stuff,tower):
            damage += stuff.damage
            break
    for stuff in tower3u3_list:
        if inrange(stuff,tower):
            damage += stuff.damage
            break
    #print (damage)
    enemy.hp -= tower.damage

def burnout(tower):
    tower.burnout = not tower.burnout

def cooldown():
    for tower in tower1_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower1u1_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower1u2_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower1u3_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower2_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower2u1_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower2u2_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break
    for tower in tower2u3_list:
        if tower.burnout:
            if tower.count >= tower.cd:
                burnout(tower)
                tower.count = 0
            else:
                tower.count += 1
                for stuff in tower3u2_list:
                    if inrange(stuff,tower):
                        tower.count += 1
                        break

def tower1_shoot():
    for tower in tower1_list:
        #print (tower.burnout)
        if tower.target != None: #if target already determined
            if inrange(tower,tower.target) and tower.target.hp > 0: #and is in range
                if tower.burnout == False: #and tower is not on cooldown
                    damage(tower,tower.target) #shoot'em
                    burnout(tower)
            else:
                tower.target = None #else declare no target
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy4_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        #print (tower.burnout)

def tower1u1_shoot():
    for tower in tower1u1_list:
        #print (tower.burnout)
        if tower.target != None: #if target already determined
            if inrange(tower,tower.target) and tower.target.hp > 0: #and is in range
                if tower.burnout == False: #and tower is not on cooldown
                    damage(tower,tower.target) #shoot'em
                    burnout(tower)
            else:
                tower.target = None #else declare no target
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy4_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        #print (tower.burnout)

def tower1u2_shoot():
    for tower in tower1u2_list:
        #print (tower.burnout)
        if tower.target != None: #if target already determined
            if inrange(tower,tower.target) and tower.target.hp > 0: #and is in range
                if tower.burnout == False: #and tower is not on cooldown
                    damage(tower,tower.target) #shoot'em
                    burnout(tower)
            else:
                tower.target = None #else declare no target
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy4_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        #print (tower.burnout)

def tower1u3_shoot():
    for tower in tower1u3_list:
        #print (tower.burnout)
        if tower.target != None: #if target already determined
            if inrange(tower,tower.target) and tower.target.hp > 0: #and is in range
                if tower.burnout == False: #and tower is not on cooldown
                    damage(tower,tower.target) #shoot'em
                    burnout(tower)
            else:
                tower.target = None #else declare no target
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy1b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy2b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3a_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy3b_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        if tower.target == None: #ensures that as soon as tower loses target it gets new one
            for enemy in enemy4_list: #check list of enemies
                if inrange(tower,enemy):
                    tower.target = enemy
                    if tower.burnout == False:
                        damage(tower,enemy)
                        burnout(tower)
                    break
        #print (tower.burnout)

def tower2_shoot():
    for tower in tower2_list:
        tower.field = []
        for enemy in enemy1_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy4_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        if tower.burnout == False:
            for enemy in tower.field:
                damage(tower,enemy)
            if len(tower.field) > 0:
                burnout(tower)
        
def tower2u1_shoot():
    for tower in tower2u1_list:
        tower.field = []
        for enemy in enemy1_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy4_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        if tower.burnout == False:
            for enemy in tower.field:
                damage(tower,enemy)
            if len(tower.field) > 0:
                burnout(tower)

def tower2u2_shoot():
    for tower in tower2u2_list:
        tower.field = []
        for enemy in enemy1_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy4_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        if tower.burnout == False:
            for enemy in tower.field:
                damage(tower,enemy)
            if len(tower.field) > 0:
                burnout(tower)

def tower2u3_shoot():
    for tower in tower2u3_list:
        tower.field = []
        for enemy in enemy1_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy1b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy2b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3a_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy3b_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        for enemy in enemy4_list:
            if inrange(tower,enemy):
                tower.field.append(enemy)
        if tower.burnout == False:
            for enemy in tower.field:
                damage(tower,enemy)
            if len(tower.field) > 0:
                burnout(tower)

def upgradeQ(tower):
    if tower.name == 'Standard Turret':
        new_tower = Tower1U1(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower1u1_list.append(new_tower)
            tower1_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')
    if tower.name == 'Gravity Field':
        new_tower = Tower2U1(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower2u1_list.append(new_tower)
            tower2_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')
    if tower.name == 'Support Tower':
        new_tower = Tower3U1(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower3u1_list.append(new_tower)
            tower3_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')

def upgradeW(tower):
    if tower.name == 'Standard Turret':
        new_tower = Tower1U2(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower1u2_list.append(new_tower)
            tower1_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')
    if tower.name == 'Gravity Field':
        new_tower = Tower2U2(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower2u2_list.append(new_tower)
            tower2_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')
    if tower.name == 'Support Tower':
        new_tower = Tower3U2(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower3u2_list.append(new_tower)
            tower3_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')


def upgradeE(tower):
    if tower.name == 'Standard Turret':
        new_tower = Tower1U3(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower1u3_list.append(new_tower)
            tower1_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')
    if tower.name == 'Gravity Field':
        new_tower = Tower2U3(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower2u3_list.append(new_tower)
            tower2_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')
    if tower.name == 'Support Tower':
        new_tower = Tower3U3(tower.x,tower.y)
        if can_purchase((new_tower.cost - tower.cost)):
            tower3u3_list.append(new_tower)
            tower3_list.remove(tower)
            remove_tower(tower)
            purchase(new_tower.cost)
        else:
            print('You need more gold to purchase this')


def enemyAI():
    enemy_dead()
    enemy_move()

def enemy_dead():
    global gold
    for enemy in enemy1_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            #print (gold)
            enemy1_list.remove(enemy)
    for enemy in enemy1a_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            #print (gold)
            friends1 = Enemy1(enemy.start)
            friends2 = Enemy1(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x - 5
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            enemy1_list.append(friends1)
            enemy1_list.append(friends2)
            enemy1a_list.remove(enemy)
    for enemy in enemy1b_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            friends1 = Enemy1(enemy.start)
            friends2 = Enemy1(enemy.start)
            friends3 = Enemy1(enemy.start)
            friends4 = Enemy1(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x - 5
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            friends3.x = enemy.x + 10
            friends3.y = enemy.y
            friends3.angle = enemy.angle
            friends3.mileage = enemy.mileage
            friends3.corner = enemy.corner
            friends3.cornermax = enemy.cornermax
            friends4.x = enemy.x - 10
            friends4.y = enemy.y
            friends4.angle = enemy.angle
            friends4.mileage = enemy.mileage
            friends4.corner = enemy.corner
            friends4.cornermax = enemy.cornermax
            enemy1_list.append(friends1)
            enemy1_list.append(friends2)
            enemy1_list.append(friends3)
            enemy1_list.append(friends4)
            #print (gold)
            enemy1b_list.remove(enemy)
    for enemy in enemy2_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            #print (gold)
            enemy2_list.remove(enemy)
    for enemy in enemy2a_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            #print (gold)
            friends1 = Enemy2(enemy.start)
            friends2 = Enemy2(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x - 5
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            enemy2_list.append(friends1)
            enemy2_list.append(friends2)
            enemy2a_list.remove(enemy)
    for enemy in enemy2b_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            friends1 = Enemy2(enemy.start)
            friends2 = Enemy2(enemy.start)
            friends3 = Enemy2(enemy.start)
            friends4 = Enemy2(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x - 5
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            friends3.x = enemy.x + 10
            friends3.y = enemy.y
            friends3.angle = enemy.angle
            friends3.mileage = enemy.mileage
            friends3.corner = enemy.corner
            friends3.cornermax = enemy.cornermax
            friends4.x = enemy.x - 10
            friends4.y = enemy.y
            friends4.angle = enemy.angle
            friends4.mileage = enemy.mileage
            friends4.corner = enemy.corner
            friends4.cornermax = enemy.cornermax
            enemy2_list.append(friends1)
            enemy2_list.append(friends2)
            enemy2_list.append(friends3)
            enemy2_list.append(friends4)
            #print (gold)
            enemy2b_list.remove(enemy)
    for enemy in enemy3_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            #print (gold)
            enemy3_list.remove(enemy)
    for enemy in enemy3a_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            #print (gold)
            friends1 = Enemy3(enemy.start)
            friends2 = Enemy3(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x - 5
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            enemy3_list.append(friends1)
            enemy3_list.append(friends2)
            enemy3a_list.remove(enemy)
    for enemy in enemy3b_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            friends1 = Enemy3(enemy.start)
            friends2 = Enemy3(enemy.start)
            friends3 = Enemy3(enemy.start)
            friends4 = Enemy3(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x - 5
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            friends3.x = enemy.x + 10
            friends3.y = enemy.y
            friends3.angle = enemy.angle
            friends3.mileage = enemy.mileage
            friends3.corner = enemy.corner
            friends3.cornermax = enemy.cornermax
            friends4.x = enemy.x - 10
            friends4.y = enemy.y
            friends4.angle = enemy.angle
            friends4.mileage = enemy.mileage
            friends4.corner = enemy.corner
            friends4.cornermax = enemy.cornermax
            enemy3_list.append(friends1)
            enemy3_list.append(friends2)
            enemy3_list.append(friends3)
            enemy3_list.append(friends4)
            #print (gold)
            enemy3b_list.remove(enemy)
    for enemy in enemy4_list:
        if enemy.hp <= 0:
            gold += enemy.cost
            friends1 = Enemy1B(enemy.start)
            friends2 = Enemy2B(enemy.start)
            friends3 = Enemy3B(enemy.start)
            friends1.x = enemy.x + 5
            friends1.y = enemy.y
            friends1.angle = enemy.angle
            friends1.mileage = enemy.mileage
            friends1.corner = enemy.corner
            friends1.cornermax = enemy.cornermax
            friends2.x = enemy.x
            friends2.y = enemy.y
            friends2.angle = enemy.angle
            friends2.mileage = enemy.mileage
            friends2.corner = enemy.corner
            friends2.cornermax = enemy.cornermax
            friends3.x = enemy.x - 5
            friends3.y = enemy.y
            friends3.angle = enemy.angle
            friends3.mileage = enemy.mileage
            friends3.corner = enemy.corner
            friends3.cornermax = enemy.cornermax
            enemy1b_list.append(friends1)
            enemy2b_list.append(friends2)
            enemy3b_list.append(friends3)
            #print (gold)
            enemy4_list.remove(enemy)
        #print(enemy.hp)
    #print('')

def queue_enemy1(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy1_list.append(enemy)

def queue_enemy1a(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy1a_list.append(enemy)

def queue_enemy1b(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy1b_list.append(enemy)

def queue_enemy2(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy2_list.append(enemy)

def queue_enemy2a(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy2a_list.append(enemy)

def queue_enemy2b(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy2b_list.append(enemy)

def queue_enemy3(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy3_list.append(enemy)

def queue_enemy3a(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy3a_list.append(enemy)

def queue_enemy3b(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy3b_list.append(enemy)

def queue_enemy4(enemy):
    if enemy.start == 'left':
        enemy.cornermax = len(left_mark)
        enemy.x = left_mark[0][0]
        enemy.y = left_mark[0][1]
        enemy.angle = left_mark[0][2]
    if enemy.start == 'right':
        enemy.cornermax = len(left_mark)
        enemy.x = right_mark[0][0]
        enemy.y = right_mark[0][1]
        enemy.angle = right_mark[0][2]
    if enemy.start == 'up':
        enemy.cornermax = len(left_mark)
        enemy.x = up_mark[0][0]
        enemy.y = up_mark[0][1]
        enemy.angle = up_mark[0][2]
    if enemy.start == 'down':
        enemy.cornermax = len(left_mark)
        enemy.x = down_mark[0][0]
        enemy.y = down_mark[0][1]
        enemy.angle = down_mark[0][2]
    enemy4_list.append(enemy)

def make_wave(start,time,name,end):
    global gameticks
    global spawn_over
    if gameticks == time:
        enemy = None
        if name == 'Redshirt':
            enemy = Enemy1(start)
            queue_enemy1(enemy)
        if name == 'Blueshirt':
            enemy = Enemy1A(start)
            queue_enemy1a(enemy)
        if name == 'Greenshirt':
            enemy = Enemy1B(start)
            queue_enemy1b(enemy)
        if name == 'Brute':
            enemy = Enemy2(start)
            queue_enemy2(enemy)
        if name == 'Pack':
            enemy = Enemy2A(start)
            queue_enemy2a(enemy)
        if name == 'Horde':
            enemy = Enemy2B(start)
            queue_enemy2b(enemy)
        if name == 'Speedling':
            enemy = Enemy3(start)
            queue_enemy3(enemy)
        if name == 'Quickling':
            enemy = Enemy3A(start)
            queue_enemy3a(enemy)
        if name == 'Barreling':
            enemy = Enemy3B(start)
            queue_enemy3b(enemy)
        if name == 'Honcho':
            enemy = Enemy4(start)
            queue_enemy4(enemy)
        if end:
            spawn_over = True

def enemy_mileage_reset(enemy):
    enemy.mileage = 0

def enemy_forward(enemy):
    speed = enemy.move
    for tower in tower2_list:
        if inrange(tower,enemy):
            speed = speed * 0.6
            break
    for tower in tower2u1_list:
        if inrange(tower,enemy):
            speed = speed * 0.4
            break
    for tower in tower2u3_list:
        if inrange(tower,enemy):
            speed = speed * 0.75
            break
            
    enemy.x += math.sin(enemy.angle) * speed
    enemy.y -= math.cos(enemy.angle) * speed
    enemy.mileage += speed
    #print (speed)

def enemy_corner(enemy):
    enemy.corner += 1
    if enemy.start == 'left':
        enemy.angle = left_mark[enemy.corner][2]
    if enemy.start == 'right':
        enemy.angle = right_mark[enemy.corner][2]
    if enemy.start == 'up':
        enemy.angle = up_mark[enemy.corner][2]
    if enemy.start == 'down':
        enemy.angle = down_mark[enemy.corner][2]

def enemy_onscreen(enemy):
    return all_true([(enemy.x > 0), (enemy.x < 800), (enemy.y > 0), (enemy.y < 600)])

def enemy_move():
    global playerhp
    for enemy in enemy1_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy1_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy1a_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy1a_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy1b_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy1b_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy2_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy2_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy2a_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy2a_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy2b_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy2b_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy3_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy3_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy3a_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy3a_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy3b_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy3b_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')
    for enemy in enemy4_list:
        if enemy_onscreen(enemy):
            if enemy.mileage >= 10:
                if enemy.corner < enemy.cornermax - 1:
                    enemy_corner(enemy)
                    enemy_mileage_reset(enemy)
            enemy_forward(enemy)
        else:
            enemy4_list.remove(enemy)
            playerhp -= 1
            if playerhp <= 0:
                print('Game Over. Play Again? [Y]/[N]')

            '''
        print (enemy.x)
        print (enemy.y)
        print ('')
            '''     

def check_empty(master):
    for things in master:
        if len(things) > 0:
            return False
    return True

def levels():
    global current_level
    global gameticks
    global spawn_over
    global grace_period
    global gold
    global playerhp
    global winner
    if grace_period:
        if gameticks == 0:
            if current_level > 20 and playerhp > 0:
                winner = True
                print ('Congrats, you won! Thanks for playing!')
            else:
                print ('Grace starts now, you have 10 seconds')
                print ('Gold: ' + str(gold))
                print ('HP: ' + str(playerhp))
            
        if gameticks >= 300 and winner == False:
            grace_period = False
            gameticks = 0
            print ('Level ' + str(current_level) + ' begins now')
    else:
        if current_level == 1:
            level1()
        if current_level == 2:
            level2()
        if current_level == 3:
            level3()
        if current_level == 4:
            level4()
        if current_level == 5:
            level5()
        if current_level == 6:
            level6()
        if current_level == 7:
            level7()
        if current_level == 8:
            level8()
        if current_level == 9:
            level9()
        if current_level == 10:
            level10()
        if current_level == 11:
            level11()
        if current_level == 12:
            level12()
        if current_level == 13:
            level13()
        if current_level == 14:
            level14()
        if current_level == 15:
            level15()
        if current_level == 16:
            level16()
        if current_level == 17:
            level17()
        if current_level == 18:
            level18()
        if current_level == 19:
            level19()
        if current_level == 20:
            level20()
        
        
        if spawn_over:
            if check_empty([enemy1_list,
                           enemy2_list,
                           enemy3_list,
                           enemy4_list,
                           enemy1a_list,
                           enemy2a_list,
                           enemy3a_list,
                           enemy1b_list,
                           enemy2b_list,
                           enemy3b_list]):
                current_level += 1
                gameticks = -1
                spawn_over = False
                grace_period = True

def level1():
    global gameticks
    make_wave('left',30,'Redshirt',False)
    make_wave('left',40,'Redshirt',False)
    make_wave('top,',40,'Redshirt',True)

def level2():
    global gameticks
    make_wave('left',30,'Redshirt',False)
    make_wave('left',40,'Redshirt',False)
    make_wave('left',50,'Redshirt',False)
    make_wave('right',40,'Redshirt',False)
    make_wave('right',50,'Redshirt',True)

def level3():
    global gameticks
    make_wave('up',30,'Redshirt',False)
    make_wave('up',35,'Redshirt',False)
    make_wave('up',40,'Redshirt',False)
    make_wave('up',45,'Redshirt',False)
    make_wave('up',50,'Redshirt',True)
    make_wave('left',30,'Redshirt',False)
    make_wave('left',35,'Redshirt',False)
    make_wave('left',40,'Redshirt',False)
    make_wave('right',30,'Redshirt',False)
    make_wave('right',35,'Redshirt',False)

def level4():
    global gameticks
    make_wave('right',30,'Redshirt',False)
    make_wave('right',35,'Redshirt',False)
    make_wave('right',40,'Redshirt',False)
    make_wave('right',45,'Redshirt',False)
    make_wave('right',50,'Redshirt',True)
    make_wave('down',30,'Blueshirt',False)
    make_wave('down',35,'Blueshirt',False)
    make_wave('left',40,'Blueshirt',False)

def level5():
    global gameticks
    make_wave('up',30,'Brute',False)
    make_wave('up',35,'Brute',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',35,'Speedling',False)
    make_wave('right',40,'Speedling',False)
    make_wave('down',30,'Blueshirt',False)
    make_wave('down',35,'Blueshirt',False)
    make_wave('down',40,'Blueshirt',True)
    

def level6():
    global gameticks
    make_wave('right',30,'Speedling',False)
    make_wave('right',40,'Speedling',False)
    make_wave('right',50,'Speedling',False)
    make_wave('right',60,'Speedling',False)
    make_wave('right',70,'Speedling',True)
    make_wave('down',30,'Speedling',False)
    make_wave('down',40,'Speedling',False)
    make_wave('down',50,'Speedling',False)
    make_wave('down',60,'Speedling',False)
    make_wave('down',70,'Speedling',False)

def level7():
    global gameticks
    make_wave('up',30,'Pack',False)
    make_wave('up',32,'Pack',False)
    make_wave('up',34,'Pack',False)
    make_wave('up',36,'Pack',False)
    make_wave('up',38,'Pack',False)
    make_wave('up',40,'Pack',False)
    make_wave('up',42,'Pack',False)
    make_wave('up',44,'Pack',True)

def level8():
    global gameticks
    make_wave('up',30,'Pack',False)
    make_wave('up',35,'Pack',False)
    make_wave('up',40,'Speedling',False)
    make_wave('up',42,'Quickling',False)
    make_wave('down',30,'Pack',False)
    make_wave('down',35,'Pack',False)
    make_wave('down',40,'Speedling',False)
    make_wave('down',42,'Quickling',False)
    make_wave('left',30,'Pack',False)
    make_wave('left',35,'Pack',False)
    make_wave('left',40,'Speedling',False)
    make_wave('left',42,'Quickling',False)
    make_wave('right',30,'Pack',False)
    make_wave('right',35,'Pack',False)
    make_wave('right',40,'Speedling',False)
    make_wave('right',42,'Quickling',True)

def level9():
    global gameticks
    make_wave('down',30,'Blueshirt',False)
    make_wave('down',31,'Blueshirt',False)
    make_wave('down',32,'Blueshirt',False)
    make_wave('down',33,'Blueshirt',False)
    make_wave('down',34,'Blueshirt',False)
    make_wave('left',40,'Pack',False)
    make_wave('left',41,'Pack',False)
    make_wave('left',42,'Pack',False)
    make_wave('left',43,'Pack',False)
    make_wave('left',44,'Quickling',False)
    make_wave('left',45,'Quickling',False)
    make_wave('left',46,'Quickling',True)
    make_wave('up',30,'Horde',False)
    make_wave('up',32,'Horde',False)
    make_wave('up',34,'Horde',False)
    make_wave('up',36,'Horde',False)

def level10():
    global gameticks
    make_wave('right',30,'Barreling',False)
    make_wave('right',40,'Barreling',False)
    make_wave('up',50,'Quickling',False)
    make_wave('up',60,'Quickling',False)
    make_wave('down',70,'Greenshirt',False)
    make_wave('down',80,'Greenshirt',False)
    make_wave('left',90,'Horde',False)
    make_wave('left',100,'Horde',False)
    make_wave('up',110,'Greenshirt',False)
    make_wave('up',120,'Greenshirt',False)
    make_wave('down',130,'Quickling',False)
    make_wave('down',140,'Quickling',False)
    make_wave('left',150,'Horde',False)
    make_wave('left',160,'Horde',False)
    make_wave('right',170,'Barreling',False)
    make_wave('right',180,'Barreling',True)

def level11():
    global gameticks
    make_wave('right',30,'Horde',False)
    make_wave('right',40,'Horde',False)
    make_wave('right',50,'Horde',False)
    make_wave('right',60,'Horde',False)
    make_wave('right',70,'Horde',False)
    make_wave('right',80,'Greenshirt',False)
    make_wave('right',85,'Greenshirt',False)
    make_wave('right',90,'Greenshirt',False)
    make_wave('right',95,'Greenshirt',False)
    make_wave('right',100,'Greenshirt',False)
    make_wave('left',90,'Quickling',False)
    make_wave('left',95,'Quickling',False)
    make_wave('left',100,'Quickling',False)
    make_wave('up',90,'Quickling',False)
    make_wave('up',95,'Quickling',False)
    make_wave('up',100,'Quickling',False)
    make_wave('down',90,'Quickling',False)
    make_wave('down',95,'Quickling',False)
    make_wave('down',100,'Quickling',True)

def level12():
    global gameticks
    make_wave('right',30,'Greenshirt',False)
    make_wave('right',35,'Greenshirt',False)
    make_wave('right',40,'Greenshirt',False)
    make_wave('right',45,'Greenshirt',False)
    make_wave('right',50,'Greenshirt',False)
    make_wave('down',40,'Greenshirt',False)
    make_wave('down',50,'Greenshirt',False)
    make_wave('down',60,'Greenshirt',False)
    make_wave('down',70,'Greenshirt',False)
    make_wave('down',80,'Greenshirt',False)
    make_wave('left',55,'Greenshirt',False)
    make_wave('left',60,'Greenshirt',False)
    make_wave('left',65,'Greenshirt',False)
    make_wave('up',60,'Greenshirt',False)
    make_wave('up',65,'Greenshirt',False)
    make_wave('up',70,'Greenshirt',False)
    make_wave('down',75,'Greenshirt',False)
    make_wave('down',80,'Greenshirt',False)
    make_wave('down',85,'Greenshirt',True)

def level13():
    global gameticks
    make_wave('right',30,'Horde',False)
    make_wave('down',35,'Horde',False)
    make_wave('up',40,'Horde',False)
    make_wave('left',45,'Horde',False)
    make_wave('down',50,'Barreling',False)
    make_wave('down',40,'Greenshirt',False)
    make_wave('down',50,'Greenshirt',False)
    make_wave('up',60,'Barreling',False)
    make_wave('right',70,'Greenshirt',False)
    make_wave('right',80,'Greenshirt',False)
    make_wave('left',55,'Greenshirt',False)
    make_wave('left',60,'Barreling',False)
    make_wave('left',65,'Barreling',False)
    make_wave('up',60,'Greenshirt',False)
    make_wave('down',65,'Greenshirt',False)
    make_wave('down',70,'Greenshirt',False)
    make_wave('down',75,'Horde',False)
    make_wave('right',80,'Horde',False)
    make_wave('down',85,'Horde',True)

def level14():
    global gameticks
    make_wave('up',30,'Greenshirt',False)
    make_wave('down',31,'Horde',False)
    make_wave('up',32,'Horde',False)
    make_wave('left',33,'Honcho',False)
    make_wave('down',34,'Barreling',False)
    make_wave('right',35,'Greenshirt',False)
    make_wave('down',36,'Greenshirt',False)
    make_wave('up',37,'Barreling',False)
    make_wave('right',38,'Greenshirt',False)
    make_wave('left',39,'Greenshirt',False)
    make_wave('up',40,'Barreling',False)
    make_wave('left',41,'Barreling',False)
    make_wave('down',42,'Honcho',False)
    make_wave('up',43,'Greenshirt',False)
    make_wave('down',44,'Greenshirt',True)


def level15():
    global gameticks
    make_wave('left',30,'Horde',False)
    make_wave('left',32,'Horde',False)
    make_wave('left',34,'Horde',False)
    make_wave('left',36,'Horde',False)
    make_wave('left',38,'Horde',False)
    make_wave('left',40,'Horde',False)
    make_wave('left',42,'Horde',False)
    make_wave('left',44,'Horde',False)
    make_wave('left',46,'Horde',False)
    make_wave('left',48,'Horde',False)
    make_wave('left',50,'Honcho',False)
    make_wave('left',52,'Honcho',False)
    make_wave('left',54,'Honcho',False)
    make_wave('left',56,'Honcho',False)
    make_wave('left',58,'Honcho',False)
    make_wave('left',60,'Barreling',False)
    make_wave('left',62,'Barreling',False)
    make_wave('left',64,'Barreling',False)
    make_wave('left',66,'Barreling',False)
    make_wave('left',68,'Barreling',True)

def level16():
    global gameticks
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)
    make_wave('up',30,'Speedling',False)

    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',False)
    make_wave('right',30,'Speedling',True)

def level17():
    global gameticks
    make_wave('up',30,'Greenshirt',False)
    make_wave('down',34,'Horde',False)
    make_wave('up',40,'Horde',False)
    make_wave('left',47,'Honcho',False)
    make_wave('down',52,'Barreling',False)
    make_wave('right',60,'Greenshirt',False)
    make_wave('down',64,'Greenshirt',False)
    make_wave('up',70,'Barreling',False)
    make_wave('right',72,'Greenshirt',False)
    make_wave('left',80,'Greenshirt',False)
    make_wave('up',96,'Barreling',False)
    make_wave('left',35,'Barreling',False)
    make_wave('down',68,'Honcho',False)
    make_wave('up',37,'Greenshirt',False)
    make_wave('down',92,'Greenshirt',True)
    make_wave('up',58,'Greenshirt',False)
    make_wave('down',40,'Horde',False)
    make_wave('up',85,'Horde',False)
    make_wave('left',43,'Honcho',False)
    make_wave('down',87,'Barreling',False)
    make_wave('right',43,'Greenshirt',False)
    make_wave('down',74,'Greenshirt',False)
    make_wave('up',99,'Barreling',False)
    make_wave('right',59,'Greenshirt',False)
    make_wave('left',39,'Greenshirt',False)
    make_wave('up',107,'Barreling',True)

def level18():
    global gameticks
    make_wave('down',100,'Redshirt',True)

def level19():
    global gameticks
    make_wave('up',30,'Honcho',False)
    make_wave('up',30,'Honcho',False)
    make_wave('up',30,'Honcho',False)
    make_wave('up',30,'Honcho',False)
    make_wave('up',30,'Honcho',False)
    make_wave('down',45,'Honcho',False)
    make_wave('down',45,'Honcho',False)
    make_wave('down',45,'Honcho',False)
    make_wave('down',45,'Honcho',False)
    make_wave('down',45,'Honcho',False)


    make_wave('right',45,'Honcho',False)
    make_wave('right',45,'Honcho',False)
    make_wave('right',45,'Honcho',False)
    make_wave('right',45,'Honcho',False)
    make_wave('right',45,'Honcho',False)
    make_wave('left',30,'Honcho',False)
    make_wave('left',30,'Honcho',False)
    make_wave('left',30,'Honcho',False)
    make_wave('left',30,'Honcho',False)
    make_wave('left',30,'Honcho',True)
    
def level20():
    global gameticks
    make_wave('up',30,'Redshirt',False)
    make_wave('up',32,'Redshirt',False)
    make_wave('up',34,'Redshirt',False)
    make_wave('up',36,'Redshirt',False)
    make_wave('up',38,'Redshirt',False)
    make_wave('up',40,'Redshirt',False)
    make_wave('up',42,'Redshirt',False)
    make_wave('up',44,'Redshirt',False)
    make_wave('up',46,'Redshirt',False)
    make_wave('up',48,'Redshirt',False)
    make_wave('up',50,'Redshirt',False)
    make_wave('up',52,'Redshirt',False)

    make_wave('right',30,'Redshirt',False)
    make_wave('right',32,'Redshirt',False)
    make_wave('right',34,'Redshirt',False)
    make_wave('right',36,'Redshirt',False)
    make_wave('right',38,'Redshirt',False)
    make_wave('right',40,'Redshirt',False)
    make_wave('right',42,'Redshirt',False)
    make_wave('right',44,'Redshirt',False)
    make_wave('right',46,'Redshirt',False)
    make_wave('right',48,'Redshirt',False)
    make_wave('right',50,'Redshirt',False)
    make_wave('right',52,'Redshirt',True)

    make_wave('down',30,'Redshirt',False)
    make_wave('down',32,'Redshirt',False)
    make_wave('down',34,'Redshirt',False)
    make_wave('down',36,'Redshirt',False)
    make_wave('down',38,'Redshirt',False)
    make_wave('down',40,'Redshirt',False)
    make_wave('down',42,'Redshirt',False)
    make_wave('down',44,'Redshirt',False)
    make_wave('down',46,'Redshirt',False)
    make_wave('down',48,'Redshirt',False)
    make_wave('down',50,'Redshirt',False)
    make_wave('down',52,'Redshirt',False)

    make_wave('left',30,'Redshirt',False)
    make_wave('left',32,'Redshirt',False)
    make_wave('left',34,'Redshirt',False)
    make_wave('left',36,'Redshirt',False)
    make_wave('left',38,'Redshirt',False)
    make_wave('left',40,'Redshirt',False)
    make_wave('left',42,'Redshirt',False)
    make_wave('left',44,'Redshirt',False)
    make_wave('left',46,'Redshirt',False)
    make_wave('left',48,'Redshirt',False)
    make_wave('left',50,'Redshirt',False)
    make_wave('left',52,'Redshirt',True)
    

def set_road():
    left_x = 5
    left_y = 250 + random.randint(0,100)
    left_a = math.pi / 2
    right_x = 795
    right_y = 250 + random.randint(0,100)
    right_a = 3 * math.pi / 2
    up_x = 350 + random.randint(0,100)
    up_y = 595
    up_a = 0
    down_x = 350 + random.randint(0,100)
    down_y = 5
    down_a = math.pi

    left_finish = False
    right_finish = False
    up_finish = False
    down_finish = False

    while all_true([left_finish,right_finish,up_finish,down_finish]) == False:
        if all_true([(left_x > 0), (left_x < 800), (left_y > 0), (left_y < 600)]):
            left_mark.append([left_x,left_y,left_a])
            if int(7*random.random()) < 4:
                left_a += math.pi/12 - (math.pi / 6) * random.random()
            left_x += math.sin(left_a) * 10
            left_y -= math.cos(left_a) * 10
        else:
            left_finish = True
        
        if all_true([(right_x > 0), (right_x < 800), (right_y > 0), (right_y < 600)]):
            right_mark.append([right_x,right_y,right_a])
            if int(7*random.random()) < 4:
                right_a += math.pi/12 - (math.pi / 6) * random.random()
            right_x += int(math.sin(right_a) * 10)
            right_y -= int(math.cos(right_a) * 10)
        else:
            right_finish = True

        if all_true([(up_x > 0), (up_x < 800), (up_y > 0), (up_y < 600)]):
            up_mark.append([up_x,up_y,up_a])
            if int(7*random.random()) < 4:
                up_a += math.pi/12 - (math.pi / 6) * random.random()
            up_x += int(math.sin(up_a) * 10)
            up_y -= int(math.cos(up_a) * 10)
        else:
            up_finish = True

        if all_true([(down_x > 0), (down_x < 800), (down_y > 0), (down_y < 600)]):
            down_mark.append([down_x,down_y,down_a])
            if int(7*random.random()) < 4:
                down_a += math.pi/12 - (math.pi / 6) * random.random()
            down_x += int(math.sin(down_a) * 10)
            down_y -= int(math.cos(down_a) * 10)
        else:
            down_finish = True

    for coord in left_mark:
        marker = Roadmark(coord[0],coord[1],(255,150,0))
        left_path.append(marker)
    for coord in right_mark:
        marker = Roadmark(coord[0],coord[1],(200,200,0))
        right_path.append(marker)
    for coord in up_mark:
        marker = Roadmark(coord[0],coord[1],(150,0,150))
        up_path.append(marker)
    for coord in down_mark:
        marker = Roadmark(coord[0],coord[1],(200,0,0))
        down_path.append(marker)
    
def all_true(master):
    for thing in master:
        if thing == False:
            return False
    return True

def selectrange(pos,tower):
    dist =  tower.size #calculates min radius for select
    xdelta = abs(pos[0] - tower.x) 
    ydelta = abs(pos[1] - tower.y)
    hyp = math.sqrt(math.pow(xdelta,2) + math.pow(ydelta,2)) #calculates distance between radius
    if hyp > dist: #compare :^)
        return False
    else:
        return True

def inradius(object1,object2): #checks if two objects overlap
    dist = object1.size + object2.size #calculates min radius for no overlap
    xdelta = abs(object1.x - object2.x) 
    ydelta = abs(object1.y - object2.y)
    hyp = math.sqrt(math.pow(xdelta,2) + math.pow(ydelta,2)) #calculates distance between radius
    if hyp > dist: #compare :^)
        return False
    else:
        return True

def inrange(tower,thing):
    dist = tower.frange + thing.size #calculates farthest distance to be shot
    xdelta = abs(tower.x - thing.x) 
    ydelta = abs(tower.y - thing.y)
    hyp = math.sqrt(math.pow(xdelta,2) + math.pow(ydelta,2)) #calculates distance between radius
    if hyp > dist: #compare :^)
        return False
    else:
        return True

def check_overlap(object1, master): #checks if object1 overlap with everything in master
    for alist in master:
        for thing in alist:
            if inradius(object1, thing):
                return False
    return True

def draw_list(stuff): #draws everything in stuff
    for items in stuff:
        items.display()

def draw_range():
    for tower in tower1_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           60,
                           2)
    for tower in tower1u1_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           60,
                           2)
    for tower in tower1u2_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           45,
                           2)
    for tower in tower1u3_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           120,
                           2)
    for tower in tower2_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           90,
                           2)
    for tower in tower2u1_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           90,
                           2)
    for tower in tower2u2_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           60,
                           2)
    for tower in tower2u3_list:
        pygame.draw.circle(screen,
                           (255,0,0),
                           (tower.x,tower.y),
                           150,
                           2)
    for tower in tower3_list:
        pygame.draw.circle(screen,
                           (0,255,0),
                           (tower.x,tower.y),
                           60,
                           2)
    for tower in tower3u1_list:
        pygame.draw.circle(screen,
                           (0,255,0),
                           (tower.x,tower.y),
                           80,
                           2)
    for tower in tower3u2_list:
        pygame.draw.circle(screen,
                           (0,255,0),
                           (tower.x,tower.y),
                           50,
                           2)
    for tower in tower3u3_list:
        pygame.draw.circle(screen,
                           (0,255,0),
                           (tower.x,tower.y),
                           125,
                           2)

def draw(cursor_type): #heavy duty drawing function
    global showrange
    screen.fill(background_colour)
    draw_list(left_path)
    draw_list(right_path)
    draw_list(up_path)
    draw_list(down_path)
    draw_list(tower1_list)
    draw_list(tower1u1_list)
    draw_list(tower1u2_list)
    draw_list(tower1u3_list)
    draw_list(tower2_list)
    draw_list(tower2u1_list)
    draw_list(tower2u2_list)
    draw_list(tower2u3_list)
    draw_list(tower3_list)
    draw_list(tower3u1_list)
    draw_list(tower3u2_list)
    draw_list(tower3u3_list)
    draw_list(enemy1_list)
    draw_list(enemy1a_list)
    draw_list(enemy1b_list)
    draw_list(enemy2_list)
    draw_list(enemy2a_list)
    draw_list(enemy2b_list)
    draw_list(enemy3_list)
    draw_list(enemy3a_list)
    draw_list(enemy3b_list)
    draw_list(enemy4_list)
    if show_range:
        draw_range()
    pos = pygame.mouse.get_pos()
    test = GameCursor(pos[0],pos[1],'None')
    if cursor_type == 1:
        test = GameCursor(pos[0],pos[1],'Tower1')
    elif cursor_type == 2:
        test = GameCursor(pos[0],pos[1],'Tower2')
    elif cursor_type == 3:
        test = GameCursor(pos[0],pos[1],'Tower3')
    test.display()
   

def main(): #loops constantly for updates and stuff
    global gameticks
    global grace_period
    global show_range
    global q_upgrade
    global w_upgrade
    global e_upgrade
    global gold
    global playerhp
    global gameover
    global winner
    #global spawn_over
    cursor_type = 0
    while True:
        '''
        print (gameticks)
        print (grace_period)
        print (spawn_over)
        '''
        place_down = False
        removing = False
        q_upgrade = False
        w_upgrade = False
        e_upgrade = False
        for event in pygame.event.get():
            if event.type == QUIT: #close the window if you click X
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: #if a key is pressed
                if event.key == K_1:
                    cursor_type = 0
                elif event.key == K_2:
                    cursor_type = 1
                elif event.key == K_3:
                    cursor_type = 2
                elif event.key == K_4:
                    cursor_type = 3
                elif event.key == K_r:
                    if len(selected) > 0:
                        removing = True
                elif event.key == K_q:
                    if len(selected) > 0:
                        q_upgrade = True
                elif event.key == K_w:
                    if len(selected) > 0:
                        w_upgrade = True
                elif event.key == K_e:
                    if len(selected) > 0:
                        e_upgrade = True
                elif event.key == K_SPACE:
                    show_range = not show_range
                elif event.key == K_y:
                    if gameover or winner:
                        reset()
                        set_road()
                elif event.key == K_n:
                    if gameover or winner:
                        pygame.quit()
                        sys.exit()
            if event.type == MOUSEBUTTONUP: #if mouseclick is released:
                if event.button == 1:
                    place_down = True

        clock.tick(30)
        pygame.mouse.set_visible(True)

        if playerhp <= 0:
            gameover = True
        if winner:
            pass
        elif gameover:
            pass
        else:
            if grace_period:
                if removing:
                    remove_tower(selected[0])
                if q_upgrade:
                #print(len(selected))
                #print_tower(selected[0])
                    upgradeQ(selected[0])
                if w_upgrade:
                    upgradeW(selected[0])
                if e_upgrade:
                    upgradeE(selected[0])
                if place_down:
                    pos = pygame.mouse.get_pos()
                    if cursor_type == 0:
                        if len(selected) > 0:
                            selected.remove(selected[0])
                        for tower in tower1_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower1u1_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower1u2_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower1u3_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower2_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower2u1_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower2u2_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                        for tower in tower2u3_list:
                            if selectrange(pos,tower):
                                selected.append(tower)
                                print_tower(tower)
                                break
                    if cursor_type == 1:
                        tower1 = Tower1(pos[0],pos[1])
                        if can_purchase(tower1.cost):
                            if check_overlap(tower1,[tower1_list,tower2_list,tower3_list]): #only execute if no overlap confirmed
                                tower1_list.append(tower1)
                                purchase(tower1.cost)
                        else:
                            purchase(tower1.cost)
                    if cursor_type == 2:
                        tower2 = Tower2(pos[0],pos[1])
                        if can_purchase(tower2.cost):
                            if check_overlap(tower2,[tower1_list,tower2_list,tower3_list]):
                                tower2_list.append(tower2)
                                purchase(tower2.cost)
                        else:
                            purchase(tower2.cost)
                    if cursor_type == 3:
                        tower3 = Tower3(pos[0],pos[1])
                        if can_purchase(tower3.cost):
                            if check_overlap(tower3,[tower1_list,tower2_list,tower3_list]):
                                tower3_list.append(tower3)
                                purchase(tower3.cost)
                        else:
                            purchase(tower3.cost)
                
                    
        draw(cursor_type)
        towerAI()
        enemyAI()
        pygame.display.flip()
        if not gameover:
            levels()
            gameticks += 1
        

if __name__ == '__main__':
    set_road()
    main()



