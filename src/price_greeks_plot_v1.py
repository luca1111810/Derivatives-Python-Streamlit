import numpy as np
from matplotlib import pyplot as plt

from src.black_scholes_v1_02 import black_scholes_price_greeks

def plot_price_vs_spot(call, S0, K, vol, T, r):

    spots = np.linspace(0.5 * S0, 1.5 * S0, 100)
    prices = []

    for S in spots:
        result = black_scholes_price_greeks(call, S, K, vol, T, r)
        prices.append(result["price"])

    parameterised_result = black_scholes_price_greeks(call, S0, K, vol, T, r)
    parameterised_price = parameterised_result["price"]

    fig, ax = plt.subplots(figsize=(6, 4))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_title("Option Price", color="white", fontsize=14)

    ax.plot(spots, prices, color="#00B4D8", linewidth=2)
    ax.plot(S0, parameterised_price, color="red", marker="o", markersize=4)

    ax.set_xlabel("Spot price", color="white", fontsize=10)
    ax.set_ylabel("Option price", color="white", fontsize=10)
    
    ax.grid(True, alpha=0.15, color="white")
    ax.tick_params(axis="both", colors="white", labelsize=7)

    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    return fig


def plot_delta_vs_spot(call, S0, K, vol, T, r):

    spots = np.linspace(0.5 * S0, 1.5 * S0, 100)
    prices = []

    for S in spots:
        result = black_scholes_price_greeks(call, S, K, vol, T, r)
        prices.append(result["delta"])

    parameterised_result = black_scholes_price_greeks(call, S0, K, vol, T, r)
    parameterised_price = parameterised_result["delta"]

    fig, ax = plt.subplots(figsize=(6, 4))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_title("Delta", color="white", fontsize=14)

    ax.plot(spots, prices, color="#00B4D8", linewidth=2)
    ax.plot(S0, parameterised_price, color="red", marker="o", markersize=4)

    ax.set_xlabel("Spot price", color="white", fontsize=10)
    ax.set_ylabel("Delta", color="white", fontsize=10)

    ax.grid(True, alpha=0.15, color="white")
    ax.tick_params(axis="both", colors="white", labelsize=7)

    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    return fig


def plot_gamma_vs_spot(call, S0, K, vol, T, r):

    spots = np.linspace(0.5 * S0, 1.5 * S0, 100)
    prices = []

    for S in spots:
        result = black_scholes_price_greeks(call, S, K, vol, T, r)
        prices.append(result["gamma"])

    parameterised_result = black_scholes_price_greeks(call, S0, K, vol, T, r)
    parameterised_price = parameterised_result["gamma"]

    fig, ax = plt.subplots(figsize=(6, 4))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_title("Gamma", color="white", fontsize=14)

    ax.plot(spots, prices, color="#00B4D8", linewidth=2)
    ax.plot(S0, parameterised_price, color="red", marker="o", markersize=4)

    ax.set_xlabel("Spot price", color="white", fontsize=10)
    ax.set_ylabel("Gamma", color="white", fontsize=10)

    ax.grid(True, alpha=0.15, color="white")
    ax.tick_params(axis="both", colors="white", labelsize=7)

    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    return fig


def plot_vega_vs_spot(call, S0, K, vol, T, r):

    spots = np.linspace(0.5 * S0, 1.5 * S0, 100)
    prices = []

    for S in spots:
        result = black_scholes_price_greeks(call, S, K, vol, T, r)
        prices.append(result["vega"])

    parameterised_result = black_scholes_price_greeks(call, S0, K, vol, T, r)
    parameterised_price = parameterised_result["vega"]

    fig, ax = plt.subplots(figsize=(6, 4))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_title("Vega", color="white", fontsize=14)

    ax.plot(spots, prices, color="#00B4D8", linewidth=2)
    ax.plot(S0, parameterised_price, color="red", marker="o", markersize=4)

    ax.set_xlabel("Spot price", color="white", fontsize=10)
    ax.set_ylabel("Vega", color="white", fontsize=10)

    ax.grid(True, alpha=0.15, color="white")
    ax.tick_params(axis="both", colors="white", labelsize=7)

    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    return fig