import streamlit as st
import numpy as np
from classes import NPV
import pandas as pd

header = st.container()
capital_implementation = st.container()
values_implementation = st.container()

with st.sidebar:
    st.markdown("**Currency**")
    currencies = ["PLN", "USD", "JPY", "EUR", "SEK"]
    radio = st.radio("Choose currency:", currencies)

with header:
    st.title("Net Present Value **implementation!**")
    
    col_1, col_2 = st.columns(2)
    slidee = col_1.slider("Please select the percentage of your investment(%):", min_value=1, max_value=50, value=4, step = 1)
    boxx = col_2.selectbox("Please choose how many years you would like to invest:",options=[1,2,3,4,5,6,7,8,9,10], index=0)
    st.write("------------------------------------------------------------------------")

with capital_implementation:
    b_capital = st.number_input("Please input how much would you like to invest:")
    st.write('The value of the investment is ', b_capital, " ", radio)

with st.sidebar:
    st.markdown("**Cash Flow**")
    model_cities = [str(y) for y in list(range(1,boxx + 1))]
    model_count = []
    for i, x in enumerate(model_cities):
        model_count.append(st.number_input(f"Insert Cash Flow value {x} year", value=0))

with values_implementation:
    st.write("##")
    npv = NPV(percentage = slidee, years = boxx)
    rates = [(1 / (1 + (npv.percentage / 100)) ** y) for y in list(range(1, npv.years + 1))]
    added = [round((rates[x] * model_count[x]),2) for x in range(len(model_count))]
    summarize = sum(added)
    check = summarize - b_capital
    
    if check >= 0:
        st.balloons()
        st.metric(label = "NPV", value = f"{round(check,2)} {radio}", delta="You should invest", delta_color="normal")
    else:
        st.metric(label = "NPV", value = f"{round(check,2)} {radio}")
        st.error('You should not invest!')

    st.bar_chart(model_count)
