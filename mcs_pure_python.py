
#dSt = rSt dt + sigma * St dZt 
#St = S(t-Delta t) exp ((r - sigma^2 * .5) * Delta t  + sigma sqrt(Deltat) * Zt)
# hT = max(ST(i) - K, 0)
#mc C0 = exp(-rT) 1/I sum(hT(ST(i)))   - avg of all mc simulations

S0 = 100.
K = 105.
T = 1.
r = 0.05
sigma = 0.2
M = 50 #time steps
dt = T / M
I = 250000 # number of paths


def simple_MC(): 
    from time import time
    from math import exp,sqrt
    from random import gauss,seed
    seed(2000)
    t0 = time()
    

    
    S = []
    for i in range(I):
        path = []
        for t in range(M+1):
            if t == 0:
                path.append(S0)
            else:
                z = gauss(0.0,1.0)
                St = path[t - 1] * exp((r - 0.5 * sigma ** 2) * dt
                                        + sigma * sqrt(dt) * z)
                path.append(St)
        S.append(path)
    
    C0 = exp(-r * T ) * sum([max(path[-1] - K,0) for path in S]) / I
    tpy  = time() - t0
    print "european otion value %7.3f" % C0
    print "duration is sec %7.3f" % tpy

def vector_MC():
    import numpy as np
    import math 
    from time import time
    
    np.random.seed(2000)
    t0 = time()
    
    S = np.zeros((M+1,I))
    S[0] = S0
    
    for t in range(1,M+1):
        z = np.random.standard_normal(I) #pseduo numbers 
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt 
                            + sigma * math.sqrt(dt) * z)
    
    C0 = math.exp(-r*T)*np.sum(np.maximum(S[-1] - K,0)) / I
    tmp = time() - t0
    
    print "option price using vector_MC = %7.3f" %C0
    print "in time %7.3f" %tmp
    
def full_vector_MC():
    import math
    from numpy import *
    from time import time
    
    random.seed(2000)
    t0 = time()    
    
    S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt 
                        + sigma * math.sqrt(dt)
                        * random.standard_normal((M+1,I)),axis=0))
    S[0] = S0
    
    C0 = math.exp(-r * T) * sum(maximum(S[-1] - K,0)) / I    
    tmp2 = time() - t0
    
    print "european otion value %7.3f" % C0
    print "duration is sec %7.3f" % tmp2

        