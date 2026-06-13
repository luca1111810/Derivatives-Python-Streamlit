import numpy as np
from matplotlib import pyplot as plt

from src.black_scholes_v1_02 import black_scholes_price_greeks

def solve_IV_bisection(call, option_price, S0, K, T, r, tol=1e-3, max_iters=1000):
    vol_low, vol_high = 0, 1
    vol_estimates = []

    for i in range(max_iters):
        vol_est = (vol_low + vol_high) / 2
        vol_estimates.append(vol_est)
        price_est = black_scholes_price_greeks(call, S0, K, vol_est, T, r)["price"]

        if abs(price_est - option_price) < tol:
            return {"iterations": i,
                    "estimates": vol_estimates}
        elif price_est > option_price:
            vol_high = vol_est
        else:
            vol_low = vol_est

    return {"iterations": -1,
            "estimates": vol_estimates}


def plot_bisection_estimates(estimates):

    fig, ax = plt.subplots(figsize=(6, 4))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_title("Estimating IV - Bisection", color="white", fontsize=14)

    ax.plot(estimates, color="#00B4D8", linewidth=2)
    ax.hlines(estimates[~0], xmin=0, xmax=len(estimates), color="g", linestyle="dashed")

    ax.set_xlabel("Iteration", color="white", fontsize=10)
    
    ax.grid(True, alpha=0.15, color="white")
    ax.tick_params(axis="both", colors="white", labelsize=7)

    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.legend(["Estimates", "Convergence value"])

    return fig