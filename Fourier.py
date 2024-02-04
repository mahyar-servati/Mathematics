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
video_name = 'Fourier'

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

loop = 360

def plot(vec1, vec2, vec3, vec4, n, image_folder):
    des1 = np.array(vec1)[-1]
    des2 = des1 + np.array(vec2)[-1]
    des3 = des2 + np.array(vec3)[-1]
    des4 = des3 + np.array(vec4)[-1]
    road = np.array(vec1) + np.array(vec2) + np.array(vec3) + np.array(vec4)
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
    plt.plot([des2[0], des3[0]], [des2[1], des3[1]], c='k')
    plt.scatter(des3[0], des3[1], c='k', s=20)
    plt.plot([des3[0], des4[0]], [des3[1], des4[1]], c='k')
    plt.scatter(des4[0], des4[1], c='k', s=20)
    plt.plot(road[:,0], road[:,1], c='k')
    # plt.axis('off')
    # plt.savefig(f'{image_folder}/img{n : 04d}.png', dpi=300, bbox_inches='tight')
    plt.show()

    
def rotate(vec1, degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    points = np.atleast_2d(vec1)
    rlist = np.squeeze(R @ points.T)
    return list(rlist)#[:-1][::-1]


vec1 = [[1, 0]]
vec2 = [[1, 0]]
vec3 = [[1, 0]]
vec4 = [[1, 0]]

deg1 = 5
deg2 = -3 
deg3 = 5
deg4 = -3

shape = [np.array(vec1) + np.array(vec2) + np.array(vec3) + np.array(vec4)]

for i in range(loop):
    vec1.append(rotate(vec1[-1], degrees=deg1))
    vec2.append(rotate(vec2[-1], degrees=deg2))
    vec3.append(rotate(vec3[-1], degrees=deg3))
    vec4.append(rotate(vec4[-1], degrees=deg4))
    plot(vec1, vec2, vec3, vec4, i+1, image_folder)
    shape.append(np.array(vec1) + np.array(vec2) + np.array(vec3) + np.array(vec4))

# import moviepy.video.io.ImageSequenceClip
# from moviepy import *
# import cv2
# import glob
# fps=10
# image_files = [os.path.join(image_folder,img)
#                for img in os.listdir(image_folder)
#                if img.endswith(".png")]

# img_array = []
# for filename in image_files:
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     resized = cv2.resize(img, dsize=(1000,1000), interpolation=cv2.INTER_LINEAR)
#     img_array.append(resized)
    
# clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(img_array, fps=fps)
# clip.write_videofile(f'{video_name}.mp4')