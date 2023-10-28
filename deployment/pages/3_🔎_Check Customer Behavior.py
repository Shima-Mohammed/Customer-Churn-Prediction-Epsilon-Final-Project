import streamlit as st
import pandas as pd
import joblib


#read model
mypipeline= joblib.load("models/Classification_Model_Final.pkl")

def prediction(df):
    result= mypipeline.predict(df)
    if result[0] == 1 :
          st.markdown(" <h6 style='text-align:center;margin-bottom:20px;background-color:rgb(135, 211, 124);color:white ;padding-top: 20px;border-radius: 30px'>This customer will stay</h6> " , unsafe_allow_html=True)
    else :
          st.markdown(" <h6 style='text-align:center;margin-bottom:20px;background-color:rgb(214, 69, 65);color:white;padding-top: 20px;border-radius: 30px'>This customer may leave , kindly ةake him an offer</h6> " , unsafe_allow_html=True)
    return result[0]

with st.form("my_form"):
        st.markdown(" <h1 style='text-align:center;margin-bottom:20px'>Check Customer Behavior</h1> " , unsafe_allow_html=True)
        CustomerID = st.text_input("Customer ID")
        # Every form must have a submit button.
        Check = st.form_submit_button("Check")

        if Check:
            if CustomerID == '' : 
                  st.markdown(" <span style='margin-bottom:20px;color:red'>the Customer ID should have a value </span> " , unsafe_allow_html=True)
            else :
                df = pd.read_csv('data/customer_data.csv').reset_index(drop=True)
                if df[df['Customer_id'] == int(CustomerID) ].shape[0] == 0 : 
                     st.markdown(" <span style='margin-bottom:20px;color:red'>Invalid Customer ID</span> " , unsafe_allow_html=True)
                else :
                     df = df[df['Customer_id'] == int(CustomerID)]
                     df.drop(['Customer_id'],axis=1,inplace=True)
                     prediction(df)

                     