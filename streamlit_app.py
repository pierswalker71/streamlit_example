# Imports
import streamlit as st
import pandas as pd
import numpy as np

# Data
df = pd.DataFrame(data = {'Param1':['a', 'b', 'c', 'd'], 'Param2':[10, 15, 20, 25]})

st.write(df)
