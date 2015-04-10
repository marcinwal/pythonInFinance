
#dSt = rSt dt + sigma * St dZt 
#St = S(t-Delta t) exp ((r - sigma^2 * .5) * Delta t  + sigma sqrt(Deltat Zt))
# hT = max(ST(i) - K, 0)
#mc C0 = exp(-rT) 1/I sum(hT(ST(i)))   - avg of all mc simulations

from time import time
from math import exp,sqrt,log
from random import gquss,seed



seed(2000)
t0 = time()

S0 = 100.
K = 105.
T = 1.
r = 0.05
sigma = .2
M = 50 #time steps
dt = T / M
I = 250000 # number of paths

