import itertools

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    def computeProb(self, evid):
        if(self.parents == []):
            prob = self.prob[0]
        
        else:
            #only parent evids array
            parents_evid = []

            for i in range(len(self.parents)):
                parents_evid.append(evid[self.parents[i]])

            prob = self.prob
            for j in range(len(parents_evid)):
                prob = prob[parents_evid[j]] #recursively getting deeper
        
        return [1 - prob, prob]

class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):

        prob_true = []
        prob_false = []

        #todas as combinacoes possiveis de evids desconhecidos, ou seja, []
        #guardar indices dos evids desconhecidos
        unkn_ev = []
        for i in range(len(evid)):
            if(evid[i] == []):
                unkn_ev.append(i)

        #indice da probabilidade que queremos calcular
        post_ev = evid.index(-1)

        array_ev = list(evid)

        #utilizar biblioteca para ter todas as combinações possiveis 
        for possible_evids in itertools.product([0,1], repeat=len(unkn_ev)):
            for j in range(len(unkn_ev)):
                unkn_ev_index = unkn_ev[j] #unkn_ev_index tem o valor do index correspondente no array de evid que e desconhecido

                array_ev[unkn_ev_index] = possible_evids[j]

            array_ev[post_ev] = 0
            prob_false.append(self.computeJointProb(array_ev)) #joint probability para o valor que queremos saber quando este é falso
            
            array_ev[post_ev] = 1
            prob_true.append(self.computeJointProb(array_ev))#joint probability para o valor que queremos saber quando este é verdadeiro

        #somar todos os valores de todas as joint probabilities possiveis que calculamos acima para obter a post probability
        post_prob_true = 0
        post_prob_false = 0
        for k in range(len(prob_true)):
            post_prob_true += prob_true[k]
            post_prob_false += prob_false[k]

        #alpha serve para fazer a normalizacao
        alpha = 1/(post_prob_false + post_prob_true)

        return post_prob_true * alpha


    def computeJointProb(self, evid):
        
        joint_prob = 1
        for i in range(len(evid)):
            joint_prob = joint_prob * self.prob[i].computeProb(evid)[evid[i]] 
            # para cada nó fazer:
            # 1º - calcular probabilidade do nó
            # 2º - consoante o evid, ir buscar a probabilidade de ser falso ou verdadeiro 
        return joint_prob
