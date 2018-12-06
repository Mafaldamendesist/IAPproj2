'''
Grupo 23
Margarida Morais   86473
MafaldaMendes      83502
'''

import itertools

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    def computeProb(self, evid):
        if(self.parents == []):
            #if no parents, then the probability of node being true is the probability given in arrary prob
            prob = self.prob[0]
        
        else:
            #array that contains only the node's parents evidences
            parents_evid = []

            for i in range(len(self.parents)):
                parents_evid.append(evid[self.parents[i]])

            #[[00,01],[10,11]]
            #[[[000,001],[010,011]],[[100,101],[110,111]]]
            #etc...

            #Accessing recursively the value for the desired probability knowing the evidence tuple

            prob = self.prob
            for j in range(len(parents_evid)):
                prob = prob[parents_evid[j]] 
        
        #[false, true]
        return [1 - prob, prob]

class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob
        #prob doesn't contain probabilities, but the existing node objects on the network

    def computePostProb(self, evid):

        prob_true = []
        prob_false = []

        #array containing the indexes of all the unknown evids
        unkn_ev = []
        for i in range(len(evid)):
            if(evid[i] == []):
                unkn_ev.append(i)

        #evid index of the probability to infer
        post_ev = evid.index(-1)

        #array evid
        array_ev = list(evid)

        possibilities = 0

        #use itertools library to give every combination possible o
        for possible_evids in itertools.product([0,1], repeat=len(unkn_ev)):
            for j in range(len(unkn_ev)):
                #unkn_ev_index is the value of the index from the unknown evidence on evid
                unkn_ev_index = unkn_ev[j] 
                #fill the array with the possible evid
                array_ev[unkn_ev_index] = possible_evids[j]

            #compute joint probability using evidence = 0 for the current node
            array_ev[post_ev] = 0
            prob_false.append(self.computeJointProb(array_ev))
            
            #compute joint probability using evidence = 1 for the current node
            array_ev[post_ev] = 1
            prob_true.append(self.computeJointProb(array_ev))
            
            possibilities += 1

        #sum all the possible joint probabilities for false and true
        post_prob_true = 0
        post_prob_false = 0
        for k in range(possibilities):
            post_prob_true += prob_true[k]
            post_prob_false += prob_false[k]

        #normalization constant
        alpha = 1/(post_prob_false + post_prob_true)

        return post_prob_true * alpha


    def computeJointProb(self, evid):
        #joint probability is the multiplication of all values given the evid array
        joint_prob = 1
        for i in range(len(evid)):
            joint_prob = joint_prob * self.prob[i].computeProb(evid)[evid[i]] 
        return joint_prob
