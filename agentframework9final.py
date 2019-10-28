#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:40:22 2019

@author: laurapemberton

Practical 9: Agent class 

This class is representative of the agent. The module creates the agent and 
then values are assigned to the agent within this class. 
All agents are created with a random x and y variable. 

    
"""

import random

class Agent():

    def __init__(self, environment, list_agents, y, x): #sheep_in_hole
        self.x = x
        self.y = y
        self.environment = environment
        self.store = 0
        self.agents = list_agents

    #move function randomly moves the agents around the model. each agent moves 
    # two times in both y and x direction. 
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
    
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
            
           
    #function that enables the agents to consume part of the environment. updates
    # the store to show how much of the environment the agent has eaten. 
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -=10
            self.store += 10

    #share_with_neighbour function is created that allows the agents to communicate
    # therefore each agent shares with eachother the distance between. 
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                average = sum/2
                self.store = average
                agent.store = average
            
                #print("sharing " + str(dist) + " " + str(ave))
        #print(neighbourhood)
        #print statement to test that share with neighbour function works. 
    
    # function to calculate the distance between 2 given agents. 
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    #  When an agent has a store greater than 100, the agent throws up their  
    # store in current location
    def throwup(self):
        if self.store >= 100:            
            self.environment[self.y][self.x] +=100
            self.store = self.store-100  
            
""" END OF CLASS """            
# =============================================================================
# Code written in attempt to get agents to "fall" in a hole thats in the middle
# of the grid. However could not get this to work. Could not work out how to 
# take sheep in hole list from agents list within main program document. 

        
# =============================================================================

#     def fall_in_hole(self, agents):
#         sheep_in_hole = []
#         if self.x > 145 and self.x < 156 and self.y > 145 and self.y < 156:
#              sheep_in_hole.append(self.x, self.y)
#              agents.remove(sheep_in_hole)
#         return agents
# =============================================================================

        
    
        