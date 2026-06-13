import streamlit as st

st.set_page_config(
    page_title="Derivatives Lab",
    layout="wide"
)

pages = {
    # "Home": [
    #     st.Page("pages/00_home.py", title="Home"),
    # ],
    # "Tools": [
    #     st.Page("pages/01_option_pricer.py", title="Option Pricer"),
    #     st.Page("pages/02_strategy_builder.py", title="Strategy Builder"),
    #     st.Page("pages/03_implied_volatility_solver.py", title="Implied Volatility Solver")
    # ],
        "Pages": [
         st.Page("pages/00_home.py", title="Home"),
         st.Page("pages/01_option_pricer.py", title="Option Pricer"),
         st.Page("pages/02_strategy_builder.py", title="Strategy Builder"),
         st.Page("pages/03_implied_volatility_solver.py", title="Implied Volatility Solver")
      ]
}

pg = st.navigation(pages)
pg.run()