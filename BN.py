# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents
        self.result = []

    def computeProb(self, evid):
        if(len(self.parents) > 1):
            left_evid = evid[self.parents[0]];
            right_evid = evid[self.parents[1]];

            prob_true = self.prob[left_evid][right_evid]
            prob_false = 1 - prob_true

            prob = [prob_false, prob_true]

            self.result.append(prob)

            # return result

        elif(len(self.parents) == 1):
            parent_evid = evid[self.parents[0]]

            prob_true = self.prob[parent_evid]
            prob_false = 1 - prob_true

            prob = [prob_false, prob_true]

            self.result.append(prob)

            # return result

        else:
            prob_true = self.prob
            prob_false = 1 - prob_true

            prob = [prob_false, prob_true]

            self.result.append(prob)

            # return result

        def __repr__(self):
            return result

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
