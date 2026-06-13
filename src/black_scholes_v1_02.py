import numpy as np
from scipy.stats import norm

def black_scholes_price_greeks(call:bool, S0:float, K:float, vol:float, T:float, r:float):

    if S0 <= 0 or K <= 0 or vol <= 0 or T <= 0:
        raise ValueError("S0, K, vol, and T must all be positive.")

    d1 = (np.log(S0 / K) + (r + vol**2 / 2) * T) / (vol * np.sqrt(T))
    d2 = d1 - (vol * np.sqrt(T))

    if call:
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)

    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
        delta = norm.cdf(d1) - 1

    gamma = norm.pdf(d1) / (S0 * vol * np.sqrt(T))
    vega = 0.01 * S0 * norm.pdf(d1) * np.sqrt(T)
    
    return {"price": price,
            "delta": delta,
            "gamma": gamma,
            "vega": vega}