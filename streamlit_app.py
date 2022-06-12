
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
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('This is a simple Streamlit App example. It demonstrates the application of hosting an App on Streamlit interfacing with my public code hosted on Github')

    # Data
    st.subheader('Create data table') 
    
    num_rows_required = st.number_input('Number of rows',min_value=5, max_value=50, value=5)
    
    #st.subheader('Display current data') 
    data_original = pd.DataFrame(data = {'Param1':np.random.uniform(low=0, high=10, size=num_rows_required).tolist(), 
                                'Param2':np.random.uniform(low=50, high=100, size=num_rows_required).tolist()})
    
    with st.expander('Original data'):
        st.dataframe(data_original)
    
    data = data_original.copy()
    
    with st.expander('Current data'):
        st.dataframe(data)
                                    
    
    st.subheader('Data Modification') 
    #st.slider('Consecutive subset', 0, len(data.index), 1) 
    
    row_ids_to_delete = st.multiselect('Select row IDs to delete',options=data.index,default=data.index.min())
    
    submit = False
    submit = st.button('Delete rows')  
    if submit:    
        data.drop(row_ids_to_delete,inplace=True)
    
    
    #abc = st.number_input('Row ID to deleteows',min_value=data.index.min(), max_value=data.index.max(), value=data.index.max())
    
if __name__ == '__main__':
    main()
    
