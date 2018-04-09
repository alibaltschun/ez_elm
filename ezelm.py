# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 19:41:57 2018

@author: kony
"""
import numpy as np
from numpy.linalg import inv

class EzELM(object):
    
    W = []
    b = []
    bt = []
        
    def train(self,X,y,hiddenlayer):
        
        global W
        global b
        global bt
        
        self.W = np.random.rand(X.shape[1],hiddenlayer)
        self.b = np.random.rand(1,hiddenlayer)
        
        B = []
        for i in range(0,X.shape[0]):
            B.append((self.b[0]).tolist())
        
        self.W = np.matrix(self.W)
        B = np.matrix(B)
    
        tempH = X * self.W + B
        H = 1/(1+np.exp(-tempH))
        
        self.bt = inv(np.transpose(H)*H) * np.transpose(H) * np.transpose(y)
                 
    def pred(self,y):
        result = []
        for i in range(0,len(y)):
            tempH = y[i] * self.W + self.b
            H = 1/(1+np.exp(-tempH))
            if (H*self.bt > 0):
                result.append(1)
            else:
                result.append(-1)
        return result