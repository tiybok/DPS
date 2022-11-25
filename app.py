#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'

def prediction(Category,Accident_Type,Year,Month):  
   
    prediction = classifier.predict(
        [[Category,Accident_Type,Year,Month]])
    print(prediction)
    return prediction
      
# This is the main function in which we define our webpage
def main():
      # giving the webpage a title
    st.title("DPS CHALLENGE")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit DPS CHALLENGE AI APP </h1>
    <h3 style ="color:black;text-align:center;"><a href="https://github.com/tiybok/DPS">More Details </a> </h3>
    <div style ="background-color:black;padding:13px">
    <h4 style ="color:white;text-align:center;"> Category: <br> alcohol accidents --> 0  <br> escape accidents -->1 <br>traffic accidents --> 2 </h4>
    <h4 style ="color:white;text-align:center;"> <br> Accident_Type: <br> all in all --> 0 <br> injured and killed --> 1 <br> with personal injury --> 2 </h4>
    </div>
    """
  
    
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
    #Category,Accident_Type,Year,Month  
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    #Category = st.text_input("Category", "Type Here : 0,1,2")
    Category = st.selectbox("Category", ['0', '1','2'])
    #Accident_Type = st.text_input("Accident_Type", "Type Here :0,1,2")
    Accident_Type = st.selectbox("Accident_Type", ['0', '1','2'])
    Year = st.number_input("Year",2021,2030)
    #Month = st.text_input("Month", "Type Here :MM")
    Month = st.number_input("Month", 1, 12)
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Category,Accident_Type,Year,Month)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()

