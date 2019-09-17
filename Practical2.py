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
 

"""

import random #import random module
import array 
import operator
import matplotlib.pyplot

agents = []

random_numberY_Axis = random.random() 
random_numberX_Axis = random.random() 


y1 = random.randint(0,99)
x1 = random.randint(0,99)


agents.append([random.randint(0,99), random.randint(0,99)])

print("random agent coordinates 0:", agents[0])

#First Iteration
if random_numberY_Axis < 0.5: 
    agents[0][0] += 1
else: #this else statement states that if the random number is more than 0.5 
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


"""Second Agent"""

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

import math


distance = math.sqrt((agents[1][1] - agents[0][1])**2 
                     + (agents[1][0] - agents[0][0])**2)
print ("distance between coordinates:")

print (round(distance)) 


""" Working with functions"""
print ("largest x value:", max(agents, key=operator.itemgetter(1)))

""" external library used to plot data in graphs"""
matplotlib.pyplot.ylim(0,100)
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.scatter(agents[0][1], agents[0][0])
matplotlib.pyplot.scatter(agents[1][1], agents[1][0])
m = max(agents, key=operator.itemgetter(1)) 
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()