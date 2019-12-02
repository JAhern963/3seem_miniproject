# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:31:43 2019

@author: Jake
"""
import numpy as np 

class torus_matrix:
    def __init__(self,N=100,M=100,t=1):
        self.N = N                                  
        self.M = M 
        self.matrix = np.zeros((N,M,t))
         
    def __call__(self,n,m,t):
        
        while n > self.N:
             n+= -self.N
        while n < 0:
            n+=  self.N
        if n == self.N:
            n = 0
            
        while m > self.M:
            m+= -self.M  
        while m < 0:
            m+= self.M
        if m == self.M:
            m = 0
            
        return (n,m,t)
    
"""
    def set_value(self,n,m,t,value):
        
        index = self(n,m,t)
        self.matrix[index] = value 
     
        
    def get_value(self,n,m,t):
        index = self(n,m,t)
        
        return self.matrix[index] 
    
    def get_matrix_by_time(self,t):
        return self.matrix[:,:,t]
        
"""
        
        