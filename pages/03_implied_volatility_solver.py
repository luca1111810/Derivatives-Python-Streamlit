import streamlit as st

from src.bisection_IV_v1 import solve_IV_bisection, plot_bisection_estimates
from src.newton_raphson_IV_v1_03 import solve_IV_newton_raphson, plot_newton_raphson_estimates

st.set_page_config(page_title="Option Pricer", layout="wide")

st.title("Implied Volatility Solver")
st.write("This solver will determine what volatility is implied by the Black-Scholes input parameters and the market price of an option.")

DEFAULTS = {
    "option_type": "Call",
    "option_price": 10.45,
    "S0": 100.0,
    "K": 100.0,
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

    option_price = st.number_input(
        "Option Price",
        min_value=1e-8,
        value=10.45,
        step=1.0,
        key="option_price"
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

bisection_result = solve_IV_bisection(
    call=call,
    option_price=option_price,
    S0=S0,
    K=K,
    T=T,
    r=r
)

bisection_iterations = bisection_result["iterations"]
bisection_estimates = bisection_result["estimates"]
bisection_IV_est = bisection_estimates[~0]

NR_result = solve_IV_newton_raphson(
    call=call,
    option_price=option_price,
    S0=S0,
    K=K,
    T=T,
    r=r
)

NR_iterations = NR_result["iterations"]
NR_estimates = NR_result["estimates"]
NR_IV_est = NR_estimates[~0]


tab1, tab2 = st.tabs(["Bisection", "Newton-Raphson"])

with tab1:
    st.text("Bisection is a simple divide and conquer algorithm that starts with an initial volatility guess in the middle of some lower and upper bound. " \
    "It then plugs the estimate into the Black-Scholes equation and compares the outputted price to the actual market price. Based on this, we adjust our" \
    "lower/upper volatility estimate bound accordingly and try again.")
    
    st.subheader("Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Implied Volatility", f"{100 * bisection_IV_est:.2f}%")

    with col2:
        st.metric("Iterations for convergence", f"{bisection_iterations}")

    st.divider()


    col1, col2, col3 = st.columns([2, 8, 2])

    fig1 = plot_bisection_estimates(estimates=bisection_estimates)

    with col2:
        st.pyplot(fig1)


with tab2:
    st.text("Newton–Raphson is a root finding algorithm, that finds the implied volatility by iteratively refining " \
    "an initial guess using the difference between the model price and market price, together with the option's vega.")
    
    st.subheader("Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Implied Volatility", f"{100 * NR_IV_est:.2f}%")

    with col2:
        st.metric("Iterations for convergence", f"{NR_iterations}")

    st.divider()


    col1, col2, col3 = st.columns([2, 8, 2])

    fig1 = plot_newton_raphson_estimates(estimates=NR_estimates)

    with col2:
        st.pyplot(fig1)



    

