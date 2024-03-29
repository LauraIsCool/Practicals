#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:29:39 2019

@author: laurapemberton


Practical 9: GUI

Sections of code taken from: https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/


"""
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import agentframework9edited
import random
import matplotlib.animation
import matplotlib.backends

import requests
import bs4


# =============================================================================
# declare all variables
# =============================================================================
num_of_agents = 100
num_of_iterations = 50
neighbourhood = 20

# =============================================================================
# Create lists for environment and agents.
# =============================================================================
agents = []  
environment = []

# =============================================================================
# Code here used to scrape data off the internet 
# =============================================================================

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

# =============================================================================
# #read text file and create environment          
# =============================================================================
f = open("in.txt")
for line in f:  
    parsed_line = str.split(line, ",") 
    data_line = [] 
    for word in parsed_line: 
        data_line.append(float(word))      
    environment.append(data_line)
#print(data) 
#Test print statement. 
f.close() 


# =============================================================================
# create figure animation
# =============================================================================
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                                                   frames=gen_function, 
                                                   repeat= False) 

    
    #canvas.show()
    canvas.draw()

# =============================================================================
# Make the agents.
# =============================================================================
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework9edited.Agent(environment, agents, y, x)) 

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
            #Print statement used as test case to confirm agents have moved. 
                                 
    # =========================================================================
    # Call methods that do stuff to agents.    
    # =========================================================================
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            agents[i].throwup()
            #agents[i].sheep_in_hole()

            #agents[i].sheep_in_hole(agent)

    # =========================================================================
    # #Create animated graphic
    # =========================================================================
    matplotlib.pyplot.xlim(0,300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment) 
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='white')
        #print("agent ", agents[i], "coordinates: ", agents[i].x, agents[i].y)
        #print statement shows coordinates for generated agents. 

#supplied generator function to frame number.           
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a<num_of_iterations) & (carry_on):
        yield a
        a = a + 1
        
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# =============================================================================
# #Code to make menu
# =============================================================================
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label='Model', menu=model_menu)
model_menu.add_command(label="Run model", command = run)


tkinter.mainloop()



""" END OF PROGRAM. """
"""

aTTEMPT TO WRITE FUNCTION THAT WOULD ENABLE THE PROGRAM TO BE PAUSED BY THE USER. 
could not find a function within python library i could understand to implement
this. 
def pause():
    programPause = input()


attempt to write code that could pause the program. Could not find function
in library that would do this
model_menu.add_command(label="Pause model", command = pause)   

import time 
start = time.process_time()
end = time.process_time()
print ("time completed in: "+ str(round(end-start, 3)))                                       

"""
        
        