import pandas as pd
import pickle as PK
import streamlit as st
 
model = PK.load(open('C:\python\house price prediction ML project\House_Prediction_Model.pkl', 'rb'))                       
 
st.header("House Price Prediction App")

st.header('kolkata house prices predictor')
data = pd.read_csv('C:\python\house price prediction ML project\cleaned_data.csv')                                                        #python -m streamlit run app.py
loc=st.selectbox('Choose the Location',data['Location'].unique())
Sqft= st.number_input('Enter the Area in sqft')
bedrooms= st.number_input('Enter the No. of Bedrooms')
bathrooms= st.number_input('Enter the No. of Bathrooms')



input=pd.DataFrame([[Sqft,loc,bedrooms,bathrooms]], columns =['Area','Location','No. of Bedrooms','No. of Bathrooms'])

if st.button('Predict Price'):
    output = model.predict(input)
    out_str = 'price of the house is Rs. ' + str(int(output[0]/1.8))
    st.success(out_str)
    
    
    
   
