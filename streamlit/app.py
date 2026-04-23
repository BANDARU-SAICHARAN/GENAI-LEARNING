import streamlit as st
import pandas as pd
import numpy as np   


## Title #

st.title("hello")  

# simple text 

st.write("Here is the simple data ")  

# working with simple data set 

df = pd.DataFrame( {
    'first column ':[1,2,3,4,5],
    'second column':[10,20,30,40,50]
})  


# Display a data set 

st.write(df)


# lime chart 

Chart_data = pd.DataFrame( 

    np.random.random((20,3)),columns=['a','b','c']
)
st.line_chart(Chart_data)
