#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:11:11 2019

@author: laurapemberton
"""

""" 
Practical 2 Assignment: Code shrinking 1

This code uses the array function to create x and y coordinates for two agents
(using the random function) the code then randomly changes the location of the 
two agents by two places again. 

The programme also works out the distance between the two agents. The agent 
with the largest x coordinate is then displayed in red. 
 

"""

import random 
import array 
import operator
import matplotlib.pyplot
import math

#create a list called agents
agents = []

random_numberY_Axis = random.random() 
random_numberX_Axis = random.random() 

#append function is used here to add two random integers to the list. 
agents.append([random.randint(0,99), random.randint(0,99)])

#statement to print the zero set of coordinates. Just calls agent 0.
print("random agent coordinates 0:", agents[0])

#First Iteration
if random_numberY_Axis < 0.5: 
    agents[0][0] += 1
else: 
    agents[0][0] -= 1 

if random_numberX_Axis < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

#Second Iteration
if random_numberY_Axis < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1 

if random_numberX_Axis < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
    
#Output
print ("first agent coordinates:")
print ("Random y0 = ", agents[0][0])
print ("Random x0 = ", agents[0][1])


"""Second Agent:
append function adds additional items to the list. This is then called the first
agent """
agents.append([random.randint(0,99), random.randint(0,99)])

print("random agent coordinates 0:", agents[1])

#First Iteration
if random_numberY_Axis < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random_numberX_Axis < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

#Second Iteration
if random_numberY_Axis < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random_numberX_Axis < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
#Output
print ("second agent coordinates:")
print ("Random y1 = ", agents[1][0])
print ("Random x1 = ", agents[1][1])


""" Calculate distance between both agents """

distance = math.sqrt((agents[1][1] - agents[0][1])**2 
                     + (agents[1][0] - agents[0][0])**2)
print ("distance between coordinates:")

#Show the ditance as a rounded number. 
print (round(distance)) 


""" Working with functions"""
print ("largest x value:", max(agents, key=operator.itemgetter(1)))

""" external library used to plot data in graphs.
x and y axis range between 0 and 100. the agents are then placed within the graph
in a scatter form. The agent with the maximum x axis is coloured in red."""
matplotlib.pyplot.ylim(0,100)
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.scatter(agents[0][1], agents[0][0])
matplotlib.pyplot.scatter(agents[1][1], agents[1][0])
m = max(agents, key=operator.itemgetter(1)) 
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()