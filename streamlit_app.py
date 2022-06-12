# Imports
import streamlit as st

def main():
    import pandas as pd
    import numpy as np
    
    st.set_page_config(page_title = 'Colour Blindness', initial_sidebar_state = 'expanded') 

    # Title
    st.title('Title')
    st.write('Piers Walker 2022')

    # Data
    df = pd.DataFrame(data = {'Param1':['a', 'b', 'c', 'd'], 'Param2':[10, 15, 20, 25]})

    st.write(df)
    
if __name__ == '__main__':
    main()
    
