# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:50:13 2024

@author: teodo
"""

import pygame
import math
import time
import math
import random
#math.exp(10)


# pygame setup
screenie =(1280, 720)
pygame.init()
screen = pygame.display.set_mode(screenie)
clock = pygame.time.Clock()
running = True


def f(x):
    return(-(11/9)*x + 20/9)

class drop:
    drops=[]
    def __init__(self,pos,radius,Speed):
        self.pos=pos
        self.finalradius=radius
        self.radius=0
        self.speed=Speed
        self.maxWidth=15
        
        #self.dt=dt
        #info=(self.pos,self.finalradius,self.radius,self.speed)
        self.drops.append(self)
        
    def expand(self):
        if self.radius < self.finalradius:
            self.radius += self.speed *dt
            #print(self.radius)
        else:
            #pass
            self.drops.remove(self)
    
    def draw(self):
        self.width=self.maxWidth * (((1)*abs(self.finalradius - self.radius)/self.finalradius))
        #print(self.width)
        self.width=int(self.width)
        if self.width == 0:
            self.width = -1
        pygame.draw.circle(screen,"black",self.pos,self.radius,self.width)


global dt
dt=0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                holder=[0,0]
                holder[0]=event.pos[0]
                holder[1]=event.pos[1]
                #print(holder)
                drop(holder,400,20)
                #print(drop.drops)
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    print(len(drop.drops))
    x=random.randint(0,screenie[0])
    y=random.randint(0,screenie[1])
    drop((x,y),100,20)
    
    for each in drop.drops:
        each.expand()
        each.draw()
        
    #flip() the display to put your work on screen
    pygame.display.flip()

    #clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()