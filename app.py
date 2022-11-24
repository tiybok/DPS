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
    <h1 style ="color:black;text-align:center;">Streamlit DPS CHALLENGE ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
    #Category,Accident_Type,Year,Month  
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Category = st.text_input("Category", "Type Here")
    Accident_Type = st.text_input("Accident_Type", "Type Here")
    Year = st.text_input("Year", "Type Here")
    Month = st.text_input("Month", "Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Category,Accident_Type,Year,Month)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()

