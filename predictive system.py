# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle


loaded_model=pickle.load(open('C:/Users/DELL/Desktop/java_p/trained_model.sav','rb') )

input_data=(1,1,0,1,0,3567,2322,234,360,1.0,1)

input_data_as_numpy_array=np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not eligible for loan')
else:
  print('The person is eligible for loan')