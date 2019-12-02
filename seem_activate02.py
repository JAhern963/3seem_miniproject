"""
Created on Tue Nov 12 21:59:39 2019

@author: Jake

The '...02' is the first version to use a grid with periodic boundary
conditions, which maps the activity onto a torus.

"""

import numpy as np
from torus_matrix import torus_matrix
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import time

start_time = time.time()

plt.close('all')

#parameters and coupling strength function 
N = 30
Nt = 20
pg = 0.2
u_th = 2

Wi = -300
We = 68
u_th = 2
Ce = 0.4
Ci = 0.1
de = 14
di = 42 
dm = 15 
d0 = 5.4


#set up lattice
x = np.array([i for i in range(0,N)])
y = x
xG,yG = np.meshgrid(x,y)

tm = torus_matrix(N,N,Nt)


#activity matrix
cField = np.zeros((N,N,Nt))
u = np.zeros((N,N,Nt))

#initial conditions
u[15,13,0] = 1
"""
u[1,2,0] = 1
u[2,1,0] = 1
u[2,2,0] = 1
"""

#coupling strength fucntion
Wn = mexican_hat_csf(Ce,We,Ci,Wi,d0,dm,1)
Nw = Wn.shape[0]

#time evolution of the states
for t in range(1,Nt):
     for m1 in range(0,N+1):
         for n1 in range(0,N+1):
             
             #from Spiking
             if u[tm(m1,n1,t-1)] == 1:
                 
                 u[tm(m1,n1,t)] = -1
                 
                 
             #from Refractory
             elif u[tm(m1,n1,t-1)] == -1:
                 
                 R = np.random.rand(1)
                 if R < pg:
                     u[tm(m1,n1,t)] = 0
                 elif R >= pg:
                     u[tm(m1,n1,t)] = -1
                     
             #from Accepting
             else:
                     A = np.zeros((Nw,Nw))
                     for ver in range(0,Nw):
                         for hor in range(0,Nw):
                             m2 = m1 - dm + ver
                             n2 = n1 - dm + hor
                             
                             if u[tm(m2,n2,t-1)]==1:
                                 A[hor,ver] = 1
                                 
                     I = sum(sum(Wn*A))
                     p = I - u_th
                     if p>=0:
                         u[tm(m1,n1,t)] = 1
                     else:
                         u[tm(m1,n1,t)] = 0

#create animation of activity
ims = []
fig = plt.figure()
for t in range(0,Nt):
    im = plt.imshow(u[:,:,t],animated=True)
    ims.append([im])
    
ani = animation.ArtistAnimation(fig, ims, interval=300, blit=True, repeat_delay=1)
plt.show()    

elapsed_time = time.time() - start_time
print('time cost = ',elapsed_time)                
                             
                 
             
                 
