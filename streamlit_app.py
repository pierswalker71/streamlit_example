
import streamlit as st

def main():
    # Imports
    import pandas as pd
    import numpy as np
    from random import random 
    #=================================================================


    # Settings
    st.set_page_config(page_title = 'Example App', initial_sidebar_state = 'expanded') 
    
    # Initialisation
    num_initial_rows = 10
    if 'data' not in st.session_state:
        st.session_state['data'] = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=num_initial_rows).tolist(), 
                                'Param2':np.random.uniform(low=50, high=100, size=num_initial_rows).tolist()})
    
    if 'new_rows' not in st.session_state:
        st.session_state['new_rows'] = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=3).tolist(), 
                                        'Param2':np.random.uniform(low=50, high=100, size=3).tolist()})
        
    #-----------------------------------------------------------------
    # Set flags as false. These get set to True on the assocaited streamlit button
    submit_delete = False
    submit_append = False
   
    # Title
    st.title('Example Streamlit App')
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('This is a simple Streamlit App example. It demonstrates the application of hosting an App on Streamlit interfacing with code hosted on my Github')

    # Data
    st.subheader('Create data table') 
    with st.expander('Current data'):
        st.dataframe(st.session_state['data'])
                                    
    #=================================================================
    st.subheader('Data Modification') 
    
    # Append new rows section
    with st.expander('Append new rows'):
        append_num = st.slider('Number of rows to add to bottom of table', min_value=1, max_value=5, value=1, step=1)
        if len(st.session_state['data'].index)>0:
            idx = [x for x in range(st.session_state['data'].index.max()+1,st.session_state['data'].index.max()+1+append_num)]
        else:
            idx = [x for x in range(0,append_num)]
            
        np.random.seed(idx[0])    
        st.session_state['new_rows'] = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=append_num).tolist(), 
                                                               'Param2':np.random.uniform(low=50, high=100, size=append_num).tolist()},
                                                           index = idx)
        st.write(f'rows to be added:')
        st.dataframe(st.session_state['new_rows'])
        submit_append = False
        submit_append = st.button('Append rows')   
                               
    if submit_append:
        st.session_state['data'] = pd.concat([st.session_state['data'],st.session_state['new_rows']])
        submit_append = False
        st.experimental_rerun()
    
    #-----------------------------------------------------------------
    # Delete rows section
    with st.expander('Delete rows'):
        row_ids_to_delete = st.multiselect('Select row IDs to delete',
                                           options=st.session_state['data'].index,
                                           default=st.session_state['data'].index.min())
    
        submit_delete = st.button('Delete rows', disabled=len(st.session_state['data'].index)==1) 
        
        
    if submit_delete:    
        st.session_state['data'] = st.session_state['data'].drop(row_ids_to_delete)
        #col_current_data.dataframe(st.session_state['data'])
        submit_delete = False
        st.experimental_rerun()

     #-----------------------------------------------------------------   
        
if __name__ == '__main__':
    main()
    
