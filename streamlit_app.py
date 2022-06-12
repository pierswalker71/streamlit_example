
import streamlit as st

def main():
    # Imports
    import pandas as pd
    import numpy as np
    from random import random 

    # Settings
    st.set_page_config(page_title = 'Example App', initial_sidebar_state = 'expanded') 
    
    #initialisation
    #if 'data_original' not in st.session_state:
    #    st.session_state['data_original'] = pd.DataFrame()
    if 'data' not in st.session_state:
        st.session_state['data'] = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=10).tolist(), 
                                'Param2':np.random.uniform(low=50, high=100, size=10).tolist()})

    # Title
    st.title('Example Streamlit App')
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('This is a simple Streamlit App example. It demonstrates the application of hosting an App on Streamlit interfacing with my public code hosted on Github')

    # Data
    st.subheader('Create data table') 
    
    with st.expander('Current data'):
        st.dataframe(st.session_state['data'])
                                    
    
    st.subheader('Data Modification') 
    
    with st.expander('Delete rows'):
        row_ids_to_delete = st.multiselect('Select row IDs to delete',
                                           options=st.session_state['data'].index,
                                           default=st.session_state['data'].index.min())
    
        submit_delete = False
        submit_delete = st.button('Delete rows')  
        
    if submit_delete:    
        st.session_state['data'] = st.session_state['data'].drop(row_ids_to_delete)
        submit_delete = False

if __name__ == '__main__':
    main()
    
