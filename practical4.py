#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:45:14 2019

@author: laurapemberton

Practical 4: Functions/ Building Tools

Base of this code is copied from practical instructions. 
The code creates agents consisting of random integers. These are then moved 
a given number of times. 

The code works out the distance between all of the variables. Doing this efficiently 
by incrementing each time which agents have been compared to ensure there is no
repitition. 
"""

import random
import operator
import matplotlib.pyplot
import time

#this version of the code times how long it takes to be processed.
start = time.process_time()

"""distance_between method calculates the distance between any given agents, and
returns the answer that can be used further in the programme. """
def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0]) ** 2) 
    + ((agents_row_a[1] - agents_row_b[1])**2)) ** 0.5
    return answer

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


#Graphical representation of the data in the graph. 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

"""function:
for loop cycles through all of the agents in range. then for each time it increases
the agent by one (to avoid duplication). This loop then calculates the distance
between the two agents. Finally this loop prints the distance between the two."""

for i in range(num_of_agents):
    for j in range(i + 1, num_of_agents):
        distance = distance_between(agents[i], agents[j])
        print ("distance between agent {} and agent {}: {}".format(i, j, round(distance)))

"""
Timing the running of the code
"""
end = time.process_time()
print ("time completed in: "+ str(round(end-start, 3)))



