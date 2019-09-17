#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:11:11 2019

@author: laurapemberton
"""

""" 
Practical 2 Assignment: Code shrinking 1

This code uses the array function to create x and y coordinates for both agents
the code then increments each of the integers within the array as the code from 
practical 1 did. 

Calculate distance between both agents 
import math
distance = math.sqrt((agents[1][1] - agents[0][1])**2 
                     + (agents[1][0] - agents[0][0])**2)
print ("distance between coordinates:", round(distance))
 
"""

import random #import random module
import array 
import operator
import matplotlib.pyplot

num_of_agents = 10 #controls the num of agents in array
num_of_iterations = 100 

agents = []

random_numberY_Axis = random.random() 
random_numberX_Axis = random.random() 


for i in range(num_of_agents): #i is num of times loop is run.
    agents.append([random.randint(0,99), random.randint(0,99)])

print("random agent coordinates 0:", agents[0])
print("random agent coordinates 1:", agents[1])

""" 
this for loop takes all of the agents in the array and cycles through the loop
each time moveing each of the agents twice.
"""
for agent in range(num_of_iterations):
    for i in range(num_of_agents): 

        if random_numberY_Axis < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
    
        if random_numberX_Axis < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
   
#Output
print ("coordinates 0 after move: Random y0 = ", agents[0][0], 
       "Random x0 = ", agents[0][1])

print ("coordiates 1 after move: Random y1 = ", agents[1][0], 
       "Random x1 = ", agents[1][1])


""" Working with functions"""
print ("largest x value:", max(agents, key=operator.itemgetter(1)))

""" Graphical representation of plots"""
matplotlib.pyplot.ylim(0,100)
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.scatter(agents[0][1], agents[0][0])
matplotlib.pyplot.scatter(agents[1][1], agents[1][0])
m = max(agents, key=operator.itemgetter(1)) 
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()