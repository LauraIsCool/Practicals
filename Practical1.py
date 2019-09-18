#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:11:11 2019

@author: laurapemberton
"""

""" 
Practical 1 Assignment: Agent Based Modelling
This program creates two agent coordinates and randomly assignes the x and y value 
of an integer between 1 and 100.

Next the program generates another random number that is used to determine how the 
x and y coordinates for each agent will move. 

If the random number generated is less than 0.5 then the coordinate will move
either up the y axis 1 point or right across the x axis one point. 

Finally the programme takes the newly calculated coordinates and calculates the 
distance between them using the square root function. 

The programme then outputs the coordinates for both agents and the distance 
between them.
"""

import random #import random module
import math

""" Random number axis variables use the random function to get a random number"""
random_numberY_Axis = random.random() 
random_numberX_Axis = random.random() 

""" x and y coordinates use the random function to get integer values between
0 and 99"""
y0 = random.randint(0,99)
x0 = random.randint(0,99)

"""this if function states if the random number generated is less than 0.5 
move y0 up the y axis one place. If not (and the random number is more than 0.5)
then move the coordinate down one place. 
A second if statement does the same for the x coordinate to move it one place
either left or right along the access.
This process is then repeated again so the coordinate moves twice along both 
axises."""
#First Iteration
if random_numberY_Axis < 0.5: 
    y0 = y0 + 1
else: #this else statement states that if the random number is more than 0.5 
    y0 = y0 - 1 
    

if random_numberX_Axis < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

#Second Iteration
if random_numberY_Axis < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    


if random_numberX_Axis < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
    
#Output for zero agent details
print ("Zero agent coordinates:")
print ("Random y0 = ", y0)
print ("Random x0 = ", x0)


"""Second Agent - Second agent must also move 2 places."""
random_numberY_Axis = random.random() 
random_numberX_Axis = random.random()


y1 = random.randint(0,99)
x1 = random.randint(0,99)


#First Iteration
if random_numberY_Axis < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    

if random_numberX_Axis < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

#Second Iteration
if random_numberY_Axis < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    

if random_numberX_Axis < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
    
    
#Output for first agent details
print ("First agent coordinates:")
print ("Random y1 = ", y1)
print ("Random x1 = ", x1)


""" Calculate distance between both agents:
Distance uses the sqrt function within the math import to calculate the 
distance between the points. """
distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

#Output
print ("distance between coordinates:")
print (round(distance)) 