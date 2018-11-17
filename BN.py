# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents

    def computeProb(self, evid):
        if(self.parents.len() > 1){
            left_evid = evid[self.parents[0]];
            right_evid = evid[self.parents[1]];

            prob_true = self.prob[left_evid][right_evid]
            prob_false = 1 - prob_true

            prob = [prob_false, prob_true]

            return prob
        }

        elif(self.parents.len() == 1) {
            parent_evid = evid[self.parents]

            prob_true = self.prob[parent_evid]
            prob_false = 1 - prob_true

            prob = [prob_false, prob_true]

            return prob
        }

        else {
            prob_true = self.prob
            prob_false = 1 - prob_true

            prob = [prob_false, prob_true]

            return prob
        }

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
