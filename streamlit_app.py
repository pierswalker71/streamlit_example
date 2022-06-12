
import streamlit as st

def main():
    # Imports
    import pandas as pd
    import numpy as np
    from random import random 
    
    # Settings
    st.set_page_config(page_title = 'Example App', initial_sidebar_state = 'expanded') 

    # Title
    st.title('Example Streamlit App')
    st.write('Piers Walker 2022')
    st.write('This is a simple Streamlit App example which demonstrates the application of hosting an App on Streamlit, interfacing with public code hosted on Github')

    # Data
    st.subheader('Set data table size') 
    num_rows_required = st.number_input('Number of rows')
    st.subheader('Display current data') 
    data = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=num_rows_required).tolist()}, 
                                {'Param2':np.random.uniform(low=50, high=100, size=num_rows_required).tolist()})
    st.dataframe(data)
                                
    #st.write(np.random.uniform(low=0, high=10, size=num_rows_required).tolist())
    
    st.subheader('Selections') 
    #st.slider('Consecutive subset', 0, len(data.index), 1) 

    #submit = st.button('Submit')  
    
if __name__ == '__main__':
    main()
    
