import streamlit as st

from black_scholes_v1_02 import black_scholes_price_greeks
from src.price_greeks_plot_v1 import plot_price_vs_spot, plot_delta_vs_spot, plot_gamma_vs_spot, plot_vega_vs_spot

st.set_page_config(page_title="Option Pricer", layout="wide")

st.title("Option Pricer")
st.write("A simple Black-Scholes option pricer with basic Greeks.")

DEFAULTS = {
    "option_type": "Call",
    "S0": 100.0,
    "K": 100.0,
    "vol_perc": 20,
    "T": 1.0,
    "r": 0.05,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

with st.sidebar:
    st.header("Inputs")

    if st.button("Reset to defaults"):
        for key, value in DEFAULTS.items():
            st.session_state[key] = value
        st.rerun()

    option_type = st.radio(
        "Option type",
        ["Call", "Put"],
        key="option_type"
    )

    S0 = st.number_input(
        "Stock price S₀",
        min_value=1e-8,
        step=1.0,
        key="S0"
    )

    K = st.number_input(
        "Strike price K",
        min_value=1e-8,
        step=1.0,
        key="K"
    )

    vol_perc = st.slider(
        "Volatility σ (%)",
        min_value=1,
        max_value=100,
        key="vol_perc"
    )

    T = st.slider(
        "Time to expiry T (years)",
        min_value=1e-8,
        max_value=5.0,
        step=0.01,
        key="T"
    )

    r = st.number_input(
        "Risk-free rate r",
        step=0.01,
        key="r"
    )


call = (option_type == "Call")
vol = vol_perc / 100

result = black_scholes_price_greeks(
    call=call,
    S0=S0,
    K=K,
    vol=vol,
    T=T,
    r=r
)

price = result["price"]
delta = result["delta"]
gamma = result["gamma"]
vega = result["vega"]

st.subheader("Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Option Price", f"{price:.2f}")

with col2:
    st.metric("Delta", f"{delta:.3f}")

with col3:
    st.metric("Gamma", f"{gamma:.3f}")

with col4:
    st.metric("Vega", f"{vega:.3f}")


st.divider()

col1, col2 = st.columns([1, 1])

fig1 = plot_price_vs_spot(call, S0, K, vol, T, r)
fig2 = plot_delta_vs_spot(call, S0, K, vol, T, r)
fig3 = plot_gamma_vs_spot(call, S0, K, vol, T, r)
fig4 = plot_vega_vs_spot(call, S0, K, vol, T, r)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

col1, col2 = st.columns([1, 1])

with col1:
    st.pyplot(fig3)

with col2:
    st.pyplot(fig4)
