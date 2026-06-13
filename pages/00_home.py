import streamlit as st

st.set_page_config(
    page_title="Home",
    layout="wide"
)

st.title("Derivatives Workbench")

st.write("""
Welcome to the Derivatives Workbench.

Use the navigation menu on the left to explore:

-> 📈 Option Pricer\n
-> 💰 Strategy Builder\n
-> 🔍 Implied Volatility Solver
""")