#a sample porject for option valuations

def bsm_call_value(S0,K,T,r,sigma):
    from math import log,sqrt,exp
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0 / K ) + (r + 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    d2 = (log(S0 / K ) + (r - 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1,0.0,1.0)
            - K * exp(-r * T) * stats.norm.cdf(d2,0.0,1.0))
    return value
    
def bsm_vega(S0,K,T,r,sigma):
    from math import log,sqrt
    from scipy import stats 
    S0 = float(S0)
    d1 = (log(S0 / K ) + (r + 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1,0.0,1.0) * sqrt(T)

    return vega

def bsm_implied_volatility(S0,K,T,r,C0,sigma_est, it= 100):
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0,K,T,r,sigma_est) - C0)
                     / bsm_vega(S0,K,T,r,sigma_est))
    return sigma_est
    
    