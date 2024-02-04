# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:38:49 2023

@author: Mahyar Servati
"""

import numpy as np
import matplotlib.pyplot as plt
import random

#inter polygon degree
polygon_num=5
iterate = 1000000

def polygon(first_vertex, vertex_num):
    theta = 360//vertex_num
    vertex=[]
    theta = np.radians(theta)
    for i in range(vertex_num):
        rot_mat = np.array([[np.cos(i*theta), -np.sin(i*theta)], [np.sin(i*theta), np.cos(i*theta)]])
        vertex.append(np.dot(first_vertex, rot_mat))
    return np.array(vertex)

vertex = polygon(np.array([10,0]), polygon_num)
# points = [[vertex[1,0], vertex[1,1]]]
points = [[0.0, 0.0]]

for _ in range(iterate):
    rand_vertex = random.choice(vertex)
    points.append(((rand_vertex-np.array(points[-1]))*0.618)+np.array(points[-1]))
    
# for _ in range(iterate):
#     rand_vertex = random.choice(vertex)
#     points.append((rand_vertex-np.array(points[-1]))+(np.array(points[-1])*0.618))
    
# for _ in range(iterate):
#     rand_vertex = random.choice(vertex)
#     points.append((rand_vertex+np.array(points[-1]))/2)
        
points = np.array(points)    

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.scatter(vertex[:,0], vertex[:,1], c='red', s=1)
ax.scatter(points[:,0], points[:,1], c='blue', s=0.0001)
ax.set_xticks([])
ax.set_yticks([])
fig.savefig(f"Fractal_pattern_{polygon_num}.png", bbox_inches = 'tight', dpi=300)


