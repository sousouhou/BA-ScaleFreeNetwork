# barabasi albert model algorithm to generate a scale free network.
# Refer to https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model

import numpy as np
import random

# Generated graph is bidirectional, edges are in pairs a->b and b->a
# Every node is not self-linked.
def BA_SFN(N, M0, m) :
    """
        N, number of nodes in the final network.
        M0, initial connected network of M0 nodes.
        m, Each new node is connected to m existing nodes.
    """
    assert( M0 < N )
    assert( m <= M0 )
    
    #adjacency matrix
    AM = np.zeros((N,N))
    
    for i in range(0, M0):
        for j in range(i+1,M0):
            AM[i,j] = 1
            AM[j,i] = 1
    
    # add 'c' node
    for c in range(M0,N):
        Allk = np.sum(AM)  # all  degree    Eki
        ki = np.sum(AM , axis = 1)   # ki each degree for node i
        
        pi = np.zeros(c,dtype=np.float) # probability
        for i in range(0,c):
            pi[i] = ki[i]/(Allk*1.0)
        # print pi
    
        # connect m edges.
        for d in range(0,m):
            rand01 = random.random()  #[0,1.0)
            
            sumpi = 0.0
            for g in range(0,c):
                sumpi += pi[g]
                if sumpi>rand01 :  # connect 'c' node with 'g' node.
                    AM[c,g] = 1
                    AM[g,c] = 1                    
                    break
    
    return AM    
    
    
if __name__ == '__main__':

    re_AM = BA_SFN(200,3,2)
    
    pfile = open("result-scale-free-network.txt", "w")
    
    pfile.write("Adjacency matrix: \n")
    for i in range(0, re_AM.shape[0] ) :
        for j in range(0, re_AM.shape[1] ) :
            pfile.write("%.0f "%re_AM[i,j])
        pfile.write("\n")
    
    pfile.write("\n----------\nAdjacency list: \n")
    for i in range(0, re_AM.shape[0] ) :
        pfile.write("%3d -> "%i   )
        for j in range(0, re_AM.shape[1] ) :    
            if 1 == re_AM[i,j] :
                 pfile.write("%d "%j   )
        pfile.write("\n")        
    
        
    pfile.close()

    
    
    
    
    