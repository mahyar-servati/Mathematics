# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:14:51 2024

@author: Mahyar Servati
"""

import numpy as np
import matplotlib.pyplot as plt
import os

image_folder = 'images'
video_name = 'video.avi'

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

loop = 20
nlist = [[0,0], [1,0]]
n=1

def plot(fraclist, n, image_folder):
    fraclist = np.array(fraclist)
    fig= plt.subplots(figsize=(10, 10), frameon=False)
    plt.rcParams["font.family"] = "DejaVu Serif"
    plt.rcParams["font.serif"] = "Times New Roman"
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['font.size'] = 16
    plt.axis('equal')
    plt.plot(fraclist[:,0], fraclist[:,1])
    # xlimmin = -5
    # xlimmax = 5
    # ylimmin = -5
    # ylimmax = 5
    # if max(abs(np.array(nlist)[:,0])) < xlimmax:
    #     if max(abs(np.array(nlist)[:,1])) < ylimmax:
    #         plt.xlim(xlimmin, xlimmax)
    #         plt.ylim(ylimmin, ylimmax)
    # else:
    plt.xlim(max(abs(np.array(nlist)[:,0]))*2, -1*max(abs(np.array(nlist)[:,0]))*2)
    plt.ylim(max(abs(np.array(nlist)[:,1]))*2, -1*max(abs(np.array(nlist)[:,1]))*2)
    
    # plt.xlim(n*2, -1*n*2)
    # plt.ylim(n*2, -1*n*2)
    plt.axis('off')
    plt.savefig(f'{image_folder}/img{n : 03d}.png', dpi=300, bbox_inches='tight')
    plt.show()

    
def rotate(p, origin=(0, 0), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    origin = np.atleast_2d(origin)
    points = np.atleast_2d(p)
    rlist = np.squeeze((R @ (points.T-origin.T) + origin.T).T)
    return [list(i) for i in rlist][:-1][::-1]


for _ in range(loop):
    nlist.extend(rotate(nlist, nlist[-1], degrees=90))
    plot(nlist, n, image_folder)
    print(len(nlist))
    n+=1



import moviepy.video.io.ImageSequenceClip
from moviepy import *
import cv2
import glob
fps=5
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
clip.write_videofile(f'{image_folder}/fractal.mp4')



 
# img_array = []
# for filename in glob.glob('images/*.png'):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)
 
 
# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()

