
import streamlit as st

def main():
    # Imports
    import pandas as pd
    import numpy as np
    from random import random 

    # Settings
    st.set_page_config(page_title = 'Example App', initial_sidebar_state = 'expanded') 
    
    # Initialisation
    if 'data' not in st.session_state:
        st.session_state['data'] = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=3).tolist(), 
                                'Param2':np.random.uniform(low=50, high=100, size=3).tolist()})
    submit_delete = False
    submit_append = False
    
    #=================================================================
    # Title
    st.title('Example Streamlit App')
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('This is a simple Streamlit App example. It demonstrates the application of hosting an App on Streamlit interfacing with my public code hosted on Github')

    # Data
    st.subheader('Create data table') 
    #col_current_data = st.columns(1)
    with st.expander('Current data'):
        st.dataframe(st.session_state['data'])
        #col_current_data.write('test')
        #col_current_data.dataframe(st.session_state['data'])
                                    
    #=================================================================
    st.subheader('Data Modification') 
    
    st.write(f'submit_append: {submit_append}')
    st.write(f'submit_delete: {submit_delete}')
    
    with st.expander('Append new rows'):
        append_num = st.slider('Number of rows to add to bottom of table', min_value=1, max_value=5, value=1, step=1)
        if len(st.session_state['data'].index)>0:
            idx = [x for x in range(st.session_state['data'].index.max()+1,st.session_state['data'].index.max()+1+append_num)]
        else:
            idx = [x for x in range(0,append_num)]
            
        new_rows = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=append_num).tolist(), 
                                                               'Param2':np.random.uniform(low=50, high=100, size=append_num).tolist()},
                                                           index = idx)
        st.write(f'rows to be added:')
        st.dataframe(new_rows)
        submit_append = False
        submit_append = st.button('Append rows')   
                               
    if submit_append:
        st.session_state['data'] = pd.concat([st.session_state['data'],new_rows])
        st.session_state['data'] = st.session_state['data'].sort_index(inplace=True)
        #col_current_data.dataframe(st.session_state['data'])
        submit_append = False
    
    #-----------------------------------------------------------------
    with st.expander('Delete rows'):
        row_ids_to_delete = st.multiselect('Select row IDs to delete',
                                           options=st.session_state['data'].index,
                                           default=st.session_state['data'].index.min())
    
        submit_delete = st.button('Delete rows', disabled=len(st.session_state['data'].index)==1) 
        
        
    if submit_delete:    
        st.session_state['data'] = st.session_state['data'].drop(row_ids_to_delete)
        #col_current_data.dataframe(st.session_state['data'])
        submit_delete = False

     #-----------------------------------------------------------------   
        
if __name__ == '__main__':
    main()
    
