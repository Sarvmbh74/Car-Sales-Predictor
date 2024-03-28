import streamlit as st
import joblib 
import numpy as np
import pandas as pd
import datetime

model = joblib.load("car_price_predictor")
from warnings import filterwarnings
filterwarnings("ignore")
st.title("Sales Predictor App")

p1 = st.number_input("Price of Cars(In Lakhs)",2.5,25.0,step=1.0)

p2 = st.number_input("Kms Driven",100,5000000,step=100)

s1=st.selectbox("Fuel Type",("Petrol","Diesel","CNG"))
if s1=="Petrol":
    p3=0
elif s1=="Diesel":
    p3=1
elif s1=="CNG":
    p3=2

s2=st.selectbox("Seller Type",("Dealer","Individual"))
if s2=="Dealer":
    p4=0
elif s2=="Individual":
    p4=1



s3=st.selectbox("Transmission",("Manual","Automatic"))
if s3=="Manual":
    p5=0
elif s3=="Automatic":
    p5=1


p6=st.slider("Number of Owners the Cars Previously had",0,3)
date_time=datetime.datetime.now()

years=st.number_input("In which car was purchased ?",1990,date_time.year)

p7=date_time.year -years


data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Car_Age':p7
},index=[0])


if st.button('Predict'):
    pred = model.predict(data_new)
    if pred>0:
         st.balloons()
         st.success("You can sell your car for {:.2f} Lakhs".format(pred[0]))
    else:
        st.warning("You can't able to sell this car")