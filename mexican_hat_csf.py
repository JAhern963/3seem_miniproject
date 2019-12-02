# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:07:28 2019

Fucnction to create a normalised coupling strength fucntion with mexican hat
form.

Inputs:
    Ce,We: excitory contantants
    Ci,Wi: inhibitory constants
    d0:    0<d<d0 is range of excitory coupling
    dm:    maximum coulping distance 
Theres more parametrs that can be passed as inputs, such as di and de

Output:
    Wn: normalised csf
    possible plot of Wn

@author: Jake
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mexican_hat_csf(Ce,We,Ci,Wi,d0,dm,plot):
    
    de = 14
    di = 42
    
    xd = [i for i in range(-dm,dm+1)]
    yd = xd
    Nw = len(xd) 
    ddx,ddy = np.meshgrid(xd,yd)
    d = np.sqrt(ddx**2 + ddy**2)
    
    excitory_index = d<d0
    inhibitory_index = d>=d0
    zero_coupling_index = d>dm
    
    #coupling stenght function
    W = Ce*np.exp(-d**2/de) - Ci*np.exp(-d**2/di)
    W[d>dm]=0
    
    #normalised CSF - so that E/I distances not changed
    Wn = np.zeros((Nw,Nw))
    WnE = sum(W[excitory_index])
    WnI = sum(W[inhibitory_index])
    
    Wn[excitory_index] = We * W[excitory_index] / WnE
    Wn[inhibitory_index] = Wi * W[inhibitory_index] / WnI
    Wn[zero_coupling_index] = 0
    
    if plot == 1:
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        ax.plot_surface(ddx,ddy,Wn,cmap='PiYG')
        #ax.view_init(90,0)
        plt.xlabel('x distance')
        plt.ylabel('y distance')
        plt.title('Strength and ploarity of neuron coulping')
        
        
    return Wn
        



