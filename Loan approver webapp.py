# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 07:30:20 2024

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/DELL/Desktop/java_p/trained_model.sav','rb'))

def loan_aprrove(input_data):
    

    input_data_as_numpy_array=np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not eligible for loan'
    else:
      return 'The person is eligible for loan'
  
def main():
    
    #giving a title
    st.title('Loan predictor web app')
    
    #getting input data
  
    
    Gender=st.text_input('Enter your gender')
    Married=st.text_input('Enter your relationship status')
    Dependents=st.text_input('Enter number of dependents')
    Education=st.text_input('Enter your education')
    Self_Employed=st.text_input('Enter your emp type')
    Income=st.text_input('Enter your income')
    Co_applicant=st.text_input('Enter your co applicant income')
    Amount=st.text_input('Enter your amount')
    Term=st.text_input('Enter your term')
    credit_score=st.text_input('Enter your credit score')
    property_area=st.text_input('Enter your property area')
    
    #code for prediction
    diagnosis=''#null string that stores the output string(yes or no)
    
    #creating a button for prediction
    
    if st.button('check loan eligibility'):
        diagnosis =  loan_aprrove([Gender,Married,Dependents,Education,Self_Employed, Income,Co_applicant, Amount,Term,
                                     credit_score,property_area ])
    st.success(diagnosis)
     


if __name__=='__main__':
    main()
    