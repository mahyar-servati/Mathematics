#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:56:27 2024

@author: amdm-i5
"""
import numpy as np
import matplotlib.pyplot as plt
import os

image_folder = 'images'
video_name = 'video'

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

loop = 360


def plot2D(vec1, vec2, vec3, n, image_folder):
    des1 = np.array(vec1)[-1]
    des2 = des1 + np.array(vec2)[-1]
    des3 = des1 + np.array(vec3)[-1]
    road1 = np.array(vec1) + np.array(vec2)
    road2 = np.array(vec1) + np.array(vec3)

    fig= plt.subplots(figsize=(10, 10), frameon=False)
    plt.rcParams["font.family"] = "DejaVu Serif"
    plt.rcParams["font.serif"] = "Times New Roman"
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['font.size'] = 16
    plt.axis('equal')
    plt.plot([0, des1[0]], [0, des1[1]], c='k')
    plt.scatter(des1[0], des1[1], c='k', s=20)
    plt.plot([des1[0], des2[0]], [des1[1], des2[1]], c='k')
    plt.scatter(des2[0], des2[1], c='k', s=20)
    plt.plot([des1[0], des3[0]], [des1[1], des3[1]], c='k')
    plt.scatter(des3[0], des3[1], c='k', s=20)
    plt.plot(road1[:,0], road1[:,1], c='k')
    plt.plot(road2[:,0], road2[:,1], c='k')
    plt.axis('off')
    plt.savefig(f'{image_folder}/img{n : 04d}.png', dpi=300, bbox_inches='tight')
    plt.show()

    
def rotate(vec1, degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    points = np.atleast_2d(vec1)
    rlist = np.squeeze(R @ points.T)
    return list(rlist)


    
vec1 = [[5, 0]]
vec2 = [[0, 1]]
vec3 = [[0, -1]]

deg1 = 2
deg2 = 20 
deg3 = 20

shape1 = [np.array(vec1) + np.array(vec2)]
shape2 = [np.array(vec1) + np.array(vec3)]

plot2D(vec1, vec2, vec3, 0, image_folder)

for i in range(loop//2):
    vec1.append(rotate(vec1[-1], degrees=deg1))
    vec2.append(rotate(vec2[-1], degrees=deg2))
    vec3.append(rotate(vec3[-1], degrees=deg3))
    plot2D(vec1, vec2, vec3, i+1, image_folder)
    shape1.append(np.array(vec1) + np.array(vec2))
    shape2.append(np.array(vec1) + np.array(vec3))

import moviepy.video.io.ImageSequenceClip
from moviepy import *
import cv2
import glob
fps=10
image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]

img_array = []
for filename in image_files:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    resized = cv2.resize(img, dsize=(1000,1000), interpolation=cv2.INTER_LINEAR)
    img_array.append(resized)
    
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(img_array, fps=fps)
clip.write_videofile(f'{video_name}.mp4')