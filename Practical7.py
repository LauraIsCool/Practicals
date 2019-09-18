#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:29:39 2019

@author: laurapemberton


Practical 7: Communicating


"""
import csv
import operator
import matplotlib.pyplot
import agentframework7
import random

""" method to work out the distance between two given agents. """
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


"""section of code copied from lecture notes that imports the data from the 
in.txt file and prints it into the console.

The append() method adds an item to the end of a list.

parsed_line - allows you to read a text file line by line. 
"""            
f = open("in.txt") #open the labeled file and name it f. 
environment = [] #creates new environment list 
for line in f: #for every line in the file 
    parsed_line = str.split(line, ",") #this separates each line as a string by the comma
    data_line = [] #this creates a new list for the individual items in the line
    for word in parsed_line: #this cycles through each word in the identified line
        data_line.append(float(word)) #this appends each word as a float        
    environment.append(data_line) #The fata line (that is now a float) is appended to the environment list. 
#print(data)
f.close() 

num_of_agents = 10
num_of_iterations = 10
agents = [] # declare agent as a list
neighbourhood = 20


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework7.Agent(environment, agents))

"""CODE TO PROVE IMPACT OF SHUFFLE
print('before')
for agent in agents:
    print(agent.x)
random.shuffle(agents)
print('after')
for agent in agents:
    print(agent.x)
"""

# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        #print(agents[i].x)

""" Calling the eat method to 
"""        
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment) 
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='white')
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        #print(distance)
