#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:24:09 2019

@author: laurapemberton
"""
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0]  = (agents[i][0] + 1) % 99 
        else:
            agents[i][0]  = (agents[i][0] - 1) % 99
        
        if random.random() < 0.5:
            agents[i][1]  = (agents[i][1] + 1) % 99 
        else:
            agents[i][1]  = (agents[i][1] - 1) % 99 
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)



matplotlib.pyplot.show()














