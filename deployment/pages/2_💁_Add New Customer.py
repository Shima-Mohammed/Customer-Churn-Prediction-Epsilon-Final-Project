

import streamlit as st
import pandas as pd
import joblib


#read model
predict_status_pipline= joblib.load("models/Classification_Model_Final.pkl")
predict_monthly_charge_pipline= joblib.load("models/Regression_Model_Final.pkl")

def predict_monthly_charge(df):
     df.drop(['MonthlyCharge'],inplace=True,axis=1)
     result = predict_monthly_charge_pipline.predict(df)
     st.markdown(f" <h6 style='text-align:center;margin-bottom:20px;background-color:rgb(135, 211, 124);color:white ;padding-top: 20px;border-radius: 30px'>The monthly charge will be {result} </h6> " , unsafe_allow_html=True)
     return result

def prediction_status(df):
    df['MonthlyCharge'] = predict_monthly_charge(df)
    df = df.drop(['CustomerID'],axis=1)
    result= predict_status_pipline.predict(df)
    if result[0] == 1 :
          st.markdown(" <h6 style='text-align:center;margin-bottom:20px;background-color:rgb(135, 211, 124);color:white ;padding-top: 20px;border-radius: 30px'>This customer will stay</h6> " , unsafe_allow_html=True)
    else :
          st.markdown(" <h6 style='text-align:center;margin-bottom:20px;background-color:rgb(214, 69, 65);color:white;padding-top: 20px;border-radius: 30px'>This customer may leave , kindly ةake him an offer</h6> " , unsafe_allow_html=True)
    return result[0]


with st.form("my_form"):
        # title 
        st.markdown(" <h1 style='text-align:center;margin-bottom:20px'>Add New Customer</h1> " , unsafe_allow_html=True)
        #form
        CustomerID = st.text_input("Customer ID")
        Gender = st.radio("Gender",['Male', 'Female'],horizontal=True,index=None)
        Age = st.slider('Age',19 , 80, 25)
        Married = st.radio("Married",['Yes', 'No'],horizontal=True,index=None)
        NumberofDependents = st.radio("Number of Dependents",[0, 1,2,3],horizontal=True,index=None)
        NumberofReferrals = st.number_input('Number of Referrals', min_value=0, max_value=9,step=1)
        TenureinMonths = st.slider('Tenure in Months',1 , 72, 3)
        Offer  = st.selectbox(label='Offer',options=('No Offer', 'Offer A', 'Offer B','Offer C','Offer D'),index=None,placeholder="Choose an offer") 
        PhoneService  = st.radio("Phone Service",['Yes', 'No'],horizontal=True,index=None) #,on_change=change_phone_service
        MultipleLines = st.radio("MultipleLines",['Yes', 'No','No Phone Service'],horizontal=True,index=None)
        InternetService = st.radio("Internet Service",['Yes', 'No'],horizontal=True,index=None)
        InternetType = st.selectbox('Internet Type',('Fiber Optic', 'DSL', 'Cable','No Internet Service'),index=None,placeholder='Choose an internet type') 
        AvgMonthlyGBDownload = st.slider('Avg Monthly GB Download',2 , 85, 21)
        OnlineSecurity =  st.radio("Online Security",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        OnlineBackup  =   st.radio("Online Backup",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        DeviceProtectionPlan =  st.radio("Device Protection Plan",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        PremiumTechSupport  =   st.radio("Premium Tech Support",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        StreamingTV =  st.radio("Streaming TV",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        StreamingMovies  =   st.radio("Streaming Movies",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        StreamingMusic =  st.radio("Streaming Music",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        UnlimitedData  =   st.radio("Unlimited Data",['Yes', 'No','No Internet Service'],horizontal=True,index=None)
        Contract = st.selectbox('Contract',('Month-to-Month', 'One Year', 'Two Year'),index=None,placeholder='Choose a contract') 
        PaperlessBilling = st.radio("Paperless Billing",['Yes', 'No'],horizontal=True,index=None)
        PaymentMethod = st.selectbox('Payment Method',('Bank Withdrawal', 'Credit Card', 'Mailed Check'),index=None,placeholder='Choose a payment method') 
        
        validation_object = {
              "CustomerID":CustomerID , 
              "Gender":Gender ,
              "Age":Age , 
              "Married":Married, 
              "NumberofDependents":NumberofDependents , 
              "NumberofReferrals":NumberofReferrals,
              "TenureinMonths":TenureinMonths , 
              "Offer":Offer,
              "PhoneService":PhoneService , 
              "MultipleLines":MultipleLines,
              "InternetService":InternetService,
              "InternetType":InternetType,
              "OnlineSecurity":OnlineSecurity,
              "OnlineBackup":OnlineBackup,
              "DeviceProtectionPlan":DeviceProtectionPlan,
              "PremiumTechSupport":PremiumTechSupport,
              "StreamingTV":StreamingTV,
              "StreamingMovies":StreamingMovies,
              "StreamingMusic":StreamingMusic,
              "UnlimitedData":UnlimitedData,
              "Contract":Contract,
              "PaperlessBilling":PaperlessBilling,
              "PaymentMethod":PaymentMethod , 
              'AvgMonthlyGBDownload':AvgMonthlyGBDownload,
              'MonthlyCharge':50
        }
        # Every form must have a submit button.
        Save = st.form_submit_button("Save")#, on_click=disable , disabled=st.session_state.disabled
        if Save:
            for i in validation_object.keys():
                if validation_object[i] == '' or validation_object[i] ==  None  : 
                    st.markdown(f"<span style='margin-bottom:20px;color:red'>the {''.join(' ' + char if char.isupper() else char.strip() for char in i).strip()} should have a value </span> " , unsafe_allow_html=True)
                    st.session_state.disabled = False
                    break 
            else: 
                # call ML Model 
                test_df = pd.DataFrame({k: [v] for k, v in validation_object.items()})
                prediction_status(test_df)


             