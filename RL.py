'''
Grupo 23
Margarida Morais   86473
MafaldaMendes      83502
'''

import numpy as np
import random

from tempfile import TemporaryFile
outfile = TemporaryFile()
	
class finiteMDP:

    def __init__(self, nS, nA, gamma, P=[], R=[], absorv=[]):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((self.nS,self.nA))
        self.P = P
        self.R = R
        self.absorv = absorv
        # completar se necessario
        
            
    def runPolicy(self, n, x0,  poltype = 'greedy', polpar=[]):
        #nao alterar
        traj = np.zeros((n,4))
        x = x0
        J = 0
        #n is the number of "episodes", times that the agent makes this path
        for ii in range(0,n):
            a = self.policy(x,poltype,polpar)
            r = self.R[x,a]
            y = np.nonzero(np.random.multinomial( 1, self.P[x,a,:]))[0][0]
            #y is the final state given initial state x and action a, and having the probability p
            traj[ii,:] = np.array([x, a, y, r])#new step on the trajectory
            J = J + r * self.gamma**ii
            if self.absorv[x]:
                y = x0
            x = y
        
        return J,traj


    def VI(self):
        #nao alterar
        nQ = np.zeros((self.nS,self.nA))
        while True:
            self.V = np.max(self.Q,axis=1) 
            for a in range(0,self.nA):
                nQ[:,a] = self.R[:,a] + self.gamma * np.dot(self.P[:,a,:],self.V)
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
            if err<1e-7:
                break

        #update policy
        self.V = np.max(self.Q,axis=1) 

        #correct for 2 equal actions
        self.Pol = np.argmax(self.Q, axis=1)  

        return self.Q,  self.Q2pol(self.Q)

            
    def traces2Q(self, trace):
        #Q is the matrix containing the Q values for all states and for each one the available action

        Q_aux = np.zeros((self.nS,self.nA))

        alpha = 0.7 #substitutes previous knowledge but not completely

        while True:
            for t in trace: #t = [initial state, acction, final state, reward]
                Q_aux[int(t[0]), int(t[1])] = Q_aux[int(t[0]), int(t[1])] + alpha * (t[3] + self.gamma * max(Q_aux[int(t[2]),:]) - Q_aux[int(t[0]), int(t[1])])

            error_scope = np.linalg.norm(self.Q - Q_aux)
            self.Q = np.copy(Q_aux)

            if error_scope < 1e-2:
                break

        return self.Q
    
    def policy(self, x, poltype = 'exploration', par = []):
        
        if poltype == 'exploitation':
            #exploiting -> maximize Q
            a = np.argmax(par[x,:])
            
        elif poltype == 'exploration':
            #exploring -> agent is exploring the world so he is not interested in the rewards
            a = np.random.randint(self.nA)
 
        return a
    
    def Q2pol(self, Q, eta=5):
        return np.exp(eta*Q)/np.dot(np.exp(eta*Q),np.array([[1,1],[1,1]]))
