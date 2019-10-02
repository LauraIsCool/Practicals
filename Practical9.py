#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:29:39 2019

@author: laurapemberton


Practical 9: GUI


"""
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework9
import random
import matplotlib.animation



# =============================================================================
# calculate distance between agents
# =============================================================================
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# =============================================================================
# #read text file and create environment          
# =============================================================================
f = open("in.txt")
environment = []  
for line in f:  
    parsed_line = str.split(line, ",") 
    data_line = [] 
    for word in parsed_line: 
        data_line.append(float(word))      
    environment.append(data_line)
#print(data)
f.close() 

# =============================================================================
# variables
# =============================================================================
num_of_agents = 20
num_of_iterations = 50
agents = [] # declare agent as a list
neighbourhood = 20

# =============================================================================
# create figure animation
# =============================================================================
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# =============================================================================
# Make the agents.
# Range function used to cycle through the number of agents. 
# =============================================================================
for i in range(num_of_agents):
    agents.append(agentframework9.Agent(environment, agents))
    
carry_on = True

def update(frame_number):
    fig.clear()
    global carry_on     
        
    # =========================================================================
    # Move the agents.
    # =========================================================================
    for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            #print(agents[i].x)
                                 
    # =========================================================================
    # Call eat method   
    # =========================================================================
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    # =========================================================================
    # #Create animated graphic
    # =========================================================================
    matplotlib.pyplot.xlim(0,300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment) 
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='white')
        #print("agent ", agents[i], "coordinates: ", agents[i].x, agents[i].y)
        
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a<num_of_iterations) & (carry_on):
        yield a
        a = a + 1
        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                                                   frames=gen_function, 
def pause():
    programPause = input()                                                   repeat= False, interval=1)
    #canvas.show()
    canvas.draw()
    
    

tkinter.mainloop()
                                                


        
        