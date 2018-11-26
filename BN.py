# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []): 
        self.parents = parents
        self.prob = prob
        self.result = []
        
      
        
    def computeProb(self, evid):
        if(len(self.parents)>1):
            left_evid = evid[self.parents[0]]
            right_evid =evid[self.parents[1]]
            
            prob_true = self.prob[left_evid][right_evid]
            prob_false = 1 - prob_true
            self.result=[]
            self.result.append(prob_false);
            self.result.append(prob_true); 
        elif(len(self.parents) == 1):
            parents_evid = evid[self.parents[0]]
            
            prob_true = self.prob[0][parents_evid]
            
            self.result=[]
    
            self.result.append(prob_true);
        else:
            prob_true = self.prob[0]
            prob_false = 1 - prob_true
            self.result=[]
            self.result.append(prob_false);
            self.result.append(prob_true);
        return self.result
    
    def __repr__(self):
        return "Baye results: {}".format(self.result) 
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):
        pass

        return 0


    def computeJointProb(self, evid):
        pass

        return 0
