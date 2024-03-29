#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:40:22 2019

@author: laurapemberton

Practical 9: Agent class 

This class is representative of the agent. The module creates the agent and 
then values are assigned to the agent within this class. 
All agents are created with a random x and y variable. 

A function (move) is created to move the agents twice for both the x and y value 
randomly. 

A function (eat) is used 

A function (share with neighbours)

A function (distance_between) returns the value of the distance between two 
given agents. 

    def distance_between(self, agent):
        return(((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
"""

import random

class Agent():

    
    def __init__(self, environment, list_agents):
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
        self.environment = environment
        self.store = 0
        self.agents = list_agents


    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
    
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300   
    
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -=10
            self.store += 10

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
            
                #print("sharing " + str(dist) + " " + str(ave))
        #print(neighbourhood)
        
    def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5            